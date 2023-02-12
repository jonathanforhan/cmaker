def help():
    print("  Commands:\n\
\tnew:\n\
\t\tinitializes a new cmaker build enviornment, takes project name as argument\n\
\tbuild:\n\
\t\tdefault: builds debug cmake build and stores binary in 'project'/bin/debug/\n\
\t\t--debug | -d: explicitly state debug build preference\n\
\t\t--release | -r: builds release cmake build and stores binary in 'project'/bin/release/\n\
\trun:\n\
\t\tdefault: builds debug cmake build and then runs the executable\n\
\t\t--debug | -d: explicitly state debug build preference\n\
\t\t--release | -r: builds release cmake build and then runs the executable\n\
\tclean:\n\
\t\tdefault: removes all cmake build files in the build directory\n\
\t\t--all | -a: removes all cmake build files from build directory and removes debug and release directories\n\
\tadd:\n\
\t\tclass: adds .hpp and .cpp files, takes class name as argument\n\
\t\tcmakelists: adds a CMakeLists.txt if one is not already present\n\
\t\t{dependancies}: some dependancies like SDL2 and SDL2_image are supported with more coming\n\
\tscripts:\n\
\t\tany keyword stated in the scripts.cmaker file can be run with cmkr\n")

def version():
    print("CMaker version 1.0.0")
