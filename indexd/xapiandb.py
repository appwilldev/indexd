# vim:fileencoding=utf-8:sw=4

import os
import logging

import xapian

import util
from exceptions import *

_open_dbs = {}
_dbpath = None
logger = logging.getLogger(__name__)

def set_dbdir(path):
    global _dbpath
    _dbpath = path

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

def _config_file_path(name):
    return os.path.join(_dbpath, name + '.ini')

def createdb(name, confdata):
    fn = _config_file_path(name)
    if os.path.exists(fn):
        raise AWIPRequestInvalid('Index database "%s" already exists' % name)

    #TODO: validate the config
    with open(fn, 'w') as f:
        f.write(confdata)

    get_db(name, 'RDWR')

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
        queryparser.set_stemmer(xapian.Stem(config.get('config', 'lang')))
        queryparser.set_stemming_strategy(queryparser.STEM_SOME)
        for prefix, name in config.items('prefix_name'):
            queryparser.add_prefix(name, prefix)
        queryparser.add_prefix('_id', 'Q')
        logger.info('query parser for %s loaded.', self.name)

    def load_termgenerator(self):
        if self.termgenerator:
            return

        self.load_config()
        self.termgenerator = xapian.TermGenerator()
        self.termgenerator.set_stemmer(xapian.Stem(self.config.get('config', 'lang')))
        logger.info('term generator for %s loaded.', self.name)

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


        indexingTerm = [x.strip() for x in config.get('config', 'indexing').split(',')]

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
