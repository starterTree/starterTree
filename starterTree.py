#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO voir rempacer icon par entree ? ou/et sinon incruster icone > (ou toutes icons ?) dans le parseur


# load Plugins

from Plugin import pluginsA

from modules import loadData, mainPrompt, bottomToolbar

from sys import exit
import os
import sys
import requests
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit import PromptSession
# from modules.output.textable import Tableau as Tableau
from shlex import quote
# import base64
# import paramiko
# import colorama
from rich.pretty import pprint


import modules.downloadWebContent


# style=Style.from_dict(settings)


def getIcon(icon, defaultIcon=""):
    if detectNerdFont:
        return icon
    return defaultIcon


# print(type(text))
def getPromptText():
    icon = "search > ssh_cmd >"
    if detectNerdFont: icon = "     "
    history = FileHistory(tmpDir + ".history_ssh_cmd")
    session = PromptSession("\n" + icon + " ", style=style, key_bindings=bindings, history=history)
    prompt = session.prompt(default="", rprompt=None)
    # prompt= prompt.replace('"','')
    prompt = prompt.encode('ascii', errors='ignore').decode()
    return prompt


def ssh_cmd(result):
    promptT = getPromptText()
    for r in result:
        if ssh_module_keyword in path_entry_name_content[r]:
            #	tableau=Tableau(['N°','Path','Name','Type','Tags'],detectNerdFont)
            #	setNoneForValue(path_entry_name_content[r],["type","tags"])
            #	tableau.add_row([path_entry_name_content[r]["tmp_id"],path_entry_name_content[r]["path"],path_entry_name_content[r]["name"],path_entry_name_content[r]["type"],path_entry_name_content[r]["tags"]])
            #	print()
            # tableau.draw(icon+" "+prompt)
            os.system("ssh " + path_entry_name_content[r][ssh_module_keyword] + " " + quote(promptT))
    ssh_cmd(result)


def getTag(result):
    myComplete = {}
    myCompleteL = []
    for r in result:
        if "tags" in path_entry_name_content[r]:
            if type(path_entry_name_content[r]["tags"]) == list:
                for i in path_entry_name_content[r]["tags"]:
                    myComplete[i] = {}
    for i in myComplete:
        myCompleteL.append(i)
    # promptT = getPromptText()

    completer = FuzzyCompleter(WordCompleter(myCompleteL, ignore_case=True))

    print(myCompleteL)
    icon = "search > tag >"
    if detectNerdFont: icon = "   "
    session = PromptSession(icon + " ", style=style, key_bindings=bindings)
    # prompt= session.prompt(pre_run=session.default_buffer.start_completion,default="",completer=completer)
    prompt = session.prompt(pre_run=session.default_buffer.start_completion, default="", completer=completer)


def setNoneForValue(tab, values):
    for i in values:
        if i not in tab: tab[i] = "none"


tmpDir = os.environ['HOME'] + '/.starterTree/'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)

configDir = os.environ['HOME'] + '/.config'
try:
    configFile = str(sys.argv[1])
except IndexError:
    configFile = os.environ['HOME'] + '/.config/starterTree/config.yml'

absolute_path_main_config_file = os.path.dirname(configFile) + "/"

promptTitle = os.path.basename(sys.argv[0])
if promptTitle == "starterTree.py":
    promptTitle = ""


def main():
    # charge data ( data yaml from plugins and data yaml file or data yaml plugins and data demo)
    starterTreeDATA = {
        "path_entry_name_content": {},
        "menu_completion": {},
        "style": {
            "completionMenu": {}
        },
        "settings": {},
        "config": {
            "name" : "default",
            "displayVersion": True,
        },
        "tmpDir": tmpDir,
        "plugins": pluginsA
    }

    import logging
    logging.basicConfig(filename='/tmp/st.log', level=logging.DEBUG, filemode='w')

    logging.debug("loadData(configFile="+str(configFile)+", data="+str(starterTreeDATA))
    loadData.loadData(configFile=configFile, data=starterTreeDATA)
    pprint(starterTreeDATA["menu_completion"])
    logging.debug("execMainPromptSession(data=" + str(starterTreeDATA) + ", promptTitle=" + str(promptTitle))
    mainPrompt.execMainPromptSession(data=starterTreeDATA, promptTitle=promptTitle,
                                     bottomToolbar=bottomToolbar.getToolbar(starterTreeDATA))


if __name__ == "__main__":
    # style=settings["theme"]
    main()

exit()
