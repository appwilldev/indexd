#!/usr/bin/env python
# vim:fileencoding=utf-8:sw=4

import sys
import os
topdir = os.path.split(__file__)[0]
sys.path.append(topdir)

import signal
import argparse
import logging

import indexd.server
import indexd.constants
import indexd.xapiandb
import indexd.beautifullog

def on_sigterm(signo, frame):
    raise KeyboardInterrupt

def log_level(x):
    return int(logging.getLevelName(x.upper()))

def main():
    parser = argparse.ArgumentParser(description='An indexing daemon')
    parser.add_argument('-p', '--port', metavar='PORT', type=int, required=True,
                        help='the port number to listen')
    parser.add_argument('-l', '--logfile', metavar='FILE', default=None,
                        help='where to put the log; default is stderr')
    parser.add_argument('--fork', action='store_true',
                        help='fork to background; suppress logging to stderr')
    parser.add_argument('--mode', choices=indexd.constants.supported_modes,
                        nargs='*',
                        help='the mode(s) to run')
    parser.add_argument('--db', default=None,
                        help='index db directory')

    parser.add_argument('--loglevel', metavar='LEVEL', default=logging.INFO,
                        type=log_level,
                        help='logging level, default is INFO')
    parser.add_argument('--dict', metavar='FILE', default=None,
                        help='SCWS dict file to use for word splitting')
    parser.add_argument('--rules', metavar='FILE', default=None,
                        help='SCWS rules file to use for word splitting')

    args = parser.parse_args()

    if args.fork and args.logfile is None:
        args.logfile = '/dev/null'

    if args.fork:
        if os.fork() > 0:
            sys.exit()

    if args.logfile:
        sys.stderr = open(args.logfile, 'a')

    indexd.beautifullog.enable_pretty_logging(args.loglevel)
    indexd.xapiandb.set_dbdir(args.db or '.')
    if args.dict:
        indexd.xapiandb.set_scws_data(args.dict, args.rules)

    server = indexd.server.IndexServer(('', args.port))

    try:
        signal.signal(signal.SIGTERM, on_sigterm)
        server.start()
    except KeyboardInterrupt:
        logging.info('stopping...')


if __name__ == '__main__':
    main()
