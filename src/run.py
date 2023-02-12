import os, subprocess
from src import build

def run(args):
    if len(args) == 0:
        build(args)
        __run("debug")
    elif len(args) == 1:
        if args[0] == "--release" or args[0] == "-r":
            build(args)
            __run("release")
        elif args[0] == "--debug" or args[0] == "-d":
            build(args)
            __run("debug")
        else:
            print("Invalid 'build' command")
    else:
        print("Invalid 'build' command")

def __run(build_type):
    os.chdir("bin")
    os.chdir(build_type)
    for f in os.listdir(os.getcwd()):
        if os.name == "nt":
            os.system("{}.exe".format(f))
        else:
            os.system("./{}".format(f))
    os.chdir("..")
    os.chdir("..")
