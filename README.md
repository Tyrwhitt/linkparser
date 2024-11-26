# Linkparser
Simple tool for listing links in webpage.  
Usage from CLI:
```
usage: main.py [-h] [-o {stdout,json}] [-u URL]

List all links in a web page

options:
  -h, --help            show this help message and exit
  -o {stdout,json}, --output {stdout,json}
                        Output format, default stdout
  -u URL, --url URL     Target url
```
## Docker
Building locally
```
docker build -t linkparser:latest .
```
Running image
```
docker run --rm https://ghcr.io/tyrwhitt/linkparser:<tag> -o json -u <someurl>
```
Note: python app will wait for any signal in the end.

# Domain extract
Solutions and comments are in `domain-extract` -directory.