import os
import sys
from src import util

def build(args, config):
    if len(args) == 0:
        __build("debug", config)
    elif len(args) == 1:
        if args[0] == "--release" or args[0] == "-r":
            __build("release", config)
        elif args[0] == "--debug" or args[0] == "-d":
            __build("debug", config)
        else:
            sys.exit("Invalid 'build' command")
    else:
        sys.exit("Invalid 'build' command")


def __build(build, config):
    make = config["BUILD"]["MAKE"]

    export_compile_commands = "-DCMAKE_EXPORT_COMPILE_COMMANDS="
    if config["BUILD"]["EXPORT-COMPILE-COMMANDS"]:
        export_compile_commands += "1"
    else: export_compile_commands += "0"

    verbose_makefile = "-DCMAKE_VERBOSE_MAKEFILE="
    if config["BUILD"]["VERBOSE-MAKEFILE"]:
        verbose_makefile += "1"
    else: verbose_makefile += "0"

    build_dir = config["BUILD"][build]["BUILD-DIR"]

    output_dir = os.path.join(os.getcwd(), config["BUILD"][build]["OUTPUT"])
    util.mkdir('/', output_dir)
    output = "-DCMAKE_RUNTIME_OUTPUT_DIRECTORY:FILEPATH='" + output_dir + "'"

    build_flags = config["BUILD"][build]["FLAGS"]
    build_flags = "-D" + " -D".join(build_flags)

    make_cmd = "ninja" if make == "Ninja" else "make"

    while not util.check_root():
        os.chdir("..")
    util.mkdir(os.getcwd(), build_dir)
    os.chdir(build_dir)
    
    command = "cmake -G '{}' {} {} {} {} ..".format(
        make,
        export_compile_commands,
        verbose_makefile,
        output,
        build_flags,
    )

    display = command.split(" ")
    make_len = len(make.split(" "))
    print(" ".join(display[:(2 + make_len)]))
    for item in display[(2 + make_len):-1]:
        print(item)

    os.system(command)
    os.system(make_cmd)
    # place compile_commands.json in project dir for clangd
    try:
        cwd = os.getcwd()
        while not util.check_root():
            os.chdir("..")
        root = os.getcwd()
        os.chdir(cwd)
        os.replace("./compile_commands.json", os.path.join(root, "compile_commands.json"))
    except:
        pass
