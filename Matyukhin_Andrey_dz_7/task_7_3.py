import os
from shutil import copyfile

root_dir = "my_project"
if not os.path.exists("my_project/templates"):
    os.mkdir("my_project/templates")
task_dir = os.path.join(os.getcwd(), "my_project/templates")
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.rsplit(".", maxsplit=1)[1].lower() == "html":
            if not os.path.exists(os.path.join(task_dir, os.path.split(root)[-1])):
                os.mkdir(os.path.join(task_dir, os.path.split(root)[-1]))
            if not os.path.exists(os.path.join(task_dir, os.path.split(root)[-1], file)):
                copyfile(os.path.join(root, file), os.path.join(task_dir, os.path.split(root)[-1], file))
