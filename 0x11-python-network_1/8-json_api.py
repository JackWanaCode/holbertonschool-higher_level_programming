#!/usr/bin/python3
import requests
from sys import argv
if __name__ == "__main__":
   var = ""
   if len(argv) > 1:
      var = argv[1]
   r = requests.post('http://0.0.0.0:5000/search_user', data={'q': var})
   if (var == ""):
      print("No result")
   else:
      try:
         print("[{}] {}".format(r.json()['id'], r.json()['name']))
      except:
         print("Not a valid JSON")
