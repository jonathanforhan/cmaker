import os, sys
from re import findall

def run_script(arg):
    f = open("scripts.cmaker", "r")
    lines = f.readlines();
    for line in lines:
        line, _, _ = line.partition('#')
        if line.startswith(arg) and line.find('=') != -1:
            command = findall('"([^"]*)"', line)
            os.system(command[0])
            return True
    return False
