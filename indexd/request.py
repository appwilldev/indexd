# vim:fileencoding=utf-8:sw=4

from exceptions import *

NoDefault = object()

class Request(object):
    def __init__(self, d):
        self._data = d

    def __getattr__(self, name):
        return self.get_field(name)

    def get_field(self, name, default=NoDefault):
        name = unicode(name, 'utf-8')
        try:
            return self._data[name]
        except KeyError:
            if default is NoDefault:
                raise AWIPRequestInvalid('Required "%s" field not found'% name)
            else:
                return default

    def get_type(self, name, type, default=NoDefault):
        val = self.get_field(name, default)
        if not isinstance(val, type):
            raise AWIPRequestInvalid('Field "%s" should be %s, but %s found' % (
                name, type.__name__, val.__class__.__name__))
        return val

    def get_string(self, name, default=NoDefault):
        return self.get_type(name, unicode, default)

    def get_bool(self, name, default=NoDefault):
        return self.get_type(name, bool, default)

    def get_int(self, name, default=NoDefault):
        return self.get_type(name, int, default)

    def get_float(self, name, default=NoDefault):
        return self.get_type(name, float, default)

    def get_dict(self, name, default=NoDefault):
        return self.get_type(name, dict, default)

    def get_list(self, name, default=NoDefault):
        return self.get_type(name, list, default)
