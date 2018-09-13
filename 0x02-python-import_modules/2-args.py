#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 0
    l = len(argv)
    if l == 1:
        print("0 arguments.")
    else:
        for ar in argv:
            if j == 0:
                if l == 2:
                    print("{} argument:".format(len(argv) - 1))
                else:
                    print("{} arguments:".format(len(argv) - 1))
            else:
                print("{}: {}".format(j, ar))
            j += 1
