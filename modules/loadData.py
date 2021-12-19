#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
from jinja2 import Template
from modules.utils import my_fun 

def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    return yaml.load(template.render(),Loader=yaml.SafeLoader)


#_plugins=plugins.Plugin.pluginsActivated
def loadData(plugins,configFile,path_entry_name_content,menu_completion):
    dataDemo={}
    dataYaml={}
    menu_completion=menu_completion
    settings={}

    for p in plugins:
        dataDemoModules={}
        dataModules={}

        dataDemoModules=yaml.load(
            p.getDemoDataYaml(),
            Loader=yaml.SafeLoader)  
        dataModules=yaml.load(
            p.getDataYaml(),
            Loader=yaml.SafeLoader)

        dataYaml = {**dataYaml , **dataModules }
        dataDemo = {**dataDemo , **dataDemoModules }

    if os.getenv("ST_DEMO") == '1' : 
        for data in [dataYaml,dataDemo]:
            my_fun(
                source_dict=data,menu_completion=menu_completion,
                path_entry_name_content=path_entry_name_content,path_entry_name="",  
                path_entry_name_path="",
                plugins=plugins,tab="\t",settings=settings)
    else :
        for data in [dataYaml,jinjaFile2yaml(configFile)]:
            my_fun(
                source_dict=data,
                menu_completion=menu_completion,
                path_entry_name_content=path_entry_name_content,
                path_entry_name="",
                path_entry_name_path="", 
                plugins=plugins,
                tab="\t",settings=settings)


