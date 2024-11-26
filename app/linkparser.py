import re
import requests
import logging
import urllib.parse

class linkparser():
    @staticmethod
    def getlinks(url):
        logger = logging.getLogger("linkparser")
        # Get user provided url content
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            logger.warn(f"Failed to get {url} with exception\n{e}")
            return {}
        if r.ok:
            content = r.text.replace("\n", "")
            logger.debug(f"Page content dump: {content}")
        else:
            raise Exception(f"Failed to get url {url} with status {r.status_code}")

        # Search for <a> tags in response, expression should match all link tags, regardles extra attributes
        expression = "<a.*?>"
        res = re.findall(expression, content)
        # Find values of href attributes in link tags
        expression = "href\\s?=\\s?(.*?)[ >]"
        links = {} # Link dict, baseurl is the key and paths are values. Printer class handles formatting for output
        for link in res:
            m = re.search(expression, link)
            if m:
                parsed = urllib.parse.urlparse(m.group(1).strip("\"'")) # Remove quotes, if any
                if parsed.hostname:
                    baseurl = f"{parsed.scheme}://{parsed.hostname}"
                else:
                    baseurl = url
                try:
                    logger.debug(f"Adding {baseurl} {parsed.path}, raw result: {link}, match {m.group(1)}, parsed {parsed}")
                    links[baseurl].add(parsed.path.lstrip("/"))
                except KeyError:
                    links[baseurl] = {parsed.path.lstrip("/")}
        # Change set to list for JSON encoder
        final = {}
        for k, v in links.items():
            final[k] = list(v)
        logger.debug(f"Links from {url}: {final}")
        return final