import os, sys
from src import util

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmaker/templates/")

def new(args):
    if len(args) == 1 or (len(args) == 3 and args[1] == "from"):
        __create(args, len(args))
    else:
        print("Invalid 'new' command")
        sys.exit(1)

def __create(args, len):
    project_name = args[0]
    template = "default"
    if len == 3:
        template = args[2]
    template_fd = os.path.join(template_path, template)
    if not os.path.exists(template_fd):
        print("{} is not found in template path".format(template))
        sys.exit(1)
    if os.path.exists(os.path.join(os.getcwd(), project_name)):
        print("{} already exists".format(project_name))
        sys.exit(1)
    util.mkdir(os.getcwd(), project_name)
    os.chdir(project_name)
    __recursive_file_copy(template_fd, project_name)

def __recursive_file_copy(head, replace):
    for fd in os.listdir(head):
        fd_path = os.path.join(head, fd)
        cwd = os.getcwd()
        # fd_path is path to the template fd
        # fd is just the handle that can be also created in cwd
        if os.path.isdir(fd_path):
            util.mkdir(cwd, fd)
            os.chdir(fd)
            __recursive_file_copy(fd_path, replace)
            os.chdir("..")
        else:
            contents = util.read_file(head, fd)        # read from template
            contents = contents.replace("--CMAKER_REPLACE", replace)
            util.write_file(os.getcwd(), fd, contents) # write to cwd
