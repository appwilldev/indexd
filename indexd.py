#!/usr/bin/env python
# vim:fileencoding=utf-8:sw=4

import sys
import os
topdir = os.path.split(__file__)[0]
sys.path.append(topdir)

import argparse
import logging

import indexd
import indexd.constants
import indexd.xapiandb
import indexd.beautifullog

def main():
    parser = argparse.ArgumentParser(description='An indexing daemon')
    parser.add_argument('-p', '--port', metavar='PORT', type=int, required=True,
                        help='the port number to listen')
    parser.add_argument('-l', '--logfile', metavar='FILE', default=None,
                        help='where to put the log; default is stderr')
    parser.add_argument('-d', '--fork', action='store_true',
                        help='fork to background; suppress logging to stderr')
    parser.add_argument('-m', '--mode', choices=indexd.constants.supported_modes,
                        type=lambda x: x.split(','),
                        help='the mode(s) to run')
    parser.add_argument('--db', default=None,
                        help='index db directory')

    args = parser.parse_args()

    if args.fork and args.logfile is None:
        args.logfile = '/dev/null'

    if args.fork:
        if os.fork() > 0:
            sys.exit()

    if args.logfile:
        sys.stderr = open(args.logfile, 'a')

    indexd.beautifullog.enable_pretty_logging(logging.DEBUG)
    indexd.xapiandb.set_dbdir(args.db or '.')
    server = indexd.IndexServer(('', args.port))

    try:
        server.start()
    except KeyboardInterrupt:
        logging.info('stopping...')


if __name__ == '__main__':
    main()
