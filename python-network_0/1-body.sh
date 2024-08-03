#!/bin/bash
#!/bin/bash
# This script takes in a URL, send request to that url and display size
# Usage: ./get_size.sh <URL>

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a request to the URL and display the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$url"

