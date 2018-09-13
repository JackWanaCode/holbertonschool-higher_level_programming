#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0; j = 0
    for ar in sys.argv:
        i += 1
    if i == 1:
        print("0 arguments.")
    else:
        for ar in sys.argv:
            if j == 0:
                print("{} argument:".format(i - 1))
            else:
                print("{}: {}".format(j, ar))
            j += 1
