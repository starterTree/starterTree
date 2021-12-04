#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from rich.pretty import pprint

#voir toute la commane qui va etre executé

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
    stDict["alter"]="mondial"
    if "message_rich" in configDict:
        stDict["message_rich"]=configDict["message_rich"]

        

def runInMenu(args):
#        pprint(stDict,expand_all=True)
    ssh_cmd = "ssh "+args["objet"]["ssh"]
    if "message_rich" in args["objet"]:
        rich.console
        console=Console()
        console.print(Panel.fit(args["objet"]["message_rich"]))
    os.system(ssh_cmd)   



from plugins.Plugin import Plugin,pluginsActivated
plugin=Plugin(namePlugin="ssh",demoDataYaml=demoDataYaml,register=register,runInMenu=runInMenu,icon="",titleIcon="",options=["debug"])



##########
#code bin#
##########
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

