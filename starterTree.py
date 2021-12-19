#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO voir rempacer icon par entree ? ou/et sinon incruster icone > (ou toutes icons ?) dans le parseur


# load Plugins

from plugins.Plugin import pluginsA
from modules.loadData import loadData
from modules.mainPrompt import execMainPromptSession
from modules.bottomToolbar import getBottomToolbar
from modules.bottomToolbar import getToolbar

from sys import exit
import os
import sys
import time
import yaml
import json
import requests
import re
from prompt_toolkit.shortcuts import CompleteStyle,prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import themes.green
import themes.grey
#from modules.output.textable import Tableau as Tableau
from shlex import quote 
import plugins.Plugin
import datetime
#import base64
#import paramiko
#import colorama 

from rich.pretty import pprint

from modules.output.rich import Tableau as Tableau

import modules.downloadWebContent
#modules=["modules.downloadWebContent","modules.ssh","modules.openWWW"]
modulesList=[modules.downloadWebContent]


listIcon=[]

#    listIcon=['','','','','','','','']

#from module.test import add



path_entry_name_content={}
path_entry_name_content_cmd={}
keyword_file_content_relative="file_content_relative"
keyword_web_content="web_content"
keyword_gitlab_content_code_prompt_token="gitlab_api_content_prompt_token"
keyword_github_content_code_prompt_token="github_api_content_prompt_token"
ssh_module_keyword="ssh"
#modules=""
#style=Style.from_dict({Token.RPrompt: 'bg:#ff0066 #ffffff',})
settings={}
#style=Style.from_dict(settings)

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


				




def getIcon(icon,defaultIcon=""):
	if detectNerdFont:
		return icon
	return defaultIcon


#print(type(text))
def getPromptText():
	icon="search > ssh_cmd >"
	if detectNerdFont : icon = "     "
	history = FileHistory(tmpDir+".history_ssh_cmd")
	session = PromptSession("\n"+icon+" ",style=style,key_bindings=bindings,history=history)
	prompt= session.prompt(default="",rprompt=None)
	#prompt= prompt.replace('"','')
	prompt=prompt.encode('ascii',errors='ignore').decode()
	return prompt

def ssh_cmd(result):
	promptT= getPromptText()
	for r in result :
		if ssh_module_keyword in path_entry_name_content[r]:
		#	tableau=Tableau(['N°','Path','Name','Type','Tags'],detectNerdFont)	
		#	setNoneForValue(path_entry_name_content[r],["type","tags"])
		#	tableau.add_row([path_entry_name_content[r]["tmp_id"],path_entry_name_content[r]["path"],path_entry_name_content[r]["name"],path_entry_name_content[r]["type"],path_entry_name_content[r]["tags"]])
		#	print()
			#tableau.draw(icon+" "+prompt)
			os.system("ssh "+path_entry_name_content[r][ssh_module_keyword]+ " "+quote(promptT))
	ssh_cmd(result)	
def getTag(result):
	myComplete={}
	myCompleteL=[]
	for r in result:
		if "tags" in path_entry_name_content[r]:
			if type(path_entry_name_content[r]["tags"]) == list:
				for i in path_entry_name_content[r]["tags"]:
					myComplete[i]={}	
	for i in myComplete:
		myCompleteL.append(i)	
	#promptT = getPromptText()

	completer=FuzzyCompleter(WordCompleter(myCompleteL,ignore_case=True))
   
	print(myCompleteL)
	icon="search > tag >"
	if detectNerdFont : icon = "   "
	session = PromptSession(icon+" ",style=style,key_bindings=bindings)
	#prompt= session.prompt(pre_run=session.default_buffer.start_completion,default="",completer=completer)
	prompt= session.prompt(pre_run=session.default_buffer.start_completion,default="",completer=completer)



def setNoneForValue(tab,values):
	for i in values:
		if i not in tab: tab[i]="none"
	
	
tmpDir=os.environ['HOME']+'/.starterTree/'
if not os.path.exists(tmpDir):
	os.mkdir(tmpDir)

configDir=os.environ['HOME']+'/.config'
try:
	configFile=str(sys.argv[1])
except IndexError:
	configFile=os.environ['HOME']+'/.config/starterTree/config.yml'

absolute_path_main_config_file=os.path.dirname(configFile)+"/"

promptTitle=os.path.basename(sys.argv[0])
if promptTitle == "starterTree.py":
	promptTitle = ""



def main():
	# charge data ( data yaml from plugins and data yaml file or data yaml plugins and data demo)
	path_entry_name_content={}
	menu_completion={}
	style={}

	path_entry_name_content, menu_completion, style = loadData(
		pluginsA,
		configFile,
		path_entry_name_content,
		menu_completion,
		style=style)
	execMainPromptSession(
		tmpDir=tmpDir,
		promptTitle=promptTitle,
		bottomToolbar=getToolbar(pluginsA,path_entry_name_content),
		menu_completion=menu_completion,
		path_entry_name_content=path_entry_name_content,
		plugins=pluginsA)



from rich.panel import Panel
from rich import box



if __name__ == "__main__":
	#style=settings["theme"]
	main()

exit()
