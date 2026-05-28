#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

After every 10 lines and/or a keyboard interruption (CTRL + C),
prints:
    - Total file size
    - Status code counts
"""

import sys


def print_stats(file_size, status_codes):
    """
    Print accumulated statistics.

    Args:
        file_size (int): Total accumulated file size.
        status_codes (dict): Dictionary of status code counts.
    """
    print("File size: {}".format(file_size))

    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":

    # Valid status codes
    valid_codes = ['200', '301', '400', '401',
                   '403', '404', '405', '500']

    # Metrics
    file_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:

            # Count processed lines
            line_count += 1

            # Split line into parts
            parts = line.split()

            # Extract file size
            try:
                file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Extract status code
            try:
                status = parts[-2]

                if status in valid_codes:

                    if status in status_codes:
                        status_codes[status] += 1
                    else:
                        status_codes[status] = 1

            except IndexError:
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    # Print final statistics
    print_stats(file_size, status_codes)
