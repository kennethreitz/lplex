#!/usr/bin/env python

"""
Logplex instrumentation.

Usage:
  lplex <message>... [--proc=<proc>] [--token=<token>]
  lplex -h | --help

Options:
  -h --help     Show this screen.
  --version     Show version.
"""


import os
import json
from datetime import datetime, timedelta

from logplex import Logplex
from docopt import docopt

LOG_TOKEN = os.environ.get('LOG_TOKEN')
LOGPLEX_URL = os.environ.get('LOGPLEX_URL')

def dispatch_cli(args):

    message = ' '.join(args.get('<message>', []))
    proc = args.get('--proc') or 'buildpack'
    token = args.get('--token', LOG_TOKEN)


    lp = Logplex(token=token, url=LOGPLEX_URL)
    lp.procid = proc
    lp.puts(message)


def main():
    arguments = docopt(__doc__, version='Logplex')
    try:
        dispatch_cli(arguments)
    except Exception:
        raise
        exit()


if __name__ == '__main__':
    main()
