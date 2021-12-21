#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Plugin import Plugin
from plugins.theme.Theme import themes

dataYaml = """
    "settings":
        "theme": "grey" 
"""
demoDataYaml = """
    "settings":
        "theme": "grey" 
"""


def register(args):
    for t in themes:
        if t.name == args["configDict"]["theme"]:
            args["style"] = t.getStyle


plugin = Plugin(namePlugin="theme", demoDataYaml=demoDataYaml, dataYaml=dataYaml, customRegister=register)
