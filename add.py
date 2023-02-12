import os, sys

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmkr/templates/.cmakerignore/")

def add_module(target):
    cwd = os.getcwd()
    rootdir = False
    for fd in os.listdir(cwd):
        if fd == "bin" or fd == "build":
            rootdir = True
            break
    if not rootdir:
        print("Must be in root directory")
        return
    if not os.path.exists("cmake"):
        os.mkdir("cmake")
        cmaker_inject("set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} \"${CMAKE_SOURCE_DIR}/cmake/\")", "SET")
    os.chdir("cmake")
    module_path = os.path.join(template_path, target)
    fr = open(module_path, "r")
    contents = fr.read()
    fw = open("{}".format(target), "w")
    fw.write(contents)
    fr.close()
    fw.close()
    os.chdir("..")

def cmaker_inject(injection, operation):
    cwd = os.getcwd()
    rootdir = False
    for fd in os.listdir(cwd):
        if fd == "src":
            rootdir = True
            break
    if not rootdir:
        print("Must be in root directory")
        return
    fr = open("CMakeLists.txt", "r")
    contents = fr.read()
    if contents.find(injection) != -1:
        return
    contents = contents.replace("CMAKER_{}".format(operation), "CMAKER_{}\n{}".format(operation, injection))
    fr.close()
    fw = open("CMakeLists.txt", "w")
    fw.write(contents)
    fw.close()


def add_class(class_name):
    cwd = os.getcwd()
    for fd in os.listdir(cwd):
        if fd == "src" and os.path.isdir(fd):
            os.chdir(fd)
    # header
    hpp_path = os.path.join(template_path, "class.hpp")
    fr = open(hpp_path, "r")
    contents = fr.read()
    fr.close()
    contents = contents.replace("--CMAKER_REPLACE", class_name)
    fw = open("{}.hpp".format(class_name), "w")
    fw.write(contents)
    fw.close()
    # cpp
    cpp_path = os.path.join(template_path, "class.cpp")
    fr = open(cpp_path, "r")
    contents = fr.read()
    fr.close()
    contents = contents.replace("--CMAKER_REPLACE", class_name)
    fw = open("{}.cpp".format(class_name), "w")
    fw.write(contents)
    fw.close()

def add_cmakelists():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file == "CMakeLists.txt":
            print("File already exists")
            return
    f = open("CMakeLists.txt", "x")
    f.close()

def add_sdl2():
    cmaker_inject("find_package(SDL2 REQUIRED)", "FIND")
    add_module("FindSDL2.docs")
    add_module("FindSDL2.cmake")

def add_sdl2_image():
    cmaker_inject("find_package(SDL2_image REQUIRED)", "FIND")
    add_module("FindSDL2_image.docs")
    add_module("FindSDL2_image.cmake")

