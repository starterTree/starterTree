#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from rich.pretty import pprint
#from starterTree import path_entry_name_content

#voir toute la commane qui va etre executé

demoDataYaml="""
{}
"""

dataYaml="""
settings:
 # icon: ""
  update:
    setting: update
    description: update to new version, add --v0.14f to downlad precise version
  version:
    setting: version
  debug:
    completion:
      setting: completion
      description: show completion dict
    config:
      setting: config
      description: show config dict

"""

def register(configDict,stDict):
    stDict["type"]="settings"
    pass
        

def runInMenu(args):
    stDict=args["objet"]
    menuCompletion=args["menuCompletion"]
    pathEntry=args["pathEntry"]
    if stDict["setting"] == "version":
        print("version is git rev-parse HEAD hash")
    if stDict["setting"] == "completion":
        pprint(menuCompletion)
        #print(json.dumps(menu_completion, sort_keys=False, indent=4))
    if stDict["setting"] == "config":
        pprint(pathEntry)
        #print(json.dumps(path_entry_name_content, sort_keys=False, indent=4))
    if stDict["setting"] == "update" :
        if option != None:
            pprint("download specific version")   
            os.system("cd /opt ; sudo curl -L 'https://github.com/thomas10-10/starterTree/releases/download/"+option+"/starterTree.tar.gz' | sudo tar -xz")   
        else:
            os.system('cd /opt ; sudo curl -L "https://github.com/thomas10-10/starterTree/releases/download/$(basename $(curl -fsSLI -o /dev/null -w %{url_effective} https://github.com/thomas10-10/starterTree/releases/latest))/starterTree.tar.gz" | sudo tar -xz')   



from plugins.Plugin import Plugin,pluginsActivated
plugin=Plugin(namePlugin="setting",demoDataYaml=demoDataYaml,dataYaml=dataYaml,register=register,runInMenu=runInMenu,icon=" ",options=["debug"])



##########
#code bin#
##########
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

