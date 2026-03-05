import json
from collections import Counter

def analyze_attacks(log_file):
    with open(log_file) as f:
        data = json.load(f)

    ips = [entry["ip"] for entry in data]
    attack_stats = Counter(ips)

    print("Top attacking IPs:")
    for ip, count in attack_stats.most_common(10):
        print(ip, count)