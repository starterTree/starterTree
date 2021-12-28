#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from prompt_toolkit.shortcuts import prompt

import Plugin
from prompt_toolkit.key_binding import KeyBindings

demoDataYaml = """
cmdDemoData:
  cmd:
    cmd1:
      cmd: ls
      tags: ["cmd","test"]
    cmd2:
      cmd: echo "coco"
      prompt: yes
"""

bindings = KeyBindings()


@bindings.add('c-c')
def _(event):
    # " Exit when `c-x` is pressed. "
    event.app.exit()


def register(args):
    if "prompt" in args["configDict"]:
        args["element"]["prompt"] = args["configDict"]["prompt"]


def runInMenu(args):
    cmd = args["objet"]["cmd"]
    if "prompt" in args["objet"] and args["objet"]["prompt"] not in ["No", "no", "NO", "False", "false", "FALSE", "0"]:
        cmd = prompt("> ", default='%s' % cmd, key_bindings=bindings, )
    if cmd is not None:
        os.system(cmd)


plugin = Plugin.Plugin(namePlugin="cmd", demoDataYaml=demoDataYaml, afterRegister=register, runInMenu=runInMenu, icon=" ",
                titleIcon="")
