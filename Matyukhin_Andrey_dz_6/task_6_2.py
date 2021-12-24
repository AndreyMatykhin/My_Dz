from urllib.request import urlopen

ip_addresses = {}
with urlopen('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs') as f:
    line = (f.readline()).decode(encoding="utf-8")
    while line:
        if line.split(' -')[0] in ip_addresses:
            ip_addresses[line.split(' -')[0]] += 1
        else:
            ip_addresses[line.split(' -')[0]] = 1
        line = (f.readline()).decode(encoding="utf-8")
ip_count = sorted(ip_addresses.items(), key=lambda x: x[1], reverse=True)
print(*("IP адрес {} отправил {} запросов. Возможно это спамер.\n".format(key, val) for key, val in
        [ip for ip in ip_count if ip[1] == ip_count[0][1]]))
