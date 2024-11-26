#!/usr/bin/env bash
cat urls.txt | sed 's/\.$//' | tr '/' '.' | tr 'A-Z' 'a-z' | rev | cut -d '.' -f 1,2 | rev | sort | uniq
