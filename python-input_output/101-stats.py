#!/usr/bin/python3
"""
Log parsing script that reads stdin and computes metrics.

Input format:
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Metrics printed every 10 lines, after CTRL+C, and at end of input:
  - Total file size (sum of all file sizes)
  - Count of each status code (ascending order)
"""

import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print(f"File size: {total_size}")
    # Print status codes in ascending order
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    line_count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Parse log line using regex
            # Look for: 3-digit status code, spaces, file size
            # (doesn't require file size to be at end - handles extra fields)
            match = re.search(r'(\d{3})\s+(\d+)', line)

            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))

                # Update cumulative metrics
                total_size += file_size
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print final stats on CTRL+C
        print()  # New line after ^C

    # Print final stats when input ends (EOF or CTRL+C)
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
