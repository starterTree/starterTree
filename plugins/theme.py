#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plugins.Plugin import Plugin,pluginsActivated

demoDataYaml={}

def register(args):
    if args["objet"]["theme"] == "grey":




plugin=Plugin(namePlugin="theme",demoDataYaml=demoDataYaml,register=register,runInMenu=runInMenu,icon="⠀",titleIcon="",titleColor="red",options=["debug"])
