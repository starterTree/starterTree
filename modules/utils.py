#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
keyword_file_content_relative="file_content_relative"
keyword_web_content="web_content"
keyword_gitlab_content_code_prompt_token="gitlab_api_content_prompt_token"
keyword_github_content_code_prompt_token="github_api_content_prompt_token"
www_module_keyword="www"
ssh_module_keyword="ssh"

from rich.pretty import pprint
import yaml
from prompt_toolkit.styles import Style

from jinja2 import Template
detectNerdFont= False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont= True

def getIcon(icon,defaultIcon=""):
    if detectNerdFont:
        return icon
    return defaultIcon

tmpDir=os.environ['HOME']+'/.starterTree/'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)

def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    return yaml.load(template.render(),Loader=yaml.SafeLoader)




def my_fun(source_dict,menu_completion,path_entry_name_content,path_entry_name,path_entry_name_path,plugins,tab,settings):
	for key in source_dict:
		key=key.encode('ascii',errors='ignore').decode().replace(" ","⠀")
		path_entry_name_content["path_"+path_entry_name+key]={}

		icon=""
		#cas specifique
		if not isinstance(source_dict[key],dict):
				#Register Plugins
			if key in plugins:
				plugins[key].register(configDict=source_dict,stDict=path_entry_name_content["path_"+path_entry_name+key],menuDict=menu_completion,key=key,menu=menu_completion,path=path_entry_name_path+"/",settings=settings)	

			
		if isinstance(source_dict[key], dict):
			if detectNerdFont: icon=""
			if "icon" in source_dict[key] and detectNerdFont:
				icon=source_dict[key]["icon"]
			count=0
			bad=0
			sub_e=""
			for sub in source_dict[key]:
				if sub in plugins:
					count=count+1
					sub_e=sub
				if isinstance(source_dict[key][sub],dict):
					bad=1
			#un sous dossier qui contient une seule entree classique
			if bad == 0 and count == 1:
				if sub_e in plugins:
					plugins[sub_e].register(configDict=source_dict[key],stDict=path_entry_name_content["path_"+path_entry_name+key],menuDict=menu_completion,key=key,menu=menu_completion,path=path_entry_name_path+"/",settings=settings)	
			
			# alors cest un sous dossier
			else:
				key_menu_completion=(icon+key).replace(" ","⠀")
				menu_completion[key_menu_completion]={}
				menu_completion[key_menu_completion]["--list"]={}
				my_fun(source_dict=source_dict[key], menu_completion=menu_completion[key_menu_completion] ,path_entry_name_content=path_entry_name_content ,path_entry_name=path_entry_name+key, path_entry_name_path=path_entry_name_path+"/"+key,plugins=plugins,tab=tab+"\t"+"\t",settings=settings)

