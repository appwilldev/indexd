# vim:fileencoding=utf-8:sw=4

import os

import xapian

from exceptions import *

_open_dbs = {}
_dbpath = None

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
    def __init__(self, name, mode):
        if _dbpath is None:
            raise AWIPServerError('database directory not set yet')
        if mode == 'RDONLY':
            self.db = xapian.Database(os.path.join(_dbpath, name))
        elif mode == 'RDWR':
            self.db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)
        else:
            raise AWIPServerError('unknown mode passed to %s' % self.__class__.__name__)

    def query(self, qs, offset, pagesize):
        #TODO: use correct stemmer and prefix
        queryparser = xapian.QueryParser()
        queryparser.set_stemmer(xapian.Stem("en"))
        queryparser.set_stemming_strategy(queryparser.STEM_SOME)
        queryparser.add_prefix("title", "S")
        queryparser.add_prefix("description", "XD")

        query = queryparser.parse_query(qs)
        enquire = xapian.Enquire(self.db)
        enquire.set_query(query)
        return enquire.get_mset(offset, pagesize)
