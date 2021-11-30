#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel


demoDataYaml="""
serversDemoData:
  pet:
    demoData_ssh_server1:
      ssh: root@192.168.1.1
      tags: ["demoData","server","ssh","1","web","web1"]
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


def getDemoData():
    return demoDataYaml

def register(config_dict,st_dict):
    st_dict["type"]="ssh"
    st_dict["content"]=config_dict["ssh"]
    st_dict["ssh"]=config_dict["ssh"]
    if "message_rich" in config_dict:
        st_dict["message_rich"]=config_dict["message_rich"]

	
""" ssh_object
name_of_server:
    ssh: root@user
    message_rich: "[red] warning [/red]"
    tags: tags

"""

def launch(ssh_object):
    ssh_cmd = "ssh "+ssh_object["ssh"]
    if "message_rich" in ssh_object:
        rich.console
        console=Console()
        console.print(Panel.fit(ssh_object["message_rich"]))
    os.system(ssh_cmd)   
    
def getIcon():
    return ""


##########
#code bin#
##########
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

