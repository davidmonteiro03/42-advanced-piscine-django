#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

curl -Lo /dev/null -sw '%{url_effective}\n' "$1"
