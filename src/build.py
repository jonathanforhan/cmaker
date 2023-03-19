import os, sys

def build(args):
    if len(args) == 0:
        __build("debug")
    elif len(args) == 1:
        if args[0] == "--release" or args[0] == "-r":
            __build("release")
        elif args[0] == "--debug" or args[0] == "-d":
            __build("debug")
        else:
            print("Invalid 'build' command")
    else:
        print("Invalid 'build' command")

def __build_check(build):
    _build = False # check for build and bin dir
    _bin = False   #
    for f in os.listdir(os.getcwd()):
        if f == "build":
            _build = True
        if f == "bin":
            _bin = True
    if not _build:
        print("Build command requires build directory")
        sys.exit(1)
    if not _bin:
        print("Build command requires bin directory")
        sys.exit(1)
    if not os.path.exists("bin/{}".format(build)):
        os.makedirs("bin/{}".format(build))


def __build(build):
    __build_check(build)
    os.chdir("build")
    os.system("cmake -G Ninja -DCMAKE_BUILD_TYPE={} .. && ninja".format(build.capitalize(), build))
    os.chdir("..")
