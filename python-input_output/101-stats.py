#!/usr/bin/python3
"""
Log parsing script that reads stdin and computes metrics.
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def print_stats():
    """
    Print accumulated statistics.
    """
    print(f"File size: {total_size}")
    for code in status_codes:
        if counts[code]:
            print(f"{code}: {counts[code]}")
    sys.stdout.flush()


def main():
    """
    Read stdin and compute metrics.
    """
    global total_size, line_count

    try:
        for line in sys.stdin:
            parts = line.split()

            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (IndexError, ValueError):
                continue

            total_size += size

            if status in counts:
                counts[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise

    print_stats()


if __name__ == "__main__":
    main()
