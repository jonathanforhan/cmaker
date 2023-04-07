import os
import sys
import json
from collections import UserDict

from src import util


"""
Emulates cmaker-config.json 
Case-Insensitive on both read and write
"""
class Config(UserDict):
    def __setitem__(self, key, val):
        key = key.upper()
        super().__setitem__(key, val)

    def __getitem__(self, key):
        key = key.upper()
        return self.data[key]

    def __init_defaults(self):
        self["name"] = "Unnamed"
        self["version"] = "1.0.0"
        self["license"] = "Unspecified"
        self["project"] = Config({
            "cpp" : Config({
                "header" : "hpp",
                "source" : "cpp",
                "standard" : 17,
                "standard-required" : True
            }),
            "c" : Config({
                "header" : "h",
                "source" : "c",
                "standard" : 99,
                "standard-required" : True
            }),
            "include-guards": "PROJECT-DIR-FILE",
            "namespace": ""
        })
        self["build"] = Config({
            "make": "Ninja",
            "export-compile-commands": True,
            "verbose-makefile": False,
            "debug" : Config({
                "build-dir": "build-debug",
                "output" : "./bin/debug",
                "flags" : [
                    "CMAKE_BUILD_TYPE=Debug"
                ]
            }),
            "release" : Config({
                "build-dir": "build-release",
                "output" : "./bin/release",
                "flags" : [
                    "CMAKE_BUILD_TYPE=Release"
                ]
            })
        })
        self["scripts"] = {
            "dev" : "cmkr build --debug; cd ./bin/debug; ./--CMAKER_REPLACE",
            "run-release" : "cmkr build --release; cd ./bin/release; ./--CMAKER_REPLACE",
            "clean": "rm -rdf ./build**/*"
        }

    def __json_recursive_copy(self, data, check):
        for key in data:
            if check.get(key) and data.get(key):
                if not type(check[key]) == type(data[key]):
                    if not (type(check[key]) == type(Config()) and type(data[key]) == type({})):
                        sys.exit("cmaker-config.json contains invalid configuration data for option: {}".format(key))
                if type(data[key]) == type({}) and not key.upper() == "SCRIPTS":
                    self.__json_recursive_copy(data[key], check[key])
                else:
                    check[key] = data[key]
            # handle 'None' defaults
            if key == "namespace" and data.get(key):
                check[key] = data[key]

    def parse_config(self):
        self.__init_defaults()
        cwd = os.getcwd()
        needle = False
        while "home" in os.getcwd() or "C:" in os.getcwd():
            for f in os.listdir(os.getcwd()):
                if f == "cmaker-config.json":
                    needle = True
            if needle:
                break
            os.chdir("..")

        if not needle:
            sys.exit("Could not find cmaker-config.json in your path")

        try:
            with open("cmaker-config.json") as f:
                data = json.load(f)
                self.__json_recursive_copy(data, self)
        except:
            sys.exit("cmaker-config.json contains invalid json")

        os.chdir(cwd) # reset to cwd once we find cmaker-config

