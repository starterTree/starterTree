#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Plugin import Plugin
from plugins.theme.Theme import themes

dataYaml = """
    "theme":
        "hide" : true
        "theme": "grey" 
"""
demoDataYaml = """
    "theme":
        "hide" : true
        "theme": "grey" 

"""


def register(args):
    for t in themes:
        if t.name == args["configDict"]["theme"]:
            print('set theme')
            print(args["configDict"])
            args["data"]["style"] = t.getStyle()


plugin = Plugin(namePlugin="theme", demoDataYaml=demoDataYaml, dataYaml=dataYaml, customRegister=register)
