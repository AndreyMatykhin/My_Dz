from urllib.request import urlopen
import re

with urlopen('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs') as f:
    pattern = re.compile(r'(?P<remote_addr>^[\d.:\w]+).*\[(?P<request_datetime>.+)\].\"(?P<request_type>\w+).'
                         r'(?P<requested_resource>[\w/\s.]+)\".(?P<response_code>\d+).(?P<response_size>\d+).\"',
                         re.IGNORECASE)
    line = (f.readline()).decode(encoding="utf-8")
    while line:
        print(*map(lambda x: x.groupdict(), pattern.finditer(line)))
        line = (f.readline()).decode(encoding="utf-8")
