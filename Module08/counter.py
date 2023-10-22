from collections import Counter


def get_count_visits_from_ip(ips):
    ip_count = Counter(ips)
    return ip_count
    


def get_frequent_visit_from_ip(ips):
    ip_count = Counter(ips)
    ip_count_most_common = ip_count.most_common(1)
    return ip_count_most_common[0]


ips = [
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.252",
    "85.157.172.252",
    "85.157.172.251",
]


print(get_count_visits_from_ip(ips))
print(get_frequent_visit_from_ip(ips))