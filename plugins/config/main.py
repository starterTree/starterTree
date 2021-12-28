#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Plugin import Plugin

dataYaml = """
    "configDefaultData":
        "hide" : "true"
        "name": "starterTree"
        "displayVersion": "True"
        "description": "configSetting default"
        
"""
demoDataYaml = """
    "configDemoData":
        "hide" : "true"
        changeNameTest:
            "name": "demoo" 
        "displayVersion": True
        "description": "configSetting demo"
        
"""


def register(args):
    args["data"]["config"]["name"] = args["configDict"]["name"]


plugin = Plugin(namePlugin="name", demoDataYaml=demoDataYaml, dataYaml=dataYaml, customRegister=register)




def register(args):
    args["data"]["config"]["displayVersion"] = args["configDict"]["displayVersion"]


plugin2 = Plugin(namePlugin="displayVersion", demoDataYaml=demoDataYaml, dataYaml=dataYaml, customRegister=register)
