#!/bin/bash
#Bash script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message You got me!
curl -sL -X PUT 0.0.0.0:5000/catch_me_3 -d "user_id=98" -H "Origin:School"
