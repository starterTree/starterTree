#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os



import logging
logging.basicConfig(filename='/tmp/st.log', level=logging.DEBUG)


from rich.pretty import pprint
import yaml
from prompt_toolkit.styles import Style

from jinja2 import Template

detectNerdFont = False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont = True


def getIcon(icon, defaultIcon=""):
    if detectNerdFont:
        return icon
    return defaultIcon


tmpDir = os.environ['HOME'] + '/.starterTree/'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)


def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    return yaml.load(template.render(), Loader=yaml.SafeLoader)


def detectIfoneSubEntry(source_dict,key,plugins):
    count = 0
    bad = 0
    sub_e = ""
    for sub in source_dict[key]:
        for p in (plugins):

            if p.getName() == sub:
                count = count + 1
                sub_e = sub
        if isinstance(source_dict[key][sub], dict):
            bad = 1
    if bad == 0 and count == 1:
        return sub_e
    else: return None

def my_fun(source_dict, menu_completion, plugins, data, path_entry_name="", path_entry_name_path="", tab="\t"):
    for key in source_dict:
        logging.debug("myFun: " + str(key) + " " )
        key = key.encode('ascii', errors='ignore').decode().replace(" ", "⠀")
        data["path_entry_name_content"]["path_" + path_entry_name + key] = {}
        icon = ""

        def register(p):
            if p.getName() == key:
                p.register(configDict=source_dict, menu_completion=menu_completion, key=key, path_entry_name=path_entry_name, data=data, path=path_entry_name_path + "/",tmpDir=tmpDir)

        # cas specifique
        # si cest une feuille
        if not isinstance(source_dict[key], dict):
            logging.debug("detect leaff: "+str(key)+": "+str(source_dict[key]))
            for p in (plugins):
                if p.getName() == key:
                    logging.debug("register "+p.getName())
                    p.register(configDict=source_dict, menu_completion=menu_completion, path_entry_name=path_entry_name, key=key, path=path_entry_name_path + "/", data=data,tmpDir=tmpDir)

        # si c'est unre branche
        if isinstance(source_dict[key], dict):
            logging.debug("detect branch: " + str(key) + " " + str(source_dict[key]))
            if detectNerdFont: icon = " "
            if "icon" in source_dict[key] and detectNerdFont:
                icon = source_dict[key]["icon"]

            #  si cest une branche qui contient une seule feuille
            # un sous dossier qui contient une seule entree classique
            cond=detectIfoneSubEntry(source_dict,key,plugins)
            if cond is not None:
                logging.debug("detect branch with one leaf: " + str(key) + " " + str(source_dict[key]))
                for p in (plugins):
                    if p.getName() == cond:
                        logging.debug("register " + p.getName())
                        p.register(configDict=source_dict[key], menu_completion=menu_completion, key=key, data=data, path=path_entry_name_path + "/", path_entry_name=path_entry_name,tmpDir=tmpDir)
            # alors cest un sous dossier
            # si cest une branche qui contient plusieurs feuilles
            else:
                logging.debug("detect branch with multiple leaf: " +str(key) + " " + str(source_dict[key]))
                #key_menu_completion = (icon + key).replace(" ", "⠀")

                menu=None
                for p in (plugins):
                    if p.getName() == "dir":
                        logging.debug("register "+p.getName())
                        p.register(configDict=source_dict[key], menu_completion=menu_completion, key=key, data=data, path=path_entry_name_path + "/", path_entry_name=path_entry_name,tab=tab + "\t" + "\t",tmpDir=tmpDir)
                if "hide" not in source_dict[key]:
                     pass


    return data, menu_completion
