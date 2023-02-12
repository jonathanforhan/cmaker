import os, sys

def clean(args):
    if len(args) == 0:
        __clean()
    elif len(args) == 1 and (args[0] == "--all" or args[0] == "-a"):
        __clean_all()
    else:
        print("Invalid 'clean' command")
        sys.exit(1)

def __check_clean(bt):
    build = False
    bin = False
    for f in os.listdir(os.getcwd()):
        if f == "build":
            build = True
        if f == "bin":
            bin = True
    if not build:
        print("Build folder required for clean command")
        sys.exit(1)
    if bt == "all" and not bin:
        print("Bin folder required for clean all command")
        sys.exit(1)

def __clean():
    __check_clean("")
    os.chdir("build")
    if os.name == "nt":
        os.system("ri -recurse -force *")
    else:
        os.system("rm -rdf *")
        os.chdir("..")

def __clean_all():
    __check_clean("all")
    os.chdir("build")
    if os.name == "nt":
        os.system("ri -recurse -force *")
    else:
        os.system("rm -rdf *")
    os.chdir("..")
    os.chdir("bin")
    if os.name == "nt":
        os.system("ri -recurse -force *")
    else:
        os.system("rm -rdf *")
    os.chdir("..")
