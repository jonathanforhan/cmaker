import os, sys
from src import util

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmaker/templates/.cmaker")

def add(args):
    if len(args) == 0:
        print("Invalid 'add' command")
        sys.exit(1)
    if args[0] == 'class':
        if len(args) == 1:
            print("Class command requires class name")
            sys.exit(1)
        for class_name in args[1:]:
            __add_class(class_name)
    else:
        for arg in args:
            if arg == "cmakelists":
                __add_cmakelists()
            elif arg == "SDL2" or arg == "sdl2":
                __add_sdl2()
            elif arg == "SDL2_image" or arg == "sdl2_image":
                __add_sdl2_image()
            else:
                print("add {} is not supported".format(arg))
                sys.exit(1)

def __check_root():
    check = 0
    for f in os.listdir(os.getcwd()):
        if f == "bin" or f == "build":
            check += 1
        if check > 1:
            return
    print("Must be in root directory")
    sys.exit(1)

def __inject(injection, opt):
    __check_root()
    contents = util.read_file(os.getcwd(), "CMakeLists.txt")
    if contents.find(injection) != -1:
        return
    contents = contents.replace("CMAKER_{}".format(opt), "CMAKER_{}\n{}".format(opt, injection))
    util.write_file(os.getcwd(), "CMakeLists.txt", contents)

def __add_module(mod):
    __check_root()
    if not os.path.exists("cmake"):
        cmake_module_path = "set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} \"${CMAKE_SOURCE_DIR}/cmake/\")"
        util.mkdir(os.getcwd(), "cmake")
        __inject(cmake_module_path, "SET")
    os.chdir("cmake")
    contents = util.read_file(template_path, mod)
    util.write_file(os.getcwd(), mod, contents)
    os.chdir("..")

def __add_class(class_name):
    # if in root cd src
    for f in os.listdir(os.getcwd()):
        if f == "src" and os.path.isdir(f):
            os.chdir(f)
            break
    for f in os.listdir(os.getcwd()):
        if f == class_name + ".hpp" or f == class_name + ".cpp":
            print("Class already exists")
            return
    hpp = util.read_file(template_path, "class.hpp")
    hpp = hpp.replace("--CMAKER_REPLACE", class_name)
    util.write_file(os.getcwd(), "{}.hpp".format(class_name), hpp)
    cpp = util.read_file(template_path, "class.cpp")
    cpp = cpp.replace("--CMAKER_REPLACE", class_name)
    util.write_file(os.getcwd(), "{}.cpp".format(class_name), cpp)

def __add_cmakelists():
    for f in os.listdir(os.getcwd()):
        if f == "CMakeLists.txt":
            print("File already exists")
            return
    f = open("CMakeLists.txt", "x")
    f.close()

def __add_sdl2():
    __inject("find_package(SDL2 REQUIRED)", "FIND")
    __add_module("FindSDL2.docs")
    __add_module("FindSDL2.cmake")


def __add_sdl2_image():
    __inject("find_package(SDL2_image REQUIRED)", "FIND")
    __add_module("FindSDL2_image.docs")
    __add_module("FindSDL2_image.cmake")
