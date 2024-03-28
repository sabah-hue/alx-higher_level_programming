#!/bin/bash
#sends a JSON POST request to a URL
curl -sX $1 POST -L -H "Content-Type: application/json" -d @$2
