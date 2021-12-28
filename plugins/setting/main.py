#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from rich.pretty import pprint


dataYaml = """
settings:
  icon: ""
  description: display debug information and update
  tags: ["settings"]
#  test:
#    setting:
#      starterTree_title: bo
  config:
    setting: config
    starterTree_title: starterTree
    starterTree_theme: grey
    #starterTree_disableIcon: yes
  update:
    icon: "⠀"
    setting: update
    description: by default update to new version, add `--v0.14f` to downlad precise version
  version:
    icon: "⠀"
    setting: version
    description: show version
  debug:
    completion:
      setting: completion
      description: show completion dict
    config:
      setting: config
      description: show config dict
"""

def runInMenu(args):
    stDict = args["objet"]
    menuCompletion = args["menuCompletion"]
    pathEntry = args["pathEntry"]
    if stDict["setting"] == "version":
        print("version is git rev-parse HEAD hash")
    if stDict["setting"] == "completion":
        pprint(args["data"]["menu_completion"])
        # print(json.dumps(menu_completion, sort_keys=False, indent=4))
    if stDict["setting"] == "config":
        pprint(args["data"]["path_"])
        # print(json.dumps(path_entry_name_content, sort_keys=False, indent=4))
    if stDict["setting"] == "update":
        if option != None:
            pprint("download specific version")
            os.system(
                "cd /opt ; sudo curl -L 'https://github.com/thomas10-10/starterTree/releases/download/" + option + "/starterTree.tar.gz' | sudo tar -xz")
        else:
            os.system(
                'cd /opt ; sudo curl -L "https://github.com/thomas10-10/starterTree/releases/download/$(basename $(curl -fsSLI -o /dev/null -w %{url_effective} https://github.com/thomas10-10/starterTree/releases/latest))/starterTree.tar.gz" | sudo tar -xz')


from Plugin import Plugin

plugin = Plugin(namePlugin="setting",  dataYaml=dataYaml, runInMenu=runInMenu, icon="⠀",titleIcon="", options=["debug"])
