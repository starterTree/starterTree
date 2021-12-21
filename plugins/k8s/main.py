#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Plugin import Plugin

import os

####
namePlugin = "k8s"

demoDataYaml = """
  kinder:
    k8s: "~/.kube/kindLocal.asc"
"""

detectNerdFont = False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont = True


def startKubectl(path_file):
    filename, file_extension = os.path.splitext(path_file)
    if file_extension == ".asc":
        os.system("gpg --batch --yes --out " + path_file + ".decrypt" + " -d " + path_file)
        path_file = path_file + ".decrypt"
    # kubectl config current-context
    os.putenv("KUBECONFIG", os.path.expanduser(path_file))
    icon = ""
    if detectNerdFont: icon = " "
    os.putenv("ST", "Kind-Kind " + icon)
    os.system("bash")
    if file_extension == ".asc":
        os.remove(os.path.expanduser(path_file))
        os.system("echo RELOADAGENT | gpg-connect-agent")


def register(args):
    configDict = args["configDict"]
    stDict = args["stDict"]
    stDict["--encrypt"] = {}
    stDict["--encrypt"]["encryptable-kube"] = configDict[namePlugin]


def runInMenu(args):
    startKubectl(args["objet"][namePlugin])


plugin = Plugin(namePlugin=namePlugin, demoDataYaml=demoDataYaml, afterRegister=register, runInMenu=runInMenu,
                icon=" ", titleIcon="")
