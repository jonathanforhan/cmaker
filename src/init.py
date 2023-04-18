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
    for fd in os.listdir(os.getcwd()):
        if fd == "CMakeLists.txt":
            sys.exit("CMakeLists.txt already present")
        if fd == "cmaker-config.json":
            sys.exit("cmaker-config.json already present")

    for fd in os.listdir(head):
        if fd == "CMakeLists.txt" or fd == "cmaker-config.json":
            contents = util.read_file(head, fd)        # read from template
            contents = contents.replace("--CMAKER_REPLACE", replace)
            util.write_file(os.getcwd(), fd, contents) # write to cwd
