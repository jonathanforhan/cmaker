def print_help():
    print("Commands:\n\
\tnew:\n\
\t\tinitializes a new cmake++ build enviornment, takes project name as argument\n\
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
\t\t--all | -a: removes all cmake build files from build directory and removes debug and release directories")
