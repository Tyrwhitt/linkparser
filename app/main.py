#!/usr/bin/env python
import argparse
import logging
import os
import signal
import sys
from os.path import basename

from printer import printer
from linkparser import linkparser

def main(args):
    """
    Loop over input urls for request and print
    """
    p = printer(args.output)
    for url in args.url:
        p.print(linkparser.getlinks(url))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=basename(__file__),
        description="List all links in a web page"
    )
    parser.add_argument("-o", "--output", help="Output format, default stdout", choices=["stdout","json"], default="stdout")
    parser.add_argument("-u", "--url", help="Target url", action="append", default=[])
    args = parser.parse_args()

    logger = logging.getLogger("LinkParser")
    try:
        loglevel = logging.getLevelNamesMapping()[os.getenv("loglevel", "warn").upper()]
    except KeyError:
        loglevel = logging.WARN
    logging.basicConfig(level=loglevel, stream=sys.stderr)

    logger.debug(args)
    main(args)
    signal.pause()
