#!/usr/bin/env bash
cat urls.txt | tr '/' ' ' | tr '.' ' ' | awk '{print tolower($(NF-1))"."tolower($NF)}' | sort | uniq
