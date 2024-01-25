#!/bin/bash
# takes in a URL, sends a POST request
# displays the body of the response
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
