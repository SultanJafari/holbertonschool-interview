#!/usr/bin/python3
"""
Module 0-stats
A script that reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
"""

import sys


def print_statistics(total_file_size, status_counts):
    """Prints the accumulated total file size and status code counts."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    total_file_size = 0
    line_count = 0
    valid_statuses = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_counts = {code: 0 for code in valid_statuses}

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    file_size = int(parts[-1])
                    status_code = parts[-2]

                    total_file_size += file_size

                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except ValueError:
                    pass

            line_count += 1

            if line_count == 10:
                print_statistics(total_file_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)
        raise

    if line_count > 0:
        print_statistics(total_file_size, status_counts)


if __name__ == "__main__":
    main()
