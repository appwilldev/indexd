# vim:fileencoding=utf-8:sw=4

import os
import io
import re
import logging
import ConfigParser

import xapian
import scws

import util
from exceptions import *

_open_dbs = {}
_dbpath = None
logger = logging.getLogger(__name__)

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
        return _open_dbs[(name, mode)]
    else:
        try:
            db = XapianDB(name, mode)
        except xapian.DatabaseOpeningError, e:
            raise AWIPOperationError(str(e))
        _open_dbs[(name, mode)] = db
        return db

def _parse_indexing_fields(val):
        return [x.strip() for x in val.split(',')]

def _validate_dbname(name):
    if not re.match(r'\w+$', name):
        raise AWIPRequestInvalid('inproper index database name')

def _config_file_path(name):
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

        fields = _parse_indexing_fields(conf.get('config', 'indexing'))

        for k, v in conf.items('field_prefix'):
            conf.get('prefix_name', k)
            assert v in fields

    except (ConfigParser.Error, TypeError, AssertionError), e:
        raise AWIPRequestInvalid('Invalid config data: %r' % e)

def _extendWithPrefix(l, words, prefix=''):
    if len(words) >= 3 and words[1] == ':':
        l.extend(['%s%s:%s' % (prefix, words[0], x) for x in words[2:]])
    else:
        l.extend([prefix + x for x in words])

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

    def query(self, qs, offset, pagesize):
        self.load_queryparser()
        qs = self.prepare_query(qs)
        query = self.queryparser.parse_query(qs)
        enquire = xapian.Enquire(self.db)
        enquire.set_query(query)
        return enquire.get_mset(offset, pagesize)

    def load_queryparser(self):
        if self.queryparser:
            return

        self.load_config()
        config = self.config

        self.queryparser = queryparser = xapian.QueryParser()
        lang = config.get('config', 'lang')
        if lang.lower() in ('zh', 'chinese'):
            # use English stemmer for Chinese
            queryparser.set_stemmer(xapian.Stem('en'))
        else:
            queryparser.set_stemmer(xapian.Stem(lang))
        queryparser.set_stemming_strategy(queryparser.STEM_SOME)
        for prefix, name in config.items('prefix_name'):
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
            try:
                last_is_op = ret[-1] in ('AND', 'OR', 'NOT')
            except IndexError:
                last_is_op = False
            if len(words) == 1:
                ret.append(words[0])
            elif len(words) >= 3 and words[1] == ':':
                l = []
                if last_is_op:
                    l.append('(')
                _extendWithPrefix(l, words)
                if last_is_op:
                    l.append(')')
                ret.extend(l)
            elif len(words) >= 2 and words[0] == '-':
                l = []
                if last_is_op:
                    l.append('(')
                _extendWithPrefix(l, words[1:], prefix='-')
                if last_is_op:
                    l.append(')')
                ret.extend(l)
            else:
                if last_is_op:
                    ret.append('(')
                ret.extend(words)
                if last_is_op:
                    ret.append(')')
        ret = ' '.join(ret).decode('utf-8')
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

        conf = self.config = util.CasedConfigParser()
        conf.readfp(open(_config_file_path(self.name)))
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

        indexingTerm = _parse_indexing_fields(config.get('config', 'indexing'))

        xpdoc = xapian.Document()
        termgenerator.set_document(xpdoc)

        try:
            # Index fields with prefixes.
            for prefix, field in config.items('field_prefix'):
                termgenerator.index_text(doc[field], 1, prefix)

            # Index fields without prefixes for general search.
            for field in indexingTerm:
                try:
                    termgenerator.index_text(doc[field])
                except KeyError:
                    # If the key can't be found, just ignore it
                    continue
                termgenerator.increase_termpos()

            xpdoc.set_data(util.tojson(doc))

            idfield = config.get('config', 'id')
            idterm = u"Q" + unicode(doc[idfield])
            if len(idterm) > 240:
                raise AWIPRequestInvalid('value for id field "%s" too long; please redesign your document structure' % idfield)
            xpdoc.add_boolean_term(idterm)
            self.db.replace_document(idterm, xpdoc)

        except KeyError, e:
            raise AWIPRequestInvalid('invalid document: missing key "%s"' % e.args[0])

    def delete_document(self, id):
        return self.db.delete_document(id)

    def close(self):
        logger.info('db %s closed (mode=%s)', self.name, self.mode)
        del _open_dbs[(self.name, self.mode)]
        self.db.commit()
        self.db.close()

    def commit(self):
        self.db.commit()
