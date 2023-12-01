#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
        print("{}: {}".format(args, sys.argv[1]))
    else:
        print("{} arguments:".format(args))
        for i in range(1, args + 1):
            print("{}: {}".format(i, sys.argv[i]))
