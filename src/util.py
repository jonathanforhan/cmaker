import os

def mkdir(path, fd):
    path = os.path.join(path, fd)
    if not os.path.exists(path):
        os.makedirs(path)


def read_file(path, fd):
    path = os.path.join(path, fd)
    f = open(path, "r")
    contents = f.read()
    f.close()
    return contents


def write_file(path, fd, contents):
    path = os.path.join(path, fd)
    f = open(path, "w")
    f.write(contents)
    f.close()


def is_root():
    for f in os.listdir(os.getcwd()):
        if f == "cmaker-config.json":
            return True
    return False


def get_root():
    cwd = os.getcwd()
    while not is_root():
        os.chdir("..")
    root = os.getcwd()
    os.chdir(cwd)
    return root

