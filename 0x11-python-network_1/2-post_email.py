#!/usr/bin/python3
"""
Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    data_encoded = urllib.parse.urlencode(data)
    data_bytes = data_encoded.encode('utf8')
    with urllib.request.urlopen(sys.argv[1], data=data_bytes) as response:
        res = response.read()
        print(res.decode('utf-8'))
