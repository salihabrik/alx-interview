#!/usr/bin/python3
import sys

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def parse_log_line(line, total_size, status_counts):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = int(parts[-2])
        total_size += size
        if status_code in status_counts:
            status_counts[status_code] += 1
    except:
        pass
    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_counts = parse_log_line(line, total_size, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise
    print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
