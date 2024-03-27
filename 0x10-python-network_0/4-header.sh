#!/bin/bash
#sends a GET request to the URL
curl -s GET $1 -L -H "X-School-User-Id: 98"
