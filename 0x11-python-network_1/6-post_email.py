#!/usr/bin/python3
#http://0.0.0.0:5000/post_email hr@holbertonschool.com
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
