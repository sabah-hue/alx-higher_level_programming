#!/bin/bash
#sends a POST request to the passed URL
e="test@gmail.com"
s="I will always be here for PLD"
curl -sX POST $1 -L -d "email=$e&subject=$s"
