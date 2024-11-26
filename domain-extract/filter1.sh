#!/usr/bin/env bash
cat urls.txt | sed -E 's/(.*[\.\/])?([^\.]+\.[^\.]+)\.?$/\2/' | tr "A-Z" "a-z" | sort | uniq
