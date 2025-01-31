#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -isX OPTIONS "$1" | grep "Allow" | cut -d ":" -f 2 | xargs
