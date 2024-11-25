import argparse
import logging
import os
import sys

from printer import printer
from linkparser import linkparser

def main(args):
    links = {}
    for url in args.url:
        links.update(linkparser.getlinks(url))

    p = printer(args.output)
    p.print(links)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="LinkParser",
        description="List all links in a web page"
    )
    parser.add_argument("-o", "--output", choices=["stdout","json"], default="stdout")
    parser.add_argument("-u", "--url", action="append", default=[])
    args = parser.parse_args()

    logger = logging.getLogger("LinkParser")
    try:
        loglevel = logging.getLevelNamesMapping()[os.getenv("loglevel", "warn").upper()]
    except KeyError:
        loglevel = logging.WARN
    logging.basicConfig(level=loglevel, stream=sys.stderr)

    logger.debug(args)
    main(args)