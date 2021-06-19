#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit

import os
import sys

import yaml
import pprint
import json
from prompt_toolkit.shortcuts import CompleteStyle,prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.completion import FuzzyWordCompleter,FuzzyCompleter,WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML

try:
	file_main=str(sys.argv[1])
except IndexError:
	file_main=os.environ['HOME']+'/.config/starterTree/config.yml'

path_entry_name_content={}
keyword_file_content_relative="file_content_relative"
keyword_module_cmd="cmd"
keyword_module_cmd_c="cmdP"
keyword_module_opn="opn"
keyword_module_ssh="ssh"
modules=""
absolute_path_main_config_file=os.path.dirname(file_main)+"/"
def my_fun(source_dict,menu_completion,path_entry_name):
	for key in source_dict:
		path_entry_name_content["path_"+path_entry_name+key]={}
		if keyword_file_content_relative in source_dict[key]:
			menu_completion[key]={}
			my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][keyword_file_content_relative], 'r'),Loader=yaml.SafeLoader),menu_completion[key],path_entry_name+key)

		for subKey in source_dict[key]:
			print(subKey)
			if not isinstance(source_dict[key][subKey],dict):
				icon=""
				if subKey == keyword_module_opn:
					icon=""
				if subKey == keyword_module_ssh:
					icon=""
				path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
				print(subKey)
				menu_completion[key+icon]=None
			
			if isinstance(source_dict[key][subKey], dict):
				menu_completion[key]={}
				my_fun(source_dict[key], menu_completion[key] ,path_entry_name+key)
				
menu_completion={}
my_fun(yaml.load(open(file_main, 'r'),Loader=yaml.SafeLoader),menu_completion,"")

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(menu_completion))

bindings = KeyBindings()

print(json.dumps(path_entry_name_content, sort_keys=False, indent=4))

@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()

def main():
	session = PromptSession(os.path.basename(sys.argv[0])+u" > ", completer=completer, mouse_support=True, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,).replace(" ","")
	except:
		exit()
	prompt_id="path_"+prompt_id 
	if  prompt_id in path_entry_name_content:  
		if keyword_module_opn in path_entry_name_content[prompt_id]:
			text = "xdg-open "+path_entry_name_content[prompt_id][keyword_module_opn]
			os.system(text)   
			with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
				myfile.write(text+' # '+prompt_id+'\n')
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
				myfile.write(text+' # '+prompt_id+'\n')


	else:
            print("ERR: entry not found")

if __name__ == "__main__":
    main()

exit()
