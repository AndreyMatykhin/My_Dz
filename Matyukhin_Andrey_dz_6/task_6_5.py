import sys
# python task_6_5.py users.csv hobby.csv users_hobby.txt
with open(sys.argv[1], 'r', encoding="utf-8") as f_users, open(sys.argv[2], 'r', encoding="utf-8") as f_hobby, open(
        sys.argv[3], 'w', encoding="utf-8") as f_us_hob:
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
            print("code = ", 1)
