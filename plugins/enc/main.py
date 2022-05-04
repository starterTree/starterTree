#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich
from rich.console import Console
from rich.panel import Panel
from Plugin import Plugin
from rich.pretty import pprint

demoDataYaml = """
encrypt:
  enc: "test"
"""


#gpg -a --cipher-algo AES256 -c <<  /tmp/st.log.asc

def runInMenu(args):
    #os.system("gpg --batch --yes --out "+path+" -d "+path)
    #ssh_cmd = "ssh " + stDict["ssh"]
    os.system("to")
    args["objet"]["key_menu_completion"]={"toooo"}
    pprint(args["objet"])
    pprint(args["menuCompletion"])


#
plugin = Plugin(namePlugin="enc", demoDataYaml=demoDataYaml,  runInMenu=runInMenu, icon=" ", titleIcon="")

