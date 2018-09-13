#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    ret = 0
    for ar in sys.argv:
        if i != 0:
            ret += int(ar)
        i += 1
    print(ret)
