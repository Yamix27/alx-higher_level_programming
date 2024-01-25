#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the body and displays the response body

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

url="$1"
json_file="$2"

# Check if the file is a valid JSON
if ! jq '.' "$json_file" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

curl -sX POST -H "Content-Type: application/json" -d @"$json_file" "$url"
