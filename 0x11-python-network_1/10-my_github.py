#!/usr/bin/python3
"""
takes your GitHub credentials
uses the GitHub API to display your id
must use Basic Authentication
first argument will be your username
second argument will be your password
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    response = r.json()
    print(response.get("id"))
