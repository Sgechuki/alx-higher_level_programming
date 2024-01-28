#!/usr/bin/python3
# takes your GitHub credentials
import sys
import requests
from requests.auth import HTTPBasicAuth


url = "https://api.github.com/user"
r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
response = r.json()
print(response.get("id"))
