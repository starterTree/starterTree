#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit

import os
import sys

import yaml
import pprint
import json
import requests
#from prompt_toolkit.token import Token
from prompt_toolkit.shortcuts import CompleteStyle,prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.completion import FuzzyWordCompleter,FuzzyCompleter,WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.application import run_in_terminal,get_app_or_none
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
#from prompt_toolkit.styles import style_from_dict


listIcon=[]
detectNerdFont= False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont= True
    listIcon=['','','','','','','','']


#from module.test import add



tmpDir=os.environ['HOME']+'/.starterTree/'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)

configDir=os.environ['HOME']+'/.config'
try:
	file_main=str(sys.argv[1])
except IndexError:
	file_main=os.environ['HOME']+'/.config/starterTree/config.yml'

promptTitle=os.path.basename(sys.argv[0])
if promptTitle == "starterTree.py":
    promptTitle = ""
path_entry_name_content={}
keyword_file_content_relative="file_content_relative"
keyword_web_content="web_content"
keyword_gitlab_content_code_prompt_token="gitlab_api_content_prompt_token"
keyword_github_content_code_prompt_token="github_api_content_prompt_token"
keyword_kubeconfig_file="kubeconfig_file"
keyword_module_cmd="cmd"
keyword_module_cmd_c="cmdP"
keyword_module_opn="www"
keyword_module_ssh="ssh"
modules=""
absolute_path_main_config_file=os.path.dirname(file_main)+"/"
#style=Style.from_dict({Token.RPrompt: 'bg:#ff0066 #ffffff',})
style=Style.from_dict({})

def downloadFromGitLabWithPromptToken(url):
	print(url)
	token=prompt('token like ezzfegzgezcH: ', is_password=True)
	r = requests.get(url, headers={'PRIVATE-TOKEN':token})
	rep='\n'.join(r.json()["content"].split('\n')[1:])
	with open(tmpDir+os.path.basename(url),"w") as f:
		f.write(rep)
	filename, file_extension = os.path.splitext(tmpDir+os.path.basename(url))
	if file_extension == ".asc":
		os.system("gpg --batch --yes --out "+tmpDir+os.path.basename(url)+" -d "+tmpDir+os.path.basename(url) )

def downloadFromGitHubWithPromptToken(url):
	print(url)
	token=prompt('token like ezzfegzgezcH: ', is_password=True)
	r = requests.get(url, headers={'Authorization':'token '+token,'Accept': 'application/vnd.github.v4.raw'})
	rep='\n'.join(r.text.split('\n')[1:])
	with open(tmpDir+os.path.basename(url),"w") as f:
		f.write(rep)
	filename, file_extension = os.path.splitext(tmpDir+os.path.basename(url))
	if file_extension == ".asc":
		os.system("gpg --batch --yes --out "+tmpDir+os.path.basename(url)+" -d "+tmpDir+os.path.basename(url) )

def downloadFromUrl(url):
	r = requests.get(url)
	with open(tmpDir+os.path.basename(url),"w") as f:
		f.write(r.text)
	filename, file_extension = os.path.splitext(tmpDir+os.path.basename(url))
	if file_extension == ".asc":
		os.system("gpg --batch --yes --out "+tmpDir+os.path.basename(url)+" -d "+tmpDir+os.path.basename(url) )

def startKubectl(path_file):
	filename, file_extension = os.path.splitext(path_file)
	if file_extension == ".asc":
		os.system("gpg --batch --yes --out "+path_file+".decrypt"+" -d "+path_file )
		path_file=path_file+".decrypt"
	#kubectl config current-context
	os.putenv("KUBECONFIG",os.path.expanduser(path_file))
	icon=""
	if detectNerdFont: icon=" "
	os.putenv("ST","Kind-Kind "+icon)
	os.system("bash")
	if file_extension == ".asc":
		os.remove(os.path.expanduser(path_file))
		os.system("echo RELOADAGENT | gpg-connect-agent")
def my_fun(source_dict,menu_completion,path_entry_name):
	for key in source_dict:
		path_entry_name_content["path_"+path_entry_name+key]={}
		#path_entry_name_content["path_"+path_entry_name+key]=source_dict[key]

		for subKey in source_dict[key]:
			icon=""
			if not isinstance(source_dict[key][subKey],dict):
				path_entry_name_content["path_"+path_entry_name+key+"--show"]={}
				path_entry_name_content["path_"+path_entry_name+key+"--show"]["show"]=source_dict[key]

				if subKey == "starterTree_title":
					global promptTitle
					promptTitle=source_dict[key][subKey]
				if subKey == "starterTree_theme":
					if source_dict[key][subKey] == "green":
						global style
						style = Style.from_dict({
							#Token.RPrompt: 'bg:#ff0066 #ffffff',
							#'session': 'bg:#ffffff #000000',
							'completion-menu.completion': 'bg:#008888 #ffffff',
							'completion-menu.completion.current': 'bg:#00aaaa #000000',
							'scrollbar.background': 'bg:#88aaaa',
							'scrollbar.button': 'bg:#222222',
							'prompt': '#00aaaa',
							'prompt.arg.text': '#00aaaa',
							#'prompt.arg.text': 'bg:#ffffff #00aaaa',
						})
				if subKey == keyword_kubeconfig_file:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					path_entry_name_content["path_"+path_entry_name+key+"--encrypt"]={}
					path_entry_name_content["path_"+path_entry_name+key+"--encrypt"]["encryptable-kube"]=source_dict[key][subKey]
					menu_completion[icon+key]={}

				if subKey == keyword_file_content_relative:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]={}
					my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)

				if subKey in [keyword_gitlab_content_code_prompt_token, keyword_github_content_code_prompt_token, keyword_web_content] :	
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+key+"--pull"]={}
					path_entry_name_content["path_"+path_entry_name+key+"--pull"][subKey]=source_dict[key][subKey]
					path_entry_name_content["path_"+path_entry_name+key+"--encrypt"]={}
					path_entry_name_content["path_"+path_entry_name+key+"--encrypt"]["encryptable"]=source_dict[key][subKey]
					if not os.path.exists(tmpDir+os.path.basename(source_dict[key][subKey])):
						#os.system("curl -L -o "+tmpDir+os.path.basename(source_dict[key][subKey])+" "+source_dict[key][subKey])
						if subKey == keyword_gitlab_content_code_prompt_token: downloadFromGitLabWithPromptToken(source_dict[key][subKey])
						if subKey == keyword_github_content_code_prompt_token: downloadFromGitHubWithPromptToken(source_dict[key][subKey])
						if subKey == keyword_web_content: downloadFromUrl(source_dict[key][subKey])
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
				menu_completion[icon+key+""]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"][subKey]=source_dict[key]
				my_fun(source_dict[key], menu_completion[icon+key+""] ,path_entry_name+key)
				
menu_completion={}
my_fun(yaml.load(open(file_main, 'r'),Loader=yaml.SafeLoader),menu_completion,"")

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(menu_completion))

bindings = KeyBindings()


@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()


def get_rprompt():
	text=get_app_or_none().current_buffer.text.replace(" ","")
	for i in text:
			if i in listIcon:
				text=text.replace(i,"")
	text='path_'+text
	if text in path_entry_name_content:
		result=path_entry_name_content[text]
		#return HTML('<aaa fg="white" bg="#008888">'+str(result)+'</aaa>')
		return HTML('<aaa fg="black" bg="white">'+str(result)+'</aaa>')
		#return [(Token, ' '),(Token.RPrompt, str(result)),]
	else:
		return('')
	#return HTML(get_app_or_none().current_buffer.text)




def main():
	session = PromptSession(promptTitle+u" > ", completer=completer, mouse_support=True,style=style, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,rprompt=get_rprompt).replace(" ","")
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
			os.system('cd /opt ; sudo curl -L "https://github.com/thomas10-10/starterTree/releases/download/$(basename $(curl -fsSLI -o /dev/null -w %{url_effective} https://github.com/thomas10-10/starterTree/releases/latest))/starterTree.tar.gz" | sudo tar -xz')   
			#download last
		#if part2 == none
		#then update laste comit
		#or 
		#==V2 download v2
		exit()

	prompt_id="path_"+prompt_id 
	if  prompt_id in path_entry_name_content:
		text=prompt_id 
		if keyword_kubeconfig_file in path_entry_name_content[prompt_id]:
			startKubectl(path_entry_name_content[prompt_id][keyword_kubeconfig_file])
		if "show" in path_entry_name_content[prompt_id]:
			print(path_entry_name_content[prompt_id]["show"])
		if "encryptable" in path_entry_name_content[prompt_id]:
			os.system("cat "+tmpDir+os.path.basename(path_entry_name_content[prompt_id]["encryptable"])+" | gpg -a --cipher-algo AES256 -c")			
		if "encryptable-kube" in path_entry_name_content[prompt_id]:
			os.system("cat "+os.path.expanduser(path_entry_name_content[prompt_id]["encryptable-kube"])+" | gpg -a --cipher-algo AES256 -c")			
		if keyword_web_content in path_entry_name_content[prompt_id]:
			downloadFromUrl(path_entry_name_content[prompt_id][keyword_web_content])
		if keyword_gitlab_content_code_prompt_token in path_entry_name_content[prompt_id]:
			downloadFromGitLabWithPromptToken(path_entry_name_content[prompt_id][keyword_gitlab_content_code_prompt_token])
		if keyword_github_content_code_prompt_token in path_entry_name_content[prompt_id]:
			downloadFromGitHubWithPromptToken(path_entry_name_content[prompt_id][keyword_github_content_code_prompt_token])
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
