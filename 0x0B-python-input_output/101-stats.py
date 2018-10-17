#!/usr/bin/python3
import sys
slit_line = []
file_size = 0
num_file = {}
ct = 0

for line in sys.stdin:
    line = sys.stdin.readline()
    split_line = line.split()
    file_size += int(split_line[-1])
    if split_line[-2] in num_file:
        num_file[split_line[-2]] += 1
        ct += 1
    else:
        num_file[split_line[-2]] = 1
        ct += 1
    if ct == 10:
        sys.stdout.write("File size: {}\n".format(file_size))
        for k, v in sorted(num_file.items()):
            sys.stdout.write("{}: {}\n".format(k, v))
        ct = 0
