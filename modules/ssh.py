#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel

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

#code bin
					#path_entry_name_content["path_"+path_entry_name+keya]=source_dict[key]
#					if len(source_dict[key][subKey].split("{{")) == 2 and len(source_dict[key][subKey].split("}}")) == 2:
#						print(source_dict[key][subKey].split("{{")[1].split("}}")[0])
#						path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey].replace("{{"+source_dict[key][subKey].split("{{")[1].split("}}")[0]+"}}" ,eval(source_dict[key][subKey].split("{{")[1].split("}}")[0]))
#

