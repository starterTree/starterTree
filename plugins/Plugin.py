#!/usr/bin/env python
# -*- coding: utf-8 -*-

pluginsActivated={}
pluginsA=[]

from rich.panel import Panel
from rich.pretty import pprint
from rich.padding import Padding
from rich.text import Text
from rich.table import Table
from rich import box
from rich.markdown import Markdown
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
    #grid =Table(expand=False, box=box.SQUARE,show_header=False,show_edge=False,padding=(0,1))
    #grid.add_row(a,Padding(content,pad=(0,0,0,0),expand=False))
    #return grid
    return Padding(content,pad=(0,0,0,0),expand=False)


#def defaultRegister(configDict,stDict,namePlugin):


#def dummyGetContentForRprompt(stDict):
#    return None

class Plugin :
    #def dummyGetContentForRprompt(self,stDict):
    #    return(stDict[self.namePlugin])


    'This is Plugin class for interract with st'
    def __init__(self,namePlugin="foo",demoDataYaml="{}",icon="",titleIcon="",titleColor="#666666",dataYaml="{}",register=None,runInMenu=dummyRunInMenu,getContentForRprompt=None,options=[],optionDebug=optionDebug):
        self.namePlugin=namePlugin
        self.demoDataYaml=demoDataYaml
        self.dataYaml=dataYaml
        self.icon=icon
        self.titleIcon=titleIcon
        self.titleColor=titleColor
        self._register=register
        self._runInMenu=runInMenu
        self._getContentForRprompt=getContentForRprompt
        self.options=options
        self._optionDebug=optionDebug
        pluginsActivated[self.namePlugin]=self
        pluginsA.append(self)



#    def dummyGetContentForRprompt(self,stDict):
#        return stDict[self.namePlugin]


    def getDemoDataYaml(self):
        return self.demoDataYaml
    def getDataYaml(self):
        return self.dataYaml
    def getName(self):
        return self.namePlugin

    def getIcon(self):
        return getIcon(self.icon)
    def getTitleIcon(self):
        return self.titleIcon

    def getContentForRprompt(self,stDict):
        if self._getContentForRprompt == None:
            #return Panel("[bold #444444 on white]"+stDict["description"],border_style="bold #444444 on red")
            #return "[bold #444444 on white]"+stDict["description"]
            #return displayTags(stDict["tags"])
            nameLeft="" 
            for i in (self.getTitleIcon()+stDict["type"].upper()):
                #nameLeft=nameLeft+"[bold #444444 on white]"+i+""+"\n"
                nameLeft=nameLeft+"[bold on white]"+i+""+"\n"
            grid =Table(expand=False, box=None,show_header=False,show_edge=False,padding=(0,1))
            grid.add_column(style=self.titleColor)
            grid2 =Table(expand=False, box=None,show_header=False,show_edge=False,padding=(0,1))
            grid2.add_row("[bold #444444 on white]\n"+stDict["description"]+"\n")
            #grid2.add_row(Markdown("# to "))
            #grid2.add_row(Markdown("`bash` "))
            grid2.add_row(displayTags(stDict["tags"]))
            grid.add_row(nameLeft,grid2)
            return grid

        #else:
        #    return self._getContentForRprompt(stDict)

    def register(self,configDict,stDict,menuDict=None,key=None,menu=None,path=None,settings=None,style=None):
        log={"name":self.namePlugin, "function":"register","configDict": configDict, "stDict":stDict,"menuDict":menuDict }
        icon=self.getIcon()
        if "icon" in configDict and detectNerdFont:
                icon=configDict["icon"]
        key_menu_completion=(icon+key).replace(" ","⠀")
        menu[key_menu_completion]={}

        stDict["path"]=path
        stDict["name"]=key

        stDict["type"]=self.namePlugin
        stDict["content"]=configDict[self.namePlugin]
        stDict["description"]=configDict[self.namePlugin]
        if "description" in configDict:
            stDict["description"]=configDict["description"]
        stDict["tags"]=[]
        if "tags" in configDict:
            stDict["tags"]=configDict["tags"]
        stDict[self.namePlugin]=configDict[self.namePlugin]
        #stDict=dict(configDict)
        for i in self.options:
            menuDict[key_menu_completion]["--"+i]={}
        if self._register != None:
            args = {"configDict":configDict, "stDict":stDict, "settings":settings, "completionDict":menuDict, "key_menu_completion":key_menu_completion, "completionDictElement": menuDict[key_menu_completion], "style": style }
            self._register(args)

    def runInMenu(self,objet,option=None,menuCompletion=None,pathEntry=None,style=None,tmpDir=None):
        if self._optionDebug != None:
            if option == "debug":
                args={"objet":objet }
                self._optionDebug(args)
                exit()
        args = {"objet":objet, "option":option, "menuCompletion":menuCompletion,"pathEntry":pathEntry,"style":style,"tmpDir":tmpDir }
        self._runInMenu(args)


import plugins.ListPlugins
