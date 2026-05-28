#!/usr/bin/python3
"""
Log parsing script that reads stdin and computes metrics.

Input format:
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>

Metrics printed every 10 lines, after CTRL+C, and at end of input:
  - Total file size (sum of all file sizes)
  - Count of each status code (ascending order)

"""


import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0


def print_stats():
    """
    This functions calculates the total file size and error codes
    """
    print(f"File size: {total_size}")
    for code in status_codes:
        if counts[code]:
            print(f"{code}: {counts[code]}")
    sys.stdout.flush()


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            status = int(parts[-2])
            size = int(parts[-1])
        except Exception:
            continue

        total_size += size
        if status in counts:
            counts[status] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
