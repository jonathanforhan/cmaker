import os, sys

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmkr/templates/.cmakerignore/")

def make_dir(dir):
    cwd = os.getcwd()
    path = os.path.join(cwd, dir)
    os.mkdir(path)

# recursively copy template dir
# fw -> write
# fr -> read
# fd -> file descriptor
def write_files(path, replace):
    for fd in os.listdir(path):
        if fd == ".cmakerignore":
            continue
        fd_path = os.path.join(path, fd)
        if os.path.isfile(fd_path):
            fr = open(fd_path, "r")
            contents = fr.read()
            if replace:
                contents = contents.replace("--CMAKER_REPLACE", replace)
            fr.close()
            fw = open(fd, "w")
            fw.write(contents)
            fw.close()
        else:
            make_dir(fd)
            os.chdir(fd)
            write_files(fd_path, "")
            os.chdir("..")

def init(project_name):
    make_dir(project_name)
    os.chdir(project_name)
    write_files(template_path, project_name)
