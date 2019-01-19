#!/bin/bash
# displays sends a GET request to the URL, and displays the body of the response.
curl -d "email:hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
