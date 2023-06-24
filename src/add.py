import os, sys
from . import util

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmaker/templates/.cmaker")


def __gen_include_guard(header, settings, project, name, ext):
    settings = settings.split("-")
    include_guard = ""

    for setting in settings:
        if setting == "PROJECT":
            if include_guard != "": include_guard += "_"
            include_guard += project.upper()
        elif setting == "PATH":
            cwd = os.getcwd()
            local = []
            while not util.is_root():
                dir = os.getcwd().replace("\\", "/")
                local.append(dir.split('/')[-1])
                os.chdir("..")
            os.chdir(cwd)
            for fd in reversed(local):
                if include_guard != "": include_guard += "_"
                include_guard += fd.upper()
        elif setting == "FILE":
            if include_guard != "": include_guard += "_"
            include_guard += (name + "_" + ext).upper()

    include_guard = include_guard.replace("-", "_")
    define = f"#ifndef {include_guard}\n#define {include_guard}"
    header = header.replace("--CMAKER_INCLUDE_GUARD", define)
    endif =  f"#endif // {include_guard}"
    header = header.replace("--CMAKER_END_INCLUDE_GUARD", endif)
    return header


def __verify_unique(class_name):
    for fd in os.listdir(os.getcwd()):
        if (fd == f"{class_name}.hpp" or fd == f"{class_name}.cpp"
                or fd == f"{class_name}.hxx" or fd == f"{class_name}.cxx"
                or fd == f"{class_name}.cc"
                or fd == f"{class_name}.h" or fd == f"{class_name}.c"):
            sys.exit("Class already exists")


def __cxx_class(config, path, class_name):
    try:    os.chdir(path)
    except: sys.exit("Invalid path argument")

    __verify_unique(class_name)

    """ Initializing """
    project = config["NAME"]
    header_ext = config["PROJECT"]["CPP"]["HEADER"]
    source_ext = config["PROJECT"]["CPP"]["SOURCE"]
    namespace = config["PROJECT"]["NAMESPACE"]
    include_guards = config["PROJECT"]["INCLUDE-GUARDS"]

    """ Header Creation """
    header = util.read_file(template_path, "class.cxx.header")

    class_list = class_name.replace("-", "_").split("_")
    class_list_len = len(class_list)
    if class_list_len > 1 and not class_name[0].isupper(): # avoid messing up PascalCase
        for i in range(class_list_len):
            class_list[i] = class_list[i].capitalize()

    header = header.replace("--CMAKER_REPLACE", "".join(class_list))
    if namespace != "":
        header = header.replace("--CMAKER_NAMESPACE", "\nnamespace " + namespace + " {\n")
        header = header.replace("--CMAKER_END_NAMESPACE", "\n} // namespace " + namespace + "\n")
    else:
        header = header.replace("--CMAKER_NAMESPACE", "")
        header = header.replace("--CMAKER_END_NAMESPACE", "")

    if include_guards == "pragma":
        header = header.replace("--CMAKER_INCLUDE_GUARD", "#pragma once")
        header = header.replace("--CMAKER_END_INCLUDE_GUARD", "")
    else:
        header = __gen_include_guard(header, include_guards, project, class_name, header_ext)

    util.write_file(os.getcwd(), "{}.{}".format(class_name, header_ext.lower()), header)

    """ Source Creation """
    source = util.read_file(template_path, "class.cxx.source")
    source = source.replace("--CMAKER_REPLACE", class_name)
    source = source.replace("--CMAKER_EXTENSION", header_ext.lower())
    if not namespace == "":
        source = source.replace("--CMAKER_NAMESPACE", "\nnamespace " + namespace + " {\n")
        source = source.replace("--CMAKER_END_NAMESPACE", "} // namespace " + namespace + "\n")
    else:
        source = source.replace("--CMAKER_NAMESPACE", "")
        source = source.replace("--CMAKER_END_NAMESPACE", "")
    util.write_file(os.getcwd(), "{}.{}".format(class_name, source_ext.lower()), source)


def __c_class(config, path, class_name):
    try:    os.chdir(path)
    except: sys.exit("Invalid path argument")

    __verify_unique(class_name)

    """ Initializing """
    project = config["NAME"]
    header_ext = config["PROJECT"]["C"]["HEADER"]
    source_ext = config["PROJECT"]["C"]["SOURCE"]
    include_guards = config["PROJECT"]["INCLUDE-GUARDS"]

    """ Header Creation """
    header = util.read_file(template_path, "class.c.header")
    header = __gen_include_guard(header, include_guards, project, class_name, header_ext)

    util.write_file(os.getcwd(), "{}.{}".format(class_name, header_ext.lower()), header)

    """ Source Creation """
    source = util.read_file(template_path, "class.c.source")
    source = source.replace("--CMAKER_REPLACE", class_name)
    source = source.replace("--CMAKER_EXTENSION", header_ext.lower())

    util.write_file(os.getcwd(), "{}.{}".format(class_name, source_ext.lower()), source)


def add(args, config):
    if len(args) == 0:
        sys.exit("Invalid 'add' command")
    if len(args) > 3:
        sys.exit("Too many arguments")

    if args[0] == 'cxx' or args[0] == 'cpp':
        if len(args) < 2:
            sys.exit("'add cxx' command requires filename name")

        class_name = args[1].replace(" ", "_")
        path = "." if len(args) < 3 else args[2]

        __cxx_class(config, path, class_name)

    elif args[0] == 'c':
        if len(args) < 2:
            sys.exit("'add c' command requires filename name")

        class_name = args[1].replace(" ", "_")
        path = "." if len(args) < 3 else args[2]

        __c_class(config, path, class_name)

    else:
        sys.exit("add {} is not supported".format(args[0]))

    
