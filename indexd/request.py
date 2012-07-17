# vim:fileencoding=utf-8:sw=4

from exceptions import *

class Request(object):
    def __init__(self, d):
        self._data = d

    def __getattr__(self, name):
        return self.get_required_field(name)

    def get_required_field(self, name):
        name = unicode(name, 'utf-8')
        try:
            return self._data[name]
        except KeyError:
            raise AWIPRequestInvalid('Required "%s" field not found'% name)

    def get_type(self, name, type):
        val = self.__getattr__(name)
        if not isinstance(val, type):
            raise AWIPRequestInvalid('Field "%s" should be %s, but %s found' % (
                name, type.__name__, val.__class__.__name__))
        return val

    def get_string(self, name):
        return self.get_type(name, unicode)

    def get_bool(self, name):
        return self.get_type(name, bool)

    def get_int(self, name):
        return self.get_type(name, int)

    def get_float(self, name):
        return self.get_type(name, float)

    def get_dict(self, name):
        return self.get_type(name, dict)

    def get_list(self, name):
        return self.get_type(name, list)
