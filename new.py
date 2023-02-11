import os, sys

template_path = "/home/jon/.scripts/cmkr/templates/"

def make_dir(dir):
    cwd = os.getcwd()
    path = os.path.join(cwd, dir)
    os.mkdir(path)

def write_file(name, template, project_name):
    path = os.path.join(template_path, template)
    fr = open(path, "r")
    contents = fr.read()
    if project_name:
        contents = contents.replace("foobar", project_name)
    fr.close()
    fw = open(name, "w")
    fw.write(contents)
    fw.close()

def init(project_name):
    make_dir(project_name)
    os.chdir(project_name)
    write_file("CMakeLists.txt", "CMakeLists.txt", project_name)

    make_dir("bin")
    make_dir("build")
    make_dir("src")

    os.chdir("src")
    write_file("main.cpp", "main.cpp", "")
    write_file("CMakeLists.txt", "src_CMakeLists.txt", "")
    os.chdir("..")
