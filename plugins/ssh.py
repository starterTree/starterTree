#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from plugins.Plugin import Plugin
from plugins.Plugin import pluginsActivated

demoDataYaml="""
set:
  starterTree_theme: grey
serversDemoData:
  pet:
    demoData_ssh_server1:
      ssh: root@192.168.1.1
      tags: ["demoData","server","ssh","1","web","web1"]
      message_rich: "toto"
    demoData_ssh_server2:
      ssh: root@192.168.1.2
      tags: ["demoData","server","ssh","2","web","web2"]
    demoData_ssh_server3:
      ssh: root@192.168.1.1
      tags: ["demoData","server","ssh","1","backend","backend1"]
    demoData_ssh_server4:
      ssh: root@192.168.1.2
      tags: ["demoData","server","ssh","2","backend","backend2"]
  cattle: # best for search mod
    id5636734734653:
      ssh: root@192.168.1.2
      tags: ["demoData","server","ssh","bdd","bdd1"]
        
"""


def register(configDict,stDict):
    stDict["type"]="ssh"
    stDict["alter"]="mondial"
    stDict["content"]=configDict["ssh"]
    stDict["ssh"]=configDict["ssh"]
    if "message_rich" in configDict:
        stDict["message_rich"]=configDict["message_rich"]


def runInMenu(stDict):
    ssh_cmd = "ssh "+stDict["ssh"]
    if "message_rich" in stDict:
        rich.console
        console=Console()
        console.print(Panel.fit(stDict["message_rich"]))
    os.system(ssh_cmd)   



plugin=Plugin(demoDataYaml=demoDataYaml,register=register,runInMenu=runInMenu,icon="")
pluginsActivated["ssh"]=plugin



##########
#code bin#
##########
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

