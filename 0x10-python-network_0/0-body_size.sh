#!/bin/bash
#body size
#curl -s "$1" | grep -i "Content-Length" | cut -d " " -f2
curl -s "$1" | wc -c
