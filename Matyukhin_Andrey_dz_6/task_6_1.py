from urllib.request import urlopen

pars_list = []
with urlopen('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs') as f:
    line = (f.readline()).decode(encoding="utf-8")
    while line:
        pars_list.append((line.split(' -')[0], line.split('"')[1].split()[0], line.split('"')[1].split()[1]))
        line = (f.readline()).decode(encoding="utf-8")
print(pars_list)
