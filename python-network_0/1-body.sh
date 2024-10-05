#!/bin/bash
<<<<<<< HEAD
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

=======
# sends GET request to given URL and displays body of response
curl -sLfG "$1"
>>>>>>> f65f6746c8065a5d8f66fb8484f0a3858ecf237a
