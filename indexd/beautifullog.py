import sys
import time
import logging

def enable_pretty_logging(level=logging.DEBUG):
  logger = logging.getLogger()
  h = logging.StreamHandler()
  formatter = logging.Formatter(u'%(asctime)s:%(levelname)-7s:%(name)-12s:%(message)s')
  try:
    import curses
    color = False
    curses.setupterm()
    if curses.tigetnum(u"colors") > 0:
      color = True
    formatter = TornadoLogFormatter(color=color)
  except:
    import traceback
    traceback.print_exc()
  finally:
    h.setLevel(level)
    h.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(h)

class TornadoLogFormatter(logging.Formatter):
  def __init__(self, color, *args, **kwargs):
    super(self.__class__, self).__init__(self, *args, **kwargs)
    self._color = color
    if color:
      import curses
      curses.setupterm()
      if sys.hexversion < 50463728:
        fg_color = unicode(curses.tigetstr(u"setaf") or
                   curses.tigetstr(u"setf") or u"", u"ascii")
      else:
        fg_color = curses.tigetstr(u"setaf") or curses.tigetstr(u"setf") or ""
      self._colors = {
        logging.DEBUG: unicode(curses.tparm(fg_color, 4), # Blue
                     u"ascii"),
        logging.INFO: unicode(curses.tparm(fg_color, 2), # Green
                    u"ascii"),
        logging.WARNING: unicode(curses.tparm(fg_color, 3), # Yellow
                     u"ascii"),
        logging.ERROR: unicode(curses.tparm(fg_color, 1), # Red
                     u"ascii"),
      }
      self._normal = unicode(curses.tigetstr(u"sgr0"), u"ascii")

  def format(self, record):
    try:
      record.message = record.getMessage()
    except Exception, e:
      record.message = u"Bad message (%r): %r" % (e, record.__dict__)
    record.asctime = time.strftime(
      u"%m-%d %H:%M:%S", self.converter(record.created))
    record.asctime += u'.%03d' % ((record.created % 1) * 1000)
    prefix = u'[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]' % \
      record.__dict__
    if self._color:
      prefix = (self._colors.get(record.levelno, self._normal) +
            prefix + self._normal)
    formatted = prefix + u" " + record.message
    if record.exc_info:
      if not record.exc_text:
        record.exc_text = self.formatException(record.exc_info)
    if record.exc_text:
      formatted = formatted.rstrip() + u"\n" + record.exc_text
    return formatted.replace(u"\n", u"\n    ")

