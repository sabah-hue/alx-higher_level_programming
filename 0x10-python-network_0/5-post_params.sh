#!/bin/bash
#sends a POST request to the passed URL
#email="test@gmail.com"
#subject="I will always be here for PLD"
curl -sX POST $1 -L -d "email=test@gmail.com&subject=I will always be here for PLD"
