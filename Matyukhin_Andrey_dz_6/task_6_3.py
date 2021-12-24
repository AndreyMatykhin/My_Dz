users_hobby = {}
with open('users.csv', 'r', encoding="utf-8") as f_users, open('hobby.csv', 'r', encoding="utf-8") as f_hobby:
    line_users = f_users.readline().strip()
    line_hobby = f_hobby.readline().strip()
    while line_users:
        if line_hobby:
            users_hobby[line_users] = line_hobby.split(",")
        else:
            users_hobby[line_users] = None
        line_users = f_users.readline().strip()
        line_hobby = f_hobby.readline().strip()
        if line_hobby and not line_users:
            exit(1)
print(users_hobby)
