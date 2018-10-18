#!/usr/bin/python3
import sys
import signal
slit_line = []
file_size = 0
num_file = {}
ct = 0


def signal_handler(signal, frame):
    sys.stdout.write("File size: {}\n".format(file_size))
    for k, v in sorted(num_file.items()):
        sys.stdout.write("{}: {}\n".format(k, v))

for line in sys.stdin:
    split_line = line.split()
    file_size += int(split_line[-1])
    list_code = ["200", "301", "400", "401", "403", "404", "405", "500"]
    if split_line[-2] in num_file and split_line[-2] in list_code:
        num_file[split_line[-2]] += 1
        ct += 1
    elif split_line[-2] in list_code:
        num_file[split_line[-2]] = 1
        ct += 1
    if ct == 10:
        sys.stdout.write("File size: {}\n".format(file_size))
        for k, v in sorted(num_file.items()):
            sys.stdout.write("{}: {}\n".format(k, v))
        ct = 0
    signal.signal(signal.SIGINT, signal_handler)
