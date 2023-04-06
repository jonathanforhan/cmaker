import os, sys
from src import util

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmaker/templates/.cmaker")


def add(args, config):
    if len(args) == 0:
        sys.exit("Invalid 'add' command")
    if args[0] == 'class':
        if len(args) == 1:
            sys.exit("Class command requires class name")
        elif len(args) == 2:
            class_name = args[1]
            __add_class(class_name, config)
        elif len(args) == 3:
            class_name = args[1]
            path = args[2]
            __add_class(class_name, config, path)
    else:
        for arg in args:
            if arg == "cmakelists":
                __add_cmakelists()
            elif arg == "SDL2" or arg == "sdl2":
                __add_sdl2()
            elif arg == "SDL2_image" or arg == "sdl2_image":
                __add_sdl2_image()
            else:
                sys.exit("add {} is not supported".format(arg))


def __check_root():
    check = 0
    for f in os.listdir(os.getcwd()):
        if f == "bin" or f == "build":
            check += 1
        if check > 1:
            return
    sys.exit("Must be in root directory")


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


def __add_class(class_name, config, path="."):
    os.chdir(path)
    for f in os.listdir(os.getcwd()):
        if f == class_name + ".hpp" or f == class_name + ".cpp":
            print("Class already exists")
            return
        if f == class_name + ".hxx" or f == class_name + ".cxx":
            print("Class already exists")
            return
        if f == class_name + ".h" or f == class_name + ".c":
            print("Class already exists")
            return

    header = util.read_file(template_path, "class.cxx.header")
    header = header.replace("--CMAKER_REPLACE", class_name.capitalize())
    if not config["PROJECT"]["NAMESPACE"] == "":
        header = header.replace("--CMAKER_NAMESPACE", "\nnamespace " + config["PROJECT"]["NAMESPACE"] + " {\n")
        header = header.replace("--CMAKER_END_NAMESPACE", "\n} // namespace " + config["PROJECT"]["NAMESPACE"] + "\n")
    else:
        header = header.replace("--CMAKER_NAMESPACE", "")
        header = header.replace("--CMAKER_END_NAMESPACE", "")

    if config["PROJECT"]["INCLUDE-GUARDS"] == "pragma":
        header = header.replace("--CMAKER_INCLUDE_GUARD", "#pragma once")
        header = header.replace("--CMAKER_END_INCLUDE_GUARD", "")
    else:
        include_settings = config["PROJECT"]["INCLUDE-GUARDS"].split("-")
        include_guard = ""
        for setting in include_settings:
            if setting == "PROJECT":
                if not include_guard == "":
                    include_guard += "_"
                include_guard += config["NAME"].upper()
            if setting == "DIR":
                if not include_guard == "":
                    include_guard += "_"
                include_guard += os.getcwd().split("/")[-1].upper()
            if setting == "FILE":
                if not include_guard == "":
                    include_guard += "_"
                include_guard += (class_name + "_" + config["PROJECT"]["CPP"]["HEADER"]).upper()

        header = header.replace("--CMAKER_INCLUDE_GUARD", "#ifndef " + include_guard + "\n#define " + include_guard)
        header = header.replace("--CMAKER_END_INCLUDE_GUARD", "#endif // " + include_guard)

    util.write_file(os.getcwd(), "{}.{}".format(class_name, config["PROJECT"]["CPP"]["HEADER"].lower()), header)

    source = util.read_file(template_path, "class.cxx.source")
    source = source.replace("--CMAKER_REPLACE", class_name)
    source = source.replace("--CMAKER_EXTENSION", config["PROJECT"]["CPP"]["HEADER"].lower())
    if not config["PROJECT"]["NAMESPACE"] == "":
        source = source.replace("--CMAKER_NAMESPACE", "\nnamespace " + config["PROJECT"]["NAMESPACE"] + " {\n")
        source = source.replace("--CMAKER_END_NAMESPACE", "} // namespace " + config["PROJECT"]["NAMESPACE"] + "\n")
    else:
        source = source.replace("--CMAKER_NAMESPACE", "")
        source = source.replace("--CMAKER_END_NAMESPACE", "")
    util.write_file(os.getcwd(), "{}.{}".format(class_name, config["PROJECT"]["CPP"]["SOURCE"].lower()), source)


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
