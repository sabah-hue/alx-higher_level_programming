#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    args_len = len(args) - 1
    if args_len == 0:
        print("0 arguments.")
    elif args_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_len))
    for i in range(1:args_len + 1):
        print("{}: {}".format(i, args[i + 1]))
