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

from os.path import expanduser

#file_main=expanduser("~")+'/.az/config.yml'
try:
	file_main=str(sys.argv[1])
except IndexError:
	file_main=os.environ['HOME']+'/.config/az/config.yml'

#path_ln='/usr/local/bin/az'


# create or update symlink to script
#if os.path.islink(sys.argv[0]) == False:
#	if os.path.exists(path_ln) == True:
#		os.remove(path_ln)
#	os.symlink(os.path.abspath(sys.argv[0]),path_ln)

_dest={}
_type={}
DEBUG=[]
sign=("")
keyword_file_content=sign+"file_content"
keyword_content=sign+"content"
keyword_module_cmd="cmd"
modules=""
absolute_source=os.path.dirname(file_main)+"/"
keywords=(keyword_module_cmd,keyword_file_content,keyword_content)

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
			
		if keyword_file_content in source[i]:
			dest[i]={}
			path_file_content=source[i][keyword_file_content]
			my_fun(yaml.load(open(absolute_source+source[i][keyword_file_content], 'r'),Loader=yaml.SafeLoader),dest[i],path_object+i,esp)

#		if 	keyword_content in source[i]:
#			dest[i]={}
#			my_fun(source[i][keyword_content], dest[i] ,path_object+i,esp)

		test={}
		test[i]={}
		for a in source[i]:
			if isinstance(source[i][a], dict):
				test[i][a]={}
				test[i][a]=source[i][a]	
				dest[i]={}
				my_fun(test[i], dest[i] ,path_object+i,esp)
				
my_fun(yaml.load(open(file_main, 'r'),Loader=yaml.SafeLoader),_dest,"","")
if 1 == 2:
	for i in DEBUG:
		print(i)

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(_dest))

from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
bindings = KeyBindings()

from datetime import datetime

today=datetime.now()
print(str(today)+"a")
global prompt_id

@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()
def bottom_toolbar():
	try:
		return HTML(prompt_id+str(datetime.now())+'This is a <b><style bg="ansired">Toolbar</style></b>!')
	except:
		return HTML(str(datetime.now())+"NONE")

def main():
	session = PromptSession(u"> ", completer=completer, mouse_support=True, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,bottom_toolbar=bottom_toolbar,).replace(" ","")
	except:
		exit()
	if  prompt_id in _type:  
		if keyword_module_cmd in _type[prompt_id]:
			#print(_type[prompt_id])
			text = _type[prompt_id][keyword_module_cmd]
			if  sign+"direct" not in _type[prompt_id]:
				text = prompt(">", default='%s' % text,key_bindings=bindings,bottom_toolbar=bottom_toolbar)
			if text is None:
				exit()
			os.system(text)
			with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
				myfile.write(text+' # '+prompt_id+'\n')
                    #myfile.write('az\n'+text+' # '+prompt_id+'\n')
	    	#os.system('echo "'+text+' #'+prompt_id+'"'+ '>> ~/.bash_history')    
                #bash -c 'history -a ; echo aaFFFFFFaaaaaaaaaaaaZZZaaa >> ~/.bash_history ; history -r ~/.bash_history'
	else:
		print("AZ: entry not found")


if __name__ == "__main__":
    main()

exit()
