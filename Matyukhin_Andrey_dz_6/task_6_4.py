with open('users.csv', 'r', encoding="utf-8") as f_users, open('hobby.csv', 'r', encoding="utf-8") as f_hobby, open(
        'users_hobby.txt', 'w', encoding="utf-8") as f_us_hob:
    print(f_hobby.readline().strip())
    line_users = f_users.readline().strip()
    line_hobby = f_hobby.readline().strip()
    while line_users:
        if line_hobby:
            f_us_hob.writelines(f'{str(line_users)}: {line_hobby}\n')
        else:
            f_us_hob.writelines(f'{str(line_users)}: {None} \n')
        line_users = f_users.readline().strip()
        line_hobby = f_hobby.readline().strip()
        if line_hobby and not line_users:
            exit(1)

