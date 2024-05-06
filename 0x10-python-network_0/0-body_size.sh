#!/bin/bash
#Bash script that sends a request to URL, and displays the size of the body of the response
curl $1 | grep -b "content-Length" 
