#!/usr/bin/python3
import sys

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def parse_log_line(line, total_size, status_counts):
    try:
        _, _, _, _, _, status_code_str, file_size_str = line.split()
        status_code = int(status_code_str)
        file_size = int(file_size_str)

        total_size += file_size

        # Updating status code counts
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

    except ValueError or IndexError:
        # Skip the line if it doesn't match the expected format
        pass

    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {}

    try:
        for idx, line in enumerate(sys.stdin, start=1):
            total_size, status_counts = parse_log_line(line, total_size, status_counts)

            # Print statistics after every 10 lines
            if idx % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Print final statistics in case of keyboard interruption
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
