import re


def email_parse(email):
    pattern = re.compile(r'(?P<username>^[\w.+-]+)@(?P<domain>[\w-]+[\w.-]+$)', re.IGNORECASE)
    try:
        if pattern.findall(email):
            print(*map(lambda x: x.groupdict(), pattern.finditer(email)))
        else:
            raise ValueError("ValueError: wrong email: " + email)
    except ValueError as e:
        print(e)


email_parse("someone@geekbrains.ru")
email_parse('someone@geek@brains.ru')
