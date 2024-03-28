#!/bin/bash
#sends a request to a URL and displays only the status code of the response
curl -s $1 -L -w "%{http_code}" -o /dev/null
