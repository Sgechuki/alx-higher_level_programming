#!/bin/bash
# displays all HTTP methods the server will accept.
curl -si "$1"|grep -w Allow|cut -d ' ' -f2-
