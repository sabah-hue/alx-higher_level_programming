#!/bin/bash
#sends a JSON POST request to a URL
curl -sX POST $1 -L -H "Content-Type: application/json" -d @$2
