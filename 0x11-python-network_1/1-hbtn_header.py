#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as resp:
        s = resp.info()
        print(s.get('X-Request-Id'))
