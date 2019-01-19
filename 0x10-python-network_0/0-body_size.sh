#!/bin/bash
# displays the size of the body of the response
curl -Is "$1" | grep -i Content-length | cut -d' ' -f2
