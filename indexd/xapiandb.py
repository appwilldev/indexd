# vim:fileencoding=utf-8:sw=4

import os
import io
import re
import logging
import ConfigParser
from collections import OrderedDict

import xapian
import scws

import util
from exceptions import *

_open_dbs = {}
_dbpath = None
_scws_args = None
logger = logging.getLogger(__name__)

def isep(array, sep):
    m = len(array)
    for i, x in enumerate(array):
        yield x
        if i+1 < m: yield sep

def _scws(sentence):
    global _scws
    if _scws_args is None:
        raise AWIPServerError('SCWS dict and rules not set yet')
    _scws = scws.SCWS(*_scws_args)
    logger.info('New SCWS created.')
    return _scws(sentence)

def set_dbdir(path):
    global _dbpath
    _dbpath = path

def set_scws_data(dict, rules=None):
    global _scws_args
    _scws_args = (dict, rules)
    logger.info('SCWS parameters set to: %r', _scws_args)

def get_db(name, mode):
    if (name, mode) in _open_dbs:
        logger.info('reuse already open db %s, mode %s', name, mode)
        db = _open_dbs[(name, mode)]
        db.db.reopen()
    else:
        try:
            db = XapianDB(name, mode)
        except xapian.DatabaseOpeningError, e:
            raise AWIPOperationError(str(e))
        _open_dbs[(name, mode)] = db
    return db

def _parse_csv_fields(val):
    ret = [x.strip() for x in val.split(',')]
    if ret == ['']:
        ret = []
    return ret

def _validate_dbname(name):
    if not re.match(r'\w+$', name):
        raise AWIPRequestInvalid('inproper index database name')

def _config_file_path(name):
    logger.debug("config file path: %s", os.path.join(_dbpath, name + '.ini'))
    return os.path.join(_dbpath, name + '.ini')

def _validate_config_file(confdata):
    conf = util.CasedConfigParser()

    try:
        conf.readfp(io.StringIO(confdata))
        conf.get('config', 'id')
        lang = conf.get('config', 'lang')
        if lang.lower() not in ('zh', 'chinese'):
            try:
                xapian.Stem(lang)
            except xapian.InvalidArgumentError:
                raise AWIPRequestInvalid('unspported language')

        fields = set(_parse_csv_fields(conf.get('config', 'indexing')))

        for k, v in conf.items('field_prefix'):
            assert k != 'Q', 'reserved prefix'
            conf.get('prefix_name', k)
            vs = _parse_csv_fields(v)
            assert set(vs) <= fields

    except (ConfigParser.Error, TypeError, AssertionError), e:
        raise AWIPRequestInvalid('Invalid config data: %r' % e)

def _extendWithPrefix(l, words, prefix=''):
    if len(words) >= 3 and words[1] == ':':
        extends = ['%s%s:%s' % (prefix, words[0], x) for x in words[2:]]
    else:
        extends = [prefix + x for x in words]
    #endif
    #l.extend([x for x in isep(extends, 'AND')])
    l.extend(extends)

def createdb(name, confdata):
    _validate_dbname(name)
    fn = _config_file_path(name)
    if os.path.exists(fn):
        raise AWIPRequestInvalid('Index database "%s" already exists' % name)

    _validate_config_file(confdata)
    with open(fn, 'w') as f:
        f.write(confdata)

    get_db(name, 'RDWR')

class ZhTermGenerator(object):
    scws = None
    stemmer = None
    def __init__(self):
        self.pos = 0
        if self.stemmer is None:
            self.__class__.stemmer = xapian.Stem('en')

    def set_document(self, doc):
        self.doc = doc

    def index_text(self, text, wdf_inc=1, prefix=u''):
        if not text: return
        text = text.encode('utf-8')
        pos = self.pos
        for word in _scws(text):
            # use English stemmer for Chinese
            try:
                word = self.stemmer(word.lower()).decode('utf-8')
            except UnicodeDecodeError:
                # scws set a max byte length (SCWS_MAX_ZLEN, 128) on words,
                # and may cut off in the middle of a multibyte character. We
                # simply ignore the "damaged" word since no useful word will
                # be so long
                logger.warn('Got a long bad word: %r', word)
                continue
            self.doc.add_posting(u'Z' + prefix + word, pos, wdf_inc)
            pos += 1
        self.pos = pos

    def increase_termpos(self, delta=100):
        self.pos += delta

class XapianDB(object):
    queryparser = None
    termgenerator = None
    config = None

    def __init__(self, name, mode):
        if _dbpath is None:
            raise AWIPServerError('database directory not set yet')
        self.name = name
        self.mode = mode
        dbpath = os.path.join(_dbpath, name)
        if mode == 'RDONLY':
            self.db = xapian.Database(dbpath)
        elif mode == 'RDWR':
            self.db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)
        else:
            raise AWIPServerError('unknown mode passed to %s' % self.__class__.__name__)
        logger.info('index db %s opened with mode %s.', name, mode)

    def get_idfield(self):
        ver = self.get_version()
        if ver >= 1.09:
            return self.config.get('config', 'id')
        else:
            return '_id'

    def get_version(self):
        self.load_config()
        try:
            ver = float(self.config.get('config', 'version'))
        except (ConfigParser.NoOptionError, ValueError):
            ver = 1.0
        return ver

    def query(self, qs, offset, pagesize, sort=[]):
        self.load_queryparser()
        qs = self.prepare_query(qs)
        # the FLAG_BOOLEAN_ANY_CASE is disabled by defaut,
        # so keep the opwords as ALLCAPS please!
        # here can give the flag as the second arg for parse_query
        # see http://xapian.org/docs/apidoc/html/classXapian_1_1QueryParser.html
        query = self.queryparser.parse_query(qs)
        enquire = xapian.Enquire(self.db)
        enquire.set_query(query)
        enquire.set_docid_order(enquire.DONT_CARE);
        # sort is [["key", Bool],...]
        if len(sort) == 1:
            key = self.lookup_sorting_key(sort[0][0])
            enquire.set_sort_by_value_then_relevance(key, sort[0][1])
        elif len(sort) > 1:
            keymaker = xapian.MultiValueKeyMaker()
            try:
                for key, order in sort:
                    keymaker.add_value(self.lookup_sorting_key(key), order)
            except ValueError: # too many values to unpack
                raise AWIPRequestInvalid('bad value for parameter "sort"')
            enquire.set_sort_by_key_then_relevance(keymaker, False)
        return enquire.get_mset(offset, pagesize)

    def lookup_sorting_key(self, key):
        return self.sortingFieldList.index(key)

    def load_queryparser(self):
        if self.queryparser:
            return

        self.load_config()
        config = self.config

        # the FLAG_BOOLEAN_ANY_CASE is disabled by defaut,
        # so keep the opwords as ALLCAPS please!
        self.queryparser = queryparser = xapian.QueryParser()
        self.queryparser.set_default_op(xapian.Query.OP_AND) # default to and
        lang = config.get('config', 'lang')
        if lang.lower() in ('zh', 'chinese'):
            # use English stemmer for Chinese
            queryparser.set_stemmer(xapian.Stem('en'))
        else:
            queryparser.set_stemmer(xapian.Stem(lang))
        queryparser.set_stemming_strategy(queryparser.STEM_ALL_Z)
        for prefix, names in self.prefix_name.items():
            for name in names:
                queryparser.add_prefix(name, prefix)
        queryparser.add_prefix('_id', 'Q')
        logger.info('query parser for %s loaded.', self.name)

    def prepare_query(self, uqs):
        self.load_config()
        lang = self.config.get('config', 'lang')

        if lang.lower() not in ('zh', 'chinese'):
            return uqs

        qs = uqs.encode('utf-8')
        ret = []
        for string in qs.split():
            words = _scws(string)
            words = [w.lower() for w in words]
            try:
                last_is_op = ret[-1] in ('AND', 'OR', 'NOT')
            except IndexError:
                last_is_op = False
            if len(words) == 1:
                if words[0] in ('and', 'or', 'not'):
                    words[0] =  words[0].upper()
                ret.append(words[0])
            elif len(words) >= 3 and words[1] == ':':
                l = []
                if last_is_op: l.append('(')
                _extendWithPrefix(l, words)
                if last_is_op: l.append(')')
                ret.append(" ".join(l))
            elif len(words) >= 2 and words[0] in '-+':
                l = []
                if last_is_op: l.append('(')
                _extendWithPrefix(l, words[1:], prefix=words[0])
                if last_is_op: l.append(')')
                ret.append(" ".join(l))
            else:
                l = []
                if last_is_op: l.append('(')
                #l.extend([x for x in isep(words, 'AND')]) # join by AND after genterm
                l.extend(words)
                if last_is_op: l.append(')')
                ret.append(" ".join(l))
            #endif
        #endfor
        ret = ' '.join(ret).decode('utf-8') #.lower(), do not lower OPS!
        logger.debug('Query %r parsed to: %r', uqs, ret)
        return ret

    def load_termgenerator(self):
        if self.termgenerator:
            return

        self.load_config()
        lang = self.config.get('config', 'lang')
        if lang.lower() in ('zh', 'chinese'):
            self.termgenerator = ZhTermGenerator()
        else:
            self.termgenerator = xapian.TermGenerator()
            self.termgenerator.set_stemmer(xapian.Stem(lang))
        logger.info('term generator for %s (lang=%s) loaded.', self.name, lang)

    def load_config(self):
        if self.config:
            return

        config = self.config = util.CasedConfigParser()
        config.readfp(open(_config_file_path(self.name)))

        self.indexingField = _parse_csv_fields(config.get('config', 'indexing'))
        try:
            self.storingField = _parse_csv_fields(config.get('config', 'storing'))
        except ConfigParser.NoOptionError:
            self.storingField = None

        sortingField = self.sortingField = OrderedDict()
        sortingFieldList = self.sortingFieldList = []
        try:
            for f in _parse_csv_fields(config.get('config', 'sorting')):
                if f.startswith('number:'):
                    f = f[7:]
                    sortingField[f] = True
                else:
                    sortingField[f] = False
                sortingFieldList.append(f)
        except ConfigParser.NoOptionError:
            pass

        self.field_prefix = {k: _parse_csv_fields(v) for k, v in
                             config.items('field_prefix')}
        self.prefix_name = {k: _parse_csv_fields(v) for k, v in
                             config.items('prefix_name')}

        logger.info('config file for %s loaded.', self.name)

    def get_document(self, id):
        if isinstance(id, basestring):
            idterm = u'_id:' + id
            ids = self.query(idterm, 0, 1)
            if len(ids) != 1:
                raise KeyError('No such document')
            return ids[0].document
        else:
            return self.db.get_document(id)

    def add_document(self, doc):
        self.load_termgenerator()
        config = self.config
        termgenerator = self.termgenerator

        xpdoc = xapian.Document()
        termgenerator.set_document(xpdoc)

        try:
            # Index fields with prefixes.
            for prefix, fields in self.field_prefix.items():
                for field in fields:
                    try:
                        termgenerator.index_text(doc[field], 1, prefix)
                    except KeyError:
                        continue

            # Index fields without prefixes for general search.
            for field in self.indexingField:
                try:
                    termgenerator.index_text(doc[field])
                    logger.debug('indexed: %s: %s', field, doc[field])
                except KeyError:
                    # If the key can't be found, just ignore it
                    continue
                termgenerator.increase_termpos()

            for i, (field, isnumber) in enumerate(self.sortingField.items()):
                if isnumber:
                    value = xapian.sortable_serialise(float(doc[field]))
                else:
                    f = doc[field]
                    if isinstance(f, unicode):
                        value = f.encode('utf-8')
                    else:
                        value = str(f)
                xpdoc.add_value(i, value)

            idfield = config.get('config', 'id')
            ver = self.get_version()
            if self.storingField is None:
                data = doc
            else:
                data = {k: doc[k] for k in self.storingField}
                if ver >= 1.09:
                    data[idfield] = doc[idfield]
                else:
                    data['_id'] = doc[idfield]
            xpdoc.set_data(util.tojson(data))
            logger.debug('data is: %s', data)

            idterm = u"Q" + unicode(doc[idfield])
            if len(idterm) > 240:
                raise AWIPRequestInvalid('value for id field "%s" too long; please redesign your document structure' % idfield)
            xpdoc.add_boolean_term(idterm)
            self.db.replace_document(idterm, xpdoc)

        except KeyError, e:
            raise AWIPRequestInvalid('invalid document: missing key "%s"' % e.args[0])
        except (TypeError, ValueError), e:
            raise AWIPRequestInvalid('invalid document: wrong value "%r"' % e)

    def delete_document(self, id):
        return self.db.delete_document(id)

    def close(self):
        logger.info('db %s closed (mode=%s)', self.name, self.mode)
        del _open_dbs[(self.name, self.mode)]
        if self.mode == 'RDWR':
            self.db.commit()
        self.db.close()

    def commit(self):
        self.db.commit()
