import os

def mkdir(path, fd):
    path = os.path.join(path, fd)
    os.mkdir(path)

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
