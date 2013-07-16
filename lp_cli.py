#!/usr/bin/env python

"""
Logplex instrumentation.

Usage:
  lplex <message> [--proc=<proc>] [--token=<token>]
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

def dispatch_cli(args):

    message = args.get('<proc>')
    proc = args.get('<proc>') or 'buildpack'
    token = args.get('<token>') or LOG_TOKEN

    lp = Logplex(token=token)
    lp.procid = proc

    lp.puts(message)


def main():
    arguments = docopt(__doc__, version='Logplex')
    try:
        dispatch_cli(arguments)
    except Exception:
        exit()


if __name__ == '__main__':
    main()
