#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    som = 0
    for i in range(1, len(sys.argv)):
        som += int(sys.argv[i])
    print("{}".format(som))
