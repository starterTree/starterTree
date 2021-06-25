#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit

import os
import sys

import yaml
import pprint
import json
import requests
from prompt_toolkit.shortcuts import CompleteStyle,prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.completion import FuzzyWordCompleter,FuzzyCompleter,WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML


listIcon=[]
detectNerdFont= False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont= True
    listIcon=['','','','','','','']


#from module.test import add



tmpDir=os.environ['HOME']+'/.starterTree/'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)

configDir=os.environ['HOME']+'/.config'
try:
	file_main=str(sys.argv[1])
except IndexError:
	file_main=os.environ['HOME']+'/.config/starterTree/config.yml'

path_entry_name_content={}
keyword_file_content_relative="file_content_relative"
keyword_web_content="web_content"
keyword_gitlab_content_code_prompt_token="gitlab_api_content_prompt_token"
keyword_module_cmd="cmd"
keyword_module_cmd_c="cmdP"
keyword_module_opn="www"
keyword_module_ssh="ssh"
modules=""
absolute_path_main_config_file=os.path.dirname(file_main)+"/"
def downloadFromGitlabWithPromptToken(url):
	token=prompt('token like ezzfegzgezcH: ', is_password=True)
	r = requests.get(url, headers={'PRIVATE-TOKEN':token})
	rep='\n'.join(r.json()["content"].split('\n')[1:])
	with open(tmpDir+os.path.basename(url),"w") as f:
		f.write(rep)


def downloadFromUrl(url):
	r = requests.get(url)
	with open(tmpDir+os.path.basename(url),"w") as f:
		f.write(r.text)
def my_fun(source_dict,menu_completion,path_entry_name):
	for key in source_dict:
		path_entry_name_content["path_"+path_entry_name+key]={}
		#path_entry_name_content["path_"+path_entry_name+key]=source_dict[key]

		for subKey in source_dict[key]:
			icon=""
			if not isinstance(source_dict[key][subKey],dict):
				path_entry_name_content["path_"+path_entry_name+key+"--show"]={}
				path_entry_name_content["path_"+path_entry_name+key+"--show"]["show"]=source_dict[key]
				if subKey == keyword_file_content_relative:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]={}
					my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)
				if subKey == keyword_web_content:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key+"--pull"]={}
					path_entry_name_content["path_"+path_entry_name+key+"--pull"][subKey]=source_dict[key][subKey]
					if not os.path.exists(tmpDir+os.path.basename(source_dict[key][subKey])):
						#os.system("curl -L -o "+tmpDir+os.path.basename(source_dict[key][subKey])+" "+source_dict[key][subKey])
						downloadFromUrl(source_dict[key][subKey])
					menu_completion[icon+key]={}
					my_fun(yaml.load(open(tmpDir+os.path.basename(source_dict[key][subKey]), 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)
				if subKey == keyword_gitlab_content_code_prompt_token:	
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key+"--pull"]={}
					path_entry_name_content["path_"+path_entry_name+key+"--pull"][subKey]=source_dict[key][subKey]
					if not os.path.exists(tmpDir+os.path.basename(source_dict[key][subKey])):
						downloadFromGitlabWithPromptToken(source_dict[key][subKey])
					menu_completion[icon+key]={}
					my_fun(yaml.load(open(tmpDir+os.path.basename(source_dict[key][subKey]), 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)
				
				if subKey == keyword_module_opn:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				if subKey == keyword_module_ssh:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				if subKey == keyword_module_cmd:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				if subKey == keyword_module_cmd_c:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				#if subKey == keyword_file_content_relative:
					#my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)
					
				
			if isinstance(source_dict[key][subKey], dict):
				if detectNerdFont: icon=""
				menu_completion[icon+key]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"][subKey]=source_dict[key]
				my_fun(source_dict[key], menu_completion[icon+key] ,path_entry_name+key)
				
menu_completion={}
my_fun(yaml.load(open(file_main, 'r'),Loader=yaml.SafeLoader),menu_completion,"")

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(menu_completion))

bindings = KeyBindings()


@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()

def main():
	session = PromptSession(os.path.basename(sys.argv[0])+u" > ", completer=completer, mouse_support=True, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,).replace(" ","")
		historyName=prompt_id
		for i in prompt_id:
			if i in listIcon:
				prompt_id=prompt_id.replace(i,"")
	except:
		exit()
	if prompt_id == "--version":
		print("version is git rev-parse HEAD hash")
		exit()
	if prompt_id == "--debug_config":
		print(json.dumps(path_entry_name_content, sort_keys=False, indent=4))
		exit()
	if prompt_id == "--debug_completion":
		print(json.dumps(menu_completion, sort_keys=False, indent=4))
		exit()
	if prompt_id.split('=')[0] == "--update":
		if len(prompt_id.split('=')) == 2:
			#download /0.2/
			os.system("cd /opt ; sudo curl -L 'https://github.com/thomas10-10/starterTree/releases/download/"+prompt_id.split('=')[1]+"/starterTree.tar.gz' | sudo tar -xz")   
		else:
			os.system("cd /opt ; sudo curl -L 'https://github.com/thomas10-10/starterTree/releases/download/last/starterTree.tar.gz' | sudo tar -xz")   
			#download last
		#if part2 == none
		#then update laste comit
		#or 
		#==V2 download v2
		exit()

	prompt_id="path_"+prompt_id 
	if  prompt_id in path_entry_name_content:
		text=prompt_id 
		if "show" in path_entry_name_content[prompt_id]:
			print(path_entry_name_content[prompt_id]["show"])
		if keyword_web_content in path_entry_name_content[prompt_id]:
			downloadFromUrl(path_entry_name_content[prompt_id][keyword_web_content])
		if keyword_gitlab_content_code_prompt_token in path_entry_name_content[prompt_id]:
			downloadFromGitlabWithPromptToken(path_entry_name_content[prompt_id][keyword_gitlab_content_code_prompt_token])
		if keyword_module_ssh in path_entry_name_content[prompt_id]:
			text = "ssh "+path_entry_name_content[prompt_id][keyword_module_ssh]
			os.system(text)   
		if keyword_module_opn in path_entry_name_content[prompt_id]:
			text = "xdg-open "+path_entry_name_content[prompt_id][keyword_module_opn]
			os.system(text)   
		if keyword_module_cmd in path_entry_name_content[prompt_id] or keyword_module_cmd_c in path_entry_name_content[prompt_id]:
			if  keyword_module_cmd_c in path_entry_name_content[prompt_id]:
				text = path_entry_name_content[prompt_id][keyword_module_cmd_c]
				text = prompt(">", default='%s' % text,key_bindings=bindings,)
			else:
				text = path_entry_name_content[prompt_id][keyword_module_cmd]
			if text is None:
				exit()
			os.system(text)
		
		with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
			myfile.write(text+' # '+historyName+'\n')


	else:
	    print("ERR: entry not found")

if __name__ == "__main__":
    main()

exit()
