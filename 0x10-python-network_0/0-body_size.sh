#!/bin/bash
#body size
curl -s "$1" | grep -i "Content-Length" | cut -d " " -f2
