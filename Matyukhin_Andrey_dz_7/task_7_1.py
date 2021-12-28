import os


def create_folder(str):
    for dir_name in str:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            if str[dir_name]:
                os.chdir(dir_name)
                for d in str[dir_name]:
                    if type(d) is dict:
                        create_folder(d)
                os.chdir(os.pardir)


struct = {'my_project': [{'settings': None, 'mainapp': None, 'adminapp': None, 'authapp': None}]}
create_folder(struct)
