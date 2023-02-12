import os
from re import findall

def scripts(args):
    if len(args) > 1:
        return False
    if not os.path.exists("scripts.cmaker"):
        return False
    arg = args[0]
    f = open("scripts.cmaker", "r")
    lines = f.readlines();
    for line in lines:
        line, _, _ = line.partition('#')
        if line.lstrip().startswith(arg) and line.find('=') != -1:
            command = findall('"([^"]*)"', line)
            os.system(command[0])
            return True
    return False
