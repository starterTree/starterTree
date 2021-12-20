#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plugins.Plugin import Plugin

themes = []


class Theme:
    def __init__(self, name, styleDict=None):
        self.name = name
        self.styleDict = styleDict
        themes.append(self)

    def getName(self):
        return self.name

    def getStyle(self):
        return self.styleDict


import plugins.theme.ListThemes

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
        if t.name == args["stDict"]["theme"]:
            args["style"] = t.getStyle


plugin = Plugin(namePlugin="theme", demoDataYaml=demoDataYaml, dataYaml=dataYaml, register=register)
