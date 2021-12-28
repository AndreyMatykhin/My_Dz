import yaml
import os


def create_config(str):
    for dir_name in str:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            if str[dir_name]:
                os.chdir(dir_name)
                for d in str[dir_name]:
                    if type(d) is dict:
                        create_config(d)
                    else:
                        f = open(d, "w")
                        f.close()
                os.chdir(os.pardir)


with open("config.yaml") as fl:
    config_dict = yaml.load(fl, Loader=yaml.FullLoader)
create_config(config_dict)
