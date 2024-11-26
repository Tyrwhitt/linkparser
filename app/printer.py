import json
import logging
import urllib.parse

class printer():
    def __init__(self, outputType):
        if outputType == "json":
            self.print = self._outputJson
        elif outputType == "stdout":
            self.print = self._outputStdout
        else:
            raise Exception(f"Unknown output format {outputType}")
        self.logger = logging.getLogger("printer")

    def _outputJson(self, links):
        self.logger.debug(f"Printing in JSON format {links}")
        print(json.dumps(links, indent = 4), flush=True)

    def _outputStdout(self, links):
        self.logger.debug(f"Printing in stdout format {links}")
        for url, linkList in links.items():
            for link in linkList:
                print(urllib.parse.urljoin(url, link), flush=True)