import os, sys
from src import util

home_dir = os.path.expanduser("~")
template_path = os.path.join(home_dir, ".scripts/cmaker/templates/.cmaker")


def __gen_include_guard(header, settings, project, name, ext):
    settings = settings.split("-")
    include_guard = ""

    for setting in settings:
        if setting == "PROJECT":
            if not include_guard == "": include_guard += "_"
            include_guard += project.upper()
        elif setting == "PATH":
            cwd = os.getcwd()
            local = []
            while not util.is_root():
                local.append(os.getcwd().split('/')[-1])
                os.chdir("..")
            os.chdir(cwd)
            for fd in reversed(local):
                if not include_guard == "": include_guard += "_"
                include_guard += fd.upper()
        elif setting == "FILE":
            if not include_guard == "": include_guard += "_"
            include_guard += (name + "_" + ext).upper()

    define = "#ifndef " + include_guard + "\n#define " + include_guard
    header = header.replace("--CMAKER_INCLUDE_GUARD", define)
    endif =  "#endif // " + include_guard
    header = header.replace("--CMAKER_END_INCLUDE_GUARD", endif)
    return header


def __verify_unique(class_name):
    for fd in os.listdir(os.getcwd()):
        if (fd == class_name + ".hpp" or fd == class_name + ".cpp"
                or fd == class_name + ".hxx" or fd == class_name + ".cxx"
                or fd == class_name + ".cc"
                or fd == class_name + ".h" or fd == class_name + ".c"):
            sys.exit("Class already exists")


def __cxx_class(config, path, class_name):
        os.chdir(path)
        __verify_unique(class_name)

        """ Initializing """
        project = config["NAME"]
        header_ext = config["PROJECT"]["CPP"]["HEADER"]
        source_ext = config["PROJECT"]["CPP"]["SOURCE"]
        namespace = config["PROJECT"]["NAMESPACE"]
        include_guards = config["PROJECT"]["INCLUDE-GUARDS"]

        """ Header Creation """
        header = util.read_file(template_path, "class.cxx.header")
        header = header.replace("--CMAKER_REPLACE", class_name.capitalize())
        if not namespace == "":
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
        os.chdir(path)
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

    if args[0] == 'cxx' or args[0] == 'cpp':
        if len(args) == 1:
            sys.exit("Class command requires class name")
        elif len(args) == 2:
            class_name = args[1]
            __cxx_class(config, ".", class_name)
        elif len(args) == 3:
            class_name = args[1]
            path = args[2]
            __cxx_class(config, path, class_name)
        else:
            sys.exit("Too many arguments")

    elif args[0] == 'c':
        if len(args) == 1:
            sys.exit("Class command requires class name")
        elif len(args) == 2:
            class_name = args[1]
            __c_class(config, ".", class_name)
        elif len(args) == 3:
            class_name = args[1]
            path = args[2]
            __c_class(config, path, class_name)
        else:
            sys.exit("Too many arguments")

    else:
        sys.exit("add {} is not supported".format(arg))

