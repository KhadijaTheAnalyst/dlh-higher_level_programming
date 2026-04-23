#!/usr/bin/python3
import sys
argv = sys.argv

if __name__ == "__main__":
    total = 0

    for i in range(1, len(argv)):
        total += int(argv[i])

    print(total)
