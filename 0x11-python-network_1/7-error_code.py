#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    sc = r.status_code
    if sc >= 400:
        print("Error code: {}".format(sc))
    else:
        print(r.text)
