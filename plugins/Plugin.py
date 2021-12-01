#!/usr/bin/env python
# -*- coding: utf-8 -*-

pluginsActivated={}

def dummyRegister(configDict,stDict):
    return None

def dummyRunInMenu(objet):
    return None

class Plugin :
    'This is Plugin class for interract with st'
    def __init__(self,demoDataYaml="{}",icon="",register=dummyRegister,runInMenu=dummyRunInMenu):
        self.demoDataYaml=demoDataYaml
        self.icon=icon
        self.register=register
        self.runInMenu=runInMenu

    def getDemoDataYaml(self):
        return self.demoDataYaml

    def getIcon(self):
        return self.icon

    def register(self,tabl1,tabl2):
        self.register(tabl1,tabl2)
    
    def runInMenu(self,objet):
        self.runInMenu(objet)

import plugins.ListPlugins
