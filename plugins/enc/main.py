#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from Plugin import Plugin


demoDataYaml = """
encrypt:
  enc: "test"
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




def runInMenu(stDict):
    ssh_cmd = "ssh " + stDict["ssh"]
    if "message_rich" in stDict:
        rich.console
        console = Console()
        console.print(Panel.fit(stDict["message_rich"]))
    os.system(ssh_cmd)


#
plugin = Plugin(namePlugin="enc", demoDataYaml=demoDataYaml,  runInMenu=runInMenu, icon=" ", titleIcon="")

