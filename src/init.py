import os
import sys
from . import util


home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmaker/templates/")


def init():
    __create()


def __create():
    project_name = os.path.dirname(os.path.join(os.getcwd(), ".."))
    project_name = project_name.replace("\\", "/").split("/")[-1]
    
    template = "default"
    template_fd = os.path.join(template_path, template)

    if not os.path.exists(template_fd):
        sys.exit("{} is not found in template path".format(template))

    __file_copy(template_fd, project_name)


def __file_copy(head, replace):
    cmake_present = False
    cmaker_conf_present = False
    for fd in os.listdir(os.getcwd()):
        if fd == "CMakeLists.txt":
            while True:
                rep = input("A CMakeLists.txt is present in this directory, do you wish to replace it? [y/n] ")
                if rep.upper() == "Y":
                    break
                elif rep.upper() == "N":
                    cmake_present = True
                    break
        if fd == "cmaker-config.json":
            while True:
                rep = input("A cmaker-config.json is present in this directory, do you wish to replace it? [y/n] ")
                if rep.upper() == "Y":
                    break
                elif rep.upper() == "N":
                    cmaker_conf_present = True
                    break

    for fd in os.listdir(head):
        if fd == "CMakeLists.txt" and not cmake_present \
        or fd == "cmaker-config.json" and not cmaker_conf_present:
            contents = util.read_file(head, fd)        # read from template
            contents = contents.replace("--CMAKER_REPLACE", replace)
            util.write_file(os.getcwd(), fd, contents) # write to cwd
