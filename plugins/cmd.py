#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from prompt_toolkit.shortcuts import prompt

from plugins.Plugin import Plugin
from plugins.Plugin import pluginsActivated
from prompt_toolkit.key_binding import KeyBindings

demoDataYaml="""
cmdDemoData:
  cmd:
    ls:
      cmd: ls
    coco:
      cmd: echo "coco"
      prompt: yes
"""
 
bindings = KeyBindings()
@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()


def register(configDict,stDict):
    stDict["type"]="cmd"
    stDict["content"]=configDict["cmd"]
    stDict["description"]=configDict["cmd"]
    stDict["cmd"]=configDict["cmd"]
    if "prompt" in configDict:
        stDict["prompt"]=configDict["prompt"]


def runInMenu(stDict):
    cmd = stDict["cmd"]
    if "prompt" in stDict and stDict["prompt"] not in ["No","no","NO","False","false","FALSE","0"]:
        cmd = prompt("> ", default='%s' % cmd,key_bindings=bindings,)
    if cmd is not None:   
        os.system(cmd)   



plugin=Plugin(demoDataYaml=demoDataYaml,register=register,runInMenu=runInMenu,icon="")
pluginsActivated["cmd"]=plugin

##########
#code bin#
##########
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

