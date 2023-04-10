import os
import sys
import subprocess
from src import util


def run(args, config):
    if len(args) == 0:
        __run("debug", config)
    elif len(args) == 1:
        if args[0] == "--release" or args[0] == "-r":
            __run("release", config)
        elif args[0] == "--debug" or args[0] == "-d":
            __run("debug", config)
        else:
            sys.exit("Invalid 'run' command")
    else:
        sys.exit("Invalid 'run' command")


def __run(build, config):
    os.chdir(util.get_root())
    output_dir = config["BUILD"][build]["OUTPUT"];
    try:
        for fd in os.listdir(output_dir):
            os.remove(os.path.join(os.getcwd(), output_dir, fd))
    except:
        pass
    out = subprocess.run(f"cmkr build --{build}", shell=True)
    try:
        exe = os.path.join(os.getcwd(), output_dir, os.listdir(output_dir)[0])
        exe = exe.replace("/./", "/") # redundant
        print(f"\033[95mExecuting: {exe}\033[0m")
        subprocess.call(exe)
    except:
        print("\033[31mCMAKER BUILD FAILED\033[0m")

