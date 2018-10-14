from help_func import run
from sys import argv

l = len(argv)
if l != 2:
    print("Usage: nqueens N")
    exit(1)
if type(int(argv[1])) is not int:
    print("N must be a number")
    exit(1)
elif int(argv[1]) < 4:
    print("N must be at least 4")

run(int(argv[1]))
