#!/usr/bin/python3
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    f = open(filename)
    f.close()
except FileNotFoundError:
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write("[]")

for a in argv:
    if a is not argv[0]:
        lis = list(load_from_json_file(filename)) + [a]
        save_to_json_file(lis, filename)
