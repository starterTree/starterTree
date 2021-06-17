#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit

import os
import sys

import yaml
from prompt_toolkit.shortcuts import CompleteStyle,prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.completion import FuzzyWordCompleter,FuzzyCompleter,WordCompleter
from prompt_toolkit import PromptSession

try:
	file_main=str(sys.argv[1])
except IndexError:
	file_main=os.environ['HOME']+'/.config/starterTree/config.yml'

_dest={}
_type={}
DEBUG=[]
sign=("")
keyword_file_content_relative=sign+"file_content_relative"
keyword_content=sign+"content"
keyword_module_cmd="cmd"
keyword_module_cmd_c="cmdP"
modules=""
absolute_source=os.path.dirname(file_main)+"/"
keywords=(keyword_module_cmd,keyword_file_content_relative,keyword_content)

def my_fun(source,dest,path_object,tab):
	path_object=path_object+" "
	esp=tab+"   "
	_type[path_object]={}
	for i in source:
		id=path_object.replace(" ", "")+i
		dest[i]=None
		DEBUG.append(esp+"⊛"+i+"  "+"id: "+id)
		_type[id]={}
		for a in source[i]:
			if a != keyword_content:
				DEBUG.append(id+" "+a)
				_type[id][a]=source[i][a]
			else:
				DEBUG.append(esp+" "+a+":")
			
		if keyword_file_content_relative in source[i]:
			dest[i]={}
			my_fun(yaml.load(open(absolute_source+source[i][keyword_file_content_relative], 'r'),Loader=yaml.SafeLoader),dest[i],path_object+i,esp)

		test={}
		test[i]={}
		for a in source[i]:
			if isinstance(source[i][a], dict):
				test[i][a]={}
				test[i][a]=source[i][a]	
				dest[i]={}
				my_fun(test[i], dest[i] ,path_object+i,esp)
				
my_fun(yaml.load(open(file_main, 'r'),Loader=yaml.SafeLoader),_dest,"","")

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(_dest))

from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
bindings = KeyBindings()


@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()

def main():
	session = PromptSession(os.path.basename(__file__)+u" > ", completer=completer, mouse_support=True, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,).replace(" ","")
	except:
		exit()
	if  prompt_id in _type:  
		if keyword_module_cmd in _type[prompt_id] or keyword_module_cmd_c in _type[prompt_id]:
			if  keyword_module_cmd_c in _type[prompt_id]:
				text = _type[prompt_id][keyword_module_cmd_c]
				text = prompt(">", default='%s' % text,key_bindings=bindings,)
			else:
				text = _type[prompt_id][keyword_module_cmd]
			if text is None:
				exit()
			os.system(text)
			with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
				myfile.write(text+' # '+prompt_id+'\n')
	else:
		print("AZ: entry not found")

if __name__ == "__main__":
    main()

exit()
