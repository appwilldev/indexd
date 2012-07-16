# vim:fileencoding=utf-8:sw=4

import os
from ConfigParser import ConfigParser
import logging

import xapian

from exceptions import *

_open_dbs = {}
_dbpath = None
logger = logging.getLogger(__name__)

class CasedConfigParser(ConfigParser):
    def optionxform(self, option):
        return option

def set_dbdir(path):
    global _dbpath
    _dbpath = path

def get_db(name, mode):
    if name in _open_dbs:
        return _open_dbs[(name, mode)]
    else:
        try:
            db = XapianDB(name, mode)
        except xapian.DatabaseOpeningError, e:
            raise AWIPOperationError(str(e))
        _open_dbs[(name, mode)] = db
        return db

class XapianDB(object):
    queryparser = None
    config = None

    def __init__(self, name, mode):
        if _dbpath is None:
            raise AWIPServerError('database directory not set yet')
        self.name = name
        if mode == 'RDONLY':
            self.db = xapian.Database(os.path.join(_dbpath, name))
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
        logger.info('query parser for %s loaded.', self.name)

    def load_config(self):
        if self.config:
            return

        conf = self.config = CasedConfigParser()
        conf.readfp(open(os.path.join(_dbpath, self.name + '.ini')))
        logger.info('config file for %s loaded.', self.name)
