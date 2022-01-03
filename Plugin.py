#!/usr/bin/env python
# -*- coding: utf-8 -*-

pluginsActivated = {}
pluginsA = []

from rich.panel import Panel
from rich.pretty import pprint
from rich.padding import Padding
from rich.text import Text
from rich.table import Table
from rich import box
from rich.markdown import Markdown
import os


def dummyRegister(configDict, stDict):
    return None


def dummyRunInMenu(objet):
    return None


def optionDebug(objet):
    pprint(objet, expand_all=True)


detectNerdFont = False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont = True


def getIcon(icon, defaultIcon=""):
    if detectNerdFont:
        return icon
    return defaultIcon


def defaultRegister(args):
    icon = args["self"].getIcon()
    if "icon" in args["configDict"] and detectNerdFont:
        icon = args["configDict"]["icon"]

    key_menu_completion = (icon + args["key"]).replace(" ", "⠀")
    args["menu_completion"][key_menu_completion] = {}

    args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]] = {
        "path": args["path"],
        "titleIcon" : args["self"].getTitleIcon(),
        "title": args["self"].title,
        "name": args["key"],
        "type": args["self"].namePlugin,
        "key_menu_completion": key_menu_completion,
        "preview": args["preview"],
        "content": args["configDict"][args["self"].namePlugin],
        "description": args["configDict"][args["self"].namePlugin],
        "tags": [],
        "self": args["self"],
        args["self"].namePlugin: args["configDict"][args["self"].namePlugin]

    }

    def overwrite(k):
        if k in args["configDict"]:
            args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]][k] = args["configDict"][k]

    overwrite("description")
    overwrite("tags")

    # stDict=dict(configDict)
    for i in args["self"].options:
        args["menu_completion"][key_menu_completion]["--" + i] = {}


def displayTags(tags):
    #    return tags
    content = Text("", overflow="fold")
    for r in range(len(tags)):
        icon = ''
        style = ''
        if tags[r] == "server": icon = getIcon(" ");style = "bold red"
        if tags[r] == "web": icon = getIcon(" ");style = "bold blue"
        # r=' '+r+' '
        # content.append("[white on black] "+r+" ")
        # content=content+("[white on black] "+r+" [/white on black] ")
        # content=content+Text(''+r,overflow="fold",style="bold white")+Text(" ")
        if (r % 2) == 0:
            # content=content+Text(''+tags[r],overflow="fold",style="bold #ffffff")+Text(" ")
            if icon == '': icon = getIcon('')
            if style == '': style = "#f2f2f2"
            content = content + Text(" " + icon + tags[r] + " ", overflow="fold", style=style) + Text(" ")
        else:
            if icon == '': icon = getIcon('')
            if style == '': style = "#f2f2f2"
            content = content + Text(" " + icon + tags[r] + " ", overflow="fold", style=style) + Text(" ")
    # grid =Table(expand=False, box=box.SQUARE,show_header=False,show_edge=False,padding=(0,1))
    # grid.add_row(a,Padding(content,pad=(0,0,0,0),expand=False))
    # return grid
    return Padding(content, pad=(0, 0, 0, 0), expand=False)


# def defaultRegister(configDict,stDict,namePlugin):


# def dummyGetContentForRprompt(stDict):
#    return None

class Plugin:
    # def dummyGetContentForRprompt(self,stDict):
    #    return(stDict[self.namePlugin])

    'This is Plugin class for interract with st'

    def __init__(self, namePlugin="foo", demoDataYaml="{}", icon="", titleIcon="", titleColor="#666666", dataYaml="{}",
                 customRegister=None, afterRegister=None, runInMenu=dummyRunInMenu, getContentForRprompt=None,
                 options=[], getCustomContentForRprompt=None, title="",
                 optionDebug=optionDebug):
        self.namePlugin = namePlugin
        self.demoDataYaml = demoDataYaml
        self.dataYaml = dataYaml
        self.icon = icon
        if title != "" :
            self.title = title
        else:
            self.title = namePlugin
        self.titleIcon = titleIcon
        self.titleColor = titleColor
        self.customRegister = customRegister
        self.afterRegister = afterRegister
        self.getCustomContentForRprompt = getCustomContentForRprompt
        self._runInMenu = runInMenu
        self._getContentForRprompt = getContentForRprompt
        self.options = options
        self._optionDebug = optionDebug
        pluginsActivated[self.namePlugin] = self
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
        return getIcon(self.titleIcon)

    def getDefaultContentForRprompt(self,args):
        nameLeft = ""
        for i in (args["element"]["titleIcon"] + args["element"]["title"].upper()):
            nameLeft = nameLeft + "[bold on white]" + i + "" + "\n"
        grid = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 1))
        grid.add_column(style=args["self"].titleColor)
        grid2 = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 1))
        grid2.add_row("[bold #444444 on white]\n" + args["element"]["description"] + "\n")
        # markdown is possible grid2.add_row(Markdown("`bash` "))
        grid2.add_row(displayTags(args["element"]["tags"]))
        grid.add_row(nameLeft, grid2)
        return grid

    def getContentForRprompt(self, element):
        args = {"element": element, "self": self}

        if self.getCustomContentForRprompt is not None:
            return(self.getCustomContentForRprompt(args))
        else:
            return(self.getDefaultContentForRprompt(args))


    def register(self, configDict, key=None, path=None, data=None, path_entry_name=None,menu_completion=None, tab="",tmpDir=""):
        data["path_entry_name_content"]["path_" + path_entry_name + key] = {}
        args = {"configDict": configDict,
                "element": data["path_entry_name_content"]["path_" + path_entry_name + key],
                "key_menu_completion": "key_menu_completion",
                "completionDictElement": "menuDict[key_menu_completion]",
                "data": data,
                "key":key,
                "path":path,
                "path_entry_name":path_entry_name,
                "menu_completion": menu_completion,
                "titleIcon": self.getTitleIcon(),
                "preview": menu_completion,
                "self": self ,
                "tmpDir": tmpDir,
                "tab": tab}
        data["path_entry_name_content"]["path_" + path_entry_name + key]["titleIcon"]=self.getTitleIcon()
        if self.customRegister is not None:
            self.customRegister(args)
        else:
            defaultRegister(args)
            if self.afterRegister is not None:
                self.afterRegister(args)

    def runInMenu(self, objet, data, option=None, pathEntry=None):
        if self._optionDebug is not None:
            if option == "debug":
                args = {"objet": objet}
                self._optionDebug(args)
                exit()
        args = {"objet": objet, "configDict": objet, "option": option, "menuCompletion": data["menu_completion"], "pathEntry": pathEntry,
                "style": data["style"], "tmpDir": data["tmpDir"], "self": self, "data": data}
        self._runInMenu(args)


import plugins.ListPlugins
