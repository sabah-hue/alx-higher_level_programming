#!/bin/bash
#sends a POST request to the passed URL
curl -s $1 POST -L -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
