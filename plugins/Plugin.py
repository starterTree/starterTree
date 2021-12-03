#!/usr/bin/env python
# -*- coding: utf-8 -*-

pluginsActivated={}

from rich.panel import Panel
from rich.pretty import pprint
from rich.padding import Padding
from rich.text import Text
from rich.table import Table
from rich import box
import os
def dummyRegister(configDict,stDict):
    return None

def dummyRunInMenu(objet):
    return None

def optionDebug(objet):
    pprint(objet,expand_all=True)

detectNerdFont= False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont= True


def getIcon(icon,defaultIcon=""):
    if detectNerdFont:
        return icon
    return defaultIcon

a=""
for i in "toto":
    a=a+i+"\n"

def displayTags(tags):
#    return tags
    content=Text("",overflow="fold")
    for r in range(len(tags)):
        icon=''
        style=''
        if tags[r]== "server": icon=getIcon(" ");style="bold red"
        if tags[r] == "web": icon=getIcon(" ");style="bold blue"
        #r=' '+r+' '
        #content.append("[white on black] "+r+" ")
        #content=content+("[white on black] "+r+" [/white on black] ")
        #content=content+Text(''+r,overflow="fold",style="bold white")+Text(" ")
        if (r % 2) == 0:
            #content=content+Text(''+tags[r],overflow="fold",style="bold #ffffff")+Text(" ")
            if icon=='': icon=getIcon('')
            if style=='': style="#f2f2f2"
            content=content+Text(" "+icon+tags[r]+" ",overflow="fold",style=style)+Text(" ")
        else:
            if icon=='': icon=getIcon('')
            if style=='': style="#f2f2f2"
            content=content+Text(" "+icon+tags[r]+" ",overflow="fold",style=style)+Text(" ")
    grid =Table(expand=False, box=box.SQUARE,show_header=False,show_edge=False,padding=(0,1))
    grid.add_row(a,Padding(content,pad=(0,0,0,0),expand=False))
    return grid
    return Padding(content,pad=(0,0,0,0),expand=False)


#def defaultRegister(configDict,stDict,namePlugin):


#def dummyGetContentForRprompt(stDict):
#    return None

class Plugin :
    #def dummyGetContentForRprompt(self,stDict):
    #    return(stDict[self.namePlugin])


    'This is Plugin class for interract with st'
    def __init__(self,namePlugin="foo",demoDataYaml="{}",icon="",dataYaml="{}",register=None,runInMenu=dummyRunInMenu,getContentForRprompt=None,options=[],optionDebug=optionDebug):
        self.namePlugin=namePlugin
        self.demoDataYaml=demoDataYaml
        self.dataYaml=dataYaml
        self.icon=icon
        self._register=register
        self._runInMenu=runInMenu
        self._getContentForRprompt=getContentForRprompt
        self.options=options
        self._optionDebug=optionDebug
        pluginsActivated[self.namePlugin]=self



#    def dummyGetContentForRprompt(self,stDict):
#        return stDict[self.namePlugin]


    def getDemoDataYaml(self):
        return self.demoDataYaml
    def getDataYaml(self):
        return self.dataYaml

    def getIcon(self):
        return self.icon

    def getContentForRprompt(self,stDict):
        if self._getContentForRprompt == None:
            #return Panel("[bold #444444 on white]"+stDict["description"],border_style="bold #444444 on red")
            #return "[bold #444444 on white]"+stDict["description"]
            return displayTags(stDict["tags"])

        grid.add_row(a,displayTags(stDict["tags"]))
        grid =Table(expand=False, box=box.SQUARE,show_header=False,show_edge=False,padding=(0,1))

        #else:
        #    return self._getContentForRprompt(stDict)

    def register(self,configDict,stDict,menuDict=None):
        stDict["type"]=self.namePlugin
        stDict["content"]=configDict[self.namePlugin]
        stDict["description"]=configDict[self.namePlugin]
        if "description" in configDict:
            stDict["description"]=configDict["description"]
        stDict["tags"]=[]
        if "tags" in configDict:
            stDict["tags"]=configDict["tags"]
        stDict[self.namePlugin]=configDict[self.namePlugin]
        for i in self.options:
            menuDict["--"+i]={}
        if self._register != None:
            self._register(configDict=configDict,stDict=stDict)


    def runInMenu(self,objet,option=None,menuCompletion=None,pathEntry=None,style=None):
        if self._optionDebug != None:
            if option == "debug":
                args={"objet":objet }
                self._optionDebug(args)
                exit()
        args = {"objet":objet, "option":option, "menuCompletion":menuCompletion,"pathEntry":pathEntry,"style":style }
        self._runInMenu(args)


import plugins.ListPlugins
