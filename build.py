import os

def build_debug():
    if not os.path.exists("bin/debug"):
        os.makedirs("bin/debug")
    os.chdir("build")
    os.system("cmake -DCMAKE_BUILD_TYPE=Debug -DOUTPUT:STRING=debug .. && make")
    os.chdir("..")

def build_release():
    if not os.path.exists("bin/release"):
        os.makedirs("bin/release")
    os.chdir("build")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DOUTPUT:STRING=release .. && make")
    os.chdir("..")

def run(output):
    os.chdir("bin")
    os.chdir(output)
    file = os.listdir(".")
    for f in file:
        os.system("./{}".format(f))
    os.chdir("../..")

def clean():
    os.chdir("build")
    os.system("rm -rdf *")
    os.chdir("..")

def clean_all():
    os.chdir("build")
    os.system("rm -rdf *")
    os.chdir("..")
    os.chdir("bin")
    os.system("rm -rdf *")
    os.chdir("..")

