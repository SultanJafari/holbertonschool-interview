#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def print_stats(stats, total_file_size):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))


if __name__ == "__main__":
    total_file_size = 0
    stats = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue

            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
            except ValueError:
                continue

            if status_code not in stats:
                continue

            total_file_size += file_size
            stats[status_code] += 1
            line_count += 1

            if line_count == 10:
                print_stats(stats, total_file_size)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(stats, total_file_size)
        raise
