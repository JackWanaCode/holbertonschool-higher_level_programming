#!/usr/bin/python3
#http://0.0.0.0:5000/post_email hr@holbertonschool.com
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
