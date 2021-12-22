#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Plugin import Plugin

demoDataYaml = """
linksDemoData:
  mySites:
    google:
      www: https://google.fr
    gitlab:
      www: gitlab.fr
"""


def runInMenu(args):
    text = "xdg-open " + args["objet"]["www"]
    os.system(text)


plugin = Plugin(namePlugin="www", demoDataYaml=demoDataYaml, runInMenu=runInMenu, icon=" ", titleIcon="",
                titleColor="blue")

