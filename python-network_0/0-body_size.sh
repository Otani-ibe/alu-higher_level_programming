#!/bin/bash
# Sends a request to a URL and displays the size of the response body in bytes

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Fetch the URL and display the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$url"
