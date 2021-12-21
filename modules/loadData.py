#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
from jinja2 import Template
from modules.utils import my_fun


def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    return yaml.load(template.render(), Loader=yaml.SafeLoader)


# _plugins=plugins.Plugin.pluginsActivated
def loadData(configFile, data):
    dataDemo = {}
    dataYaml = {}
    menu_completion = data["menu_completion"]
    settings = {}

    for p in data["plugins"]:
        dataDemoModules = {}
        dataModules = {}
        print(p.getName())
        dataDemoModules = yaml.load(
            p.getDemoDataYaml(),
            Loader=yaml.SafeLoader)
        dataModules = yaml.load(
            p.getDataYaml(),
            Loader=yaml.SafeLoader)

        dataYaml = {**dataYaml, **dataModules}
        dataDemo = {**dataDemo, **dataDemoModules}

    if os.getenv("ST_DEMO") == '1':
        for d in [dataYaml, dataDemo]:
            my_fun(source_dict=d, menu_completion=data["menu_completion"], data=data, plugins=data["plugins"])
    else:
        for d in [dataYaml, jinjaFile2yaml(configFile)]:
            my_fun(source_dict=d, menu_completion=data["menu_completion"], data=data, plugins=data["plugins"])

    return data, menu_completion
