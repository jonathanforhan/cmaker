import os
import sys


def scripts(args, scripts):
    command = False
    for arg in args:
        for key in scripts:
            if arg == key:
                value = scripts[key]
                if type(value) != type(""):
                    sys.exit("Scripts must be an array of strings")
                os.system(value)
                command = True
    return command

