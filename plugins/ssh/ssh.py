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
      cmd: coco
      cmd: coco2
      ssh: root@192.168.1.1
      tags: ["demoData","server","ssh","1","web","web1"]
      message_rich: "toto"
      cmd:
        cmd: coco1111
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


def register(args):
    configDict=args["configDict"]
    stDict=args["stDict"]
    if "message_rich" in configDict:
        stDict["message_rich"]=configDict["message_rich"]

        

def runInMenu(args):
    ssh_cmd = "ssh "+args["objet"]["ssh"]
    if "message_rich" in args["objet"]:
        rich.console
        console=Console()
        console.print(Panel.fit(args["objet"]["message_rich"]))
    os.system(ssh_cmd)   



from plugins.Plugin import Plugin,pluginsActivated
plugin=Plugin(namePlugin="ssh",demoDataYaml=demoDataYaml,register=register,runInMenu=runInMenu,icon="⠀",titleIcon="",titleColor="red",options=["debug"])



