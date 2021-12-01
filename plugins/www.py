#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from plugins.Plugin import Plugin
from plugins.Plugin import pluginsActivated

demoDataYaml="""
linksDemoData:
  mySites:
    google:
      www: https://google.fr
    gitlab:
      www: gitlab.fr
"""
 

def register(configDict,stDict):
    stDict["type"]="www"
    stDict["content"]=configDict["www"]
    stDict["description"]=configDict["www"]
    stDict["www"]=configDict["www"]


def runInMenu(stDict):
	text = "xdg-open "+stDict["www"]
	os.system(text)   



plugin=Plugin(demoDataYaml=demoDataYaml,register=register,runInMenu=runInMenu,icon="")
pluginsActivated["www"]=plugin



##########
#code bin#
##########
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

