#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from rich.pretty import pprint
from rich.table import Table

from modules.utils import my_fun

from prompt_toolkit.styles import Style

# from starterTree import path_entry_name_content

# voir toute la commane qui va etre executé



def preview(args):
    from rich.padding import Padding
    from rich.columns import Columns
    a=[]
    for i in args["element"]["preview"][args["element"]["key_menu_completion"]]:
        if i  not in ["--list"] :
            a.append(i)
    user_renderables = [Padding("[bold on white]"+user, expand=True) for user in a]
    return(Columns(user_renderables))

def getContentForRprompt(args):
    nameLeft = ""
    for i in (args["element"]["type"].upper()):
        nameLeft = nameLeft + "[bold on white]" + i + "" + "\n"
    nameLeft="[bold on green]"+args["self"].getTitleIcon()+"\n" + nameLeft
    grid = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 1))
    grid.add_column(style=args["self"].titleColor)
    grid2 = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 0))
    grid2.add_row("[bold on green]"+args["element"]["name"]+"[bold #444444 on white]\n" + args["element"]["description"] + "\n")
    # grid2.add_row(Markdown("`bash` "))     # markdown is possible !
    grid2.add_row(Plugin.displayTags(args["element"]["tags"]))
    grid3 = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 0))
    #grid3.add_row(Panel.fit(preview(args),title=args["self"].getTitleIcon(),style="bold on green"))
    grid3.add_row(preview(args))
    grid.add_row(nameLeft, grid2,Panel.fit(grid3,title=args["self"].getTitleIcon()+" "+args["element"]["name"],style="bold on green"))
    #grid.add_row(nameLeft, grid2, grid3)
    return grid

def register(args):
    icon = args["self"].getIcon()
    if "icon" in args["configDict"]:
        icon = args["configDict"]["icon"]


    key_menu_completion = (icon + args["key"]).replace(" ", "⠀")
    if "hide" not in args["configDict"]:
        args["menu_completion"][key_menu_completion]={}
    #args["menu_completion"][key_menu_completion] = {}



    args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]] = {
        "path": args["path"],
        "name": args["key"],
        "type": args["self"].namePlugin,
        "title": args["self"].title,
        "key_menu_completion": key_menu_completion,
        #"content": args["configDict"][args["self"].namePlugin],
        "tags": [],
        "preview":args["menu_completion"],
        "description": "directory",
        "titleIcon": args["self"].getTitleIcon()
    }
    args["element"]["preview"]="heho"
    args["element"]["name"]=args["key"]
    args["element"]["titleIcon"] = args["self"].getTitleIcon()
    menu={}
    if "hide" not in args["configDict"]:
        menu=args["menu_completion"][key_menu_completion]

    my_fun(
        source_dict=args["configDict"],
        menu_completion=menu,
        path_entry_name=args["path_entry_name"] + args["key"],
        path_entry_name_path=args["path"] + args["key"],
        plugins=args["data"]["plugins"],
        data=args["data"],
        tab=args["tab"]
    )

   # args["element"]["preview"]=args["menu_completion"]


    def overwrite(k):
        if k in args["configDict"]:
            print("detect")
            print(args["configDict"][k])
            args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]][k] = args["configDict"][k]

    overwrite("description")
    overwrite("tags")
    if "description" in args["configDict"]:
        print("hey",args["configDict"]["description"])
        args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]]["description"]="fuck"
        print(args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]]["description"]),
    if "description" in args["configDict"]:
        print(args["configDict"])
        args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]]["description"] = "fuck"

    args["data"]["path_entry_name_content"]["path_" + args["path_entry_name"] + args["key"]]["tags"].append("dir")

    overwrite("description")
    # stDict=dict(configDict)
    #for i in self.options:
    #    menu_completion[key_menu_completion]["--" + i] = {}



import Plugin


plugin = Plugin.Plugin(namePlugin="dir", icon=" ", customRegister=register, getCustomContentForRprompt=getContentForRprompt, titleIcon="", options=["debug"])
