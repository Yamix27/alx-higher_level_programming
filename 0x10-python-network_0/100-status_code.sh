#!/bin/bash
# This script sends a request to a URL and displays only the status code of the response
curl -sI "$1" | grep -i "HTTP" | awk '{print $2}'
