import os
import sys

def scripts(args, scripts):
    command = False
    for arg in args:
        for key in scripts:
            if arg == key:
                value = scripts[key]
                if not type(value) == type(""):
                    sys.exit("Scripts must be strings")
                os.system(value)
                command = True
    return command

