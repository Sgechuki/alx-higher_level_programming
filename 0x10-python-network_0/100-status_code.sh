#!/bin/bash
# ends a request to a URL passed as an argument
# displays only the status code of the response
curl -so /dev/null -w '%{http_code}' "$1"
