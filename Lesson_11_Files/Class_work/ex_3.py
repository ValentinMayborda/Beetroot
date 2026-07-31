def analyze_logs(filename):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1
    most_common = max(counts, key=counts.get)
    return most_common

print(analyze_logs('server.log'))