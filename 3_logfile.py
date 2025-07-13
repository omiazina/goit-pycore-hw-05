import sys
from collections import defaultdict

LOG_LEVELS = ("INFO", "ERROR", "DEBUG", "WARNING")


def parse_log_line(line):
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path):
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs, level):
    result = []
    for log in logs:
        if log["level"] == level.upper():
            result.append(log)
    return result


def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        level = log["level"]
        if level in LOG_LEVELS:
            counts[level] += 1
    return counts


def display_log_counts(counts):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level in LOG_LEVELS:
        print(f"{level:<16} | {counts.get(level, 0)}")


def display_log_details(logs, level):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python 3_logfile.py <logfile> [loglevel]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            display_log_details(filtered_logs, level)
        else:
            print(f"\nNo logs found for level: {level.upper()}")

if __name__ == "__main__":
    main()
