#!/bin/bash
<<<<<<< HEAD
# Sends a request to a URL and displays the size of the response body in bytes

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Fetch the URL and display the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$url"
=======
# This program takes in a URL, sends a request to that URL, and displays the size of the body of the response.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
>>>>>>> f65f6746c8065a5d8f66fb8484f0a3858ecf237a
