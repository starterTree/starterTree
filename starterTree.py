#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO voir rempacer icon par entree ? ou/et sinon incruster icone > (ou toutes icons ?) dans le parseur
from sys import exit
import os
import sys
import time
import yaml
import json
import requests
import re
from prompt_toolkit.shortcuts import CompleteStyle,prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.completion import FuzzyWordCompleter,FuzzyCompleter,WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.application import run_in_terminal,get_app_or_none
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML,merge_formatted_text
import themes.green
import themes.grey
#from modules.output.textable import Tableau as Tableau
from shlex import quote 
from prompt_toolkit.history import FileHistory
from rich.console import Console
from jinja2 import Template
import plugins.Plugin
from modules.utils import my_fun 
#import base64
#import paramiko
#import colorama 

from rich.pretty import pprint

from modules.output.rich import Tableau as Tableau

import modules.downloadWebContent
#modules=["modules.downloadWebContent","modules.ssh","modules.openWWW"]
modulesList=[modules.downloadWebContent]


listIcon=[]
detectNerdFont= False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont= True
#    listIcon=['','','','','','','','']

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
path_entry_name_content_cmd={}
keyword_file_content_relative="file_content_relative"
keyword_web_content="web_content"
keyword_gitlab_content_code_prompt_token="gitlab_api_content_prompt_token"
keyword_github_content_code_prompt_token="github_api_content_prompt_token"
ssh_module_keyword="ssh"
#modules=""
absolute_path_main_config_file=os.path.dirname(file_main)+"/"
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

def tags(key):
	#for i in path_entry_name_content["path_"+path_entry_name+keya]["tags"]:
	#	print("hey",i.split(key))
	#	if len(i.split(key)) == 2:
	#		return i.split(key)[1]
	return "fuckyek"



				
menu_completion={}

def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    return yaml.load(template.render(),Loader=yaml.SafeLoader)



dataDemo={}
dataYaml={}

for m in plugins.Plugin.pluginsActivated:
    dataDemoModules={}
    dataModules={}

    dataDemoModules=yaml.load(plugins.Plugin.pluginsActivated[m].getDemoDataYaml(),Loader=yaml.SafeLoader)
    dataModules=yaml.load(plugins.Plugin.pluginsActivated[m].getDataYaml(),Loader=yaml.SafeLoader)

    dataYaml = {**dataYaml , **dataModules }
    dataDemo = {**dataDemo , **dataDemoModules }
_plugins=plugins.Plugin.pluginsActivated
if os.getenv("ST_DEMO") == '1' : 
    for data in [dataYaml,dataDemo]:
        my_fun(source_dict=data,menu_completion=menu_completion,path_entry_name_content=path_entry_name_content,path_entry_name="",path_entry_name_path="",plugins=_plugins,tab="\t",settings=settings)
else :
    for data in [dataYaml,jinjaFile2yaml(file_main)]:
        my_fun(source_dict=data ,menu_completion=menu_completion ,path_entry_name_content=path_entry_name_content, path_entry_name="", path_entry_name_path="", plugins=_plugins,tab="\t",settings=settings)

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(menu_completion))

def getIcon(icon,defaultIcon=""):
    if detectNerdFont:
        return icon
    return defaultIcon

bindings = KeyBindings()
@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()


#print(type(text))
def get_toolbar():
	result=get_rprompt()	
	with console.capture() as capture:
	    #grid =Table(expand=False, box=box.SQUARE,show_header=False,show_edge=False,padding=(0,0))
	    grid =Table(expand=False, box=None,show_header=False,show_edge=False,padding=(0,0))
	    text="""   ____ __ 
  / __// /_ 
 _\ \ / __/ 
/___/ \__/
"""
#_\ \ / __/ [#444444 on green][link="https://github.com/starterTree/starterTree"]Github[/link][/#444444 on green]
	    text2="""
███████ ████████ 
██         ██    
███████    ██    
     ██    ██    
███████    ██"""   
	    grid.add_column(style="#444444")
	    #grid.add_column(style="green on purple")
	    grid.add_row("[bold  on red]"+text+"[/bold  on red]", result)
	    #grid.add_row("[bold #444444 on red]"+text2+"[/bold #444444 on red]", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
	    console.print(grid)
	str_output = capture.get()

	#return "Bottom toolbar: time=%r" % time.time()
	#if result == "":
	#    return ""
	return ANSI(str_output[:-1])


def get_rprompt():
	#text=re.sub(r' .',''," "+text)
	#text=text.encode('ascii',errors='ignore').decode()
	text=get_app_or_none().current_buffer.text.replace(" ","")
	text=text.encode('ascii',errors='ignore').decode()
	for i in text:
			if i in listIcon:
				pass
				#text=text.replace(i,"")
	text='path_'+text
	if text in path_entry_name_content:
		result=''
		for i in plugins.Plugin.pluginsActivated:
			if i in path_entry_name_content[text]:
				result=plugins.Plugin.pluginsActivated[i].getContentForRprompt(stDict=path_entry_name_content[text])

		#return HTML('<aaa fg="white" bg="#008888">'+str(result)+'</aaa>')
		#return merge_formatted_text([HTML('<aaa style="bold" fg="white" bg="#444444">'+"'"+str(result)+"'"+'</aaa>'),"dd"])
		return result
		#return [(Token, ' '),(Token.RPrompt, str(result)),]
	else:
		return('')
	#return HTML(get_app_or_none().current_buffer.text)
import datetime
def mainPrompt(title) ->HTML:
	icon=" >"
	#version=""
	version="version is version"
	#str(datetime.datetime.now())
	if detectNerdFont: icon=" " #icon=getIcon(""," >")
	caseVersion=HTML('<aaa style="" fg="red" bg="#444444"> '+str(version)+'</aaa>')
	promptUser=HTML('<aaa style="" fg="white" bg="#444444"> '+str(title+icon)+' </aaa>')
	return merge_formatted_text([caseVersion,promptUser," "])

def getPromptText():
	icon="search > ssh_cmd >"
	if detectNerdFont : icon = "     "
	history = FileHistory(tmpDir+".history_ssh_cmd")
	session = PromptSession("\n"+icon+" ",style=style,key_bindings=bindings,history=history)
	#prompt= session.prompt(pre_run=session.default_buffer.start_completion,default="",rprompt=get_rprompt)
	prompt= session.prompt(default="",rprompt=get_rprompt)
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
	

	

def main():
	history = FileHistory(tmpDir+".history_main")
	session = PromptSession(mainPrompt(promptTitle), completer=completer, mouse_support=False,style=style, history=history, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		#prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,rprompt=get_rprompt,default="").replace(" ","")
		prompt_id=session.prompt(placeholder="press space to use completion or up to use history",rprompt=None,bottom_toolbar=get_toolbar,default="").replace(" ","")
		historyName=prompt_id
		prompt_id=prompt_id.encode('ascii',errors='ignore').decode()
		for i in prompt_id:
			if i in listIcon:
				pass
				#prompt_id=prompt_id.replace(i,"")
	except:
		#print("error")
		exit()

	prompt_id="path_"+prompt_id 
	if  prompt_id in path_entry_name_content_cmd:
		if "encryptable" in path_entry_name_content_cmd[prompt_id]:
			os.system("cat "+tmpDir+os.path.basename(path_entry_name_content_cmd[prompt_id]["encryptable"])+" | gpg -a --cipher-algo AES256 -c")			
		if "encryptable-kube" in path_entry_name_content_cmd[prompt_id]:
			os.system("cat "+os.path.basename(path_entry_name_content_cmd[prompt_id]["encryptable-kube"])+" | gpg -a --cipher-algo AES256 -c")			

		if keyword_web_content in path_entry_name_content_cmd[prompt_id]:
			modules.downloadWebContent.launch(path_entry_name_content=path_entry_name_content,prompt_id=prompt_id,keyword_web_content=keyword_web_content,tmpDir=tmpDir)
			#downloadFromUrl(path_entry_name_content[prompt_id.replace("--pull","")][keyword_web_content])
		if keyword_gitlab_content_code_prompt_token in path_entry_name_content_cmd[prompt_id]:
			downloadFromGitLabWithPromptToken(path_entry_name_content_cmd[prompt_id.replace("","")][keyword_gitlab_content_code_prompt_token])
		if keyword_github_content_code_prompt_token in path_entry_name_content_cmd[prompt_id]:
			downloadFromGitHubWithPromptToken(path_entry_name_content_cmd[prompt_id.replace("","")][keyword_github_content_code_prompt_token])
		exit()
	#print(prompt_id)  
	option=None
	#print(len(prompt_id.split("--")))
	if len(prompt_id.split("--")) == 2: option=prompt_id.split("--")[1]
	prompt_id=prompt_id.split("--")[0]
	if  prompt_id in path_entry_name_content:
		#print(path_entry_name_content[prompt_id])
		text=prompt_id 
		for i in plugins.Plugin.pluginsActivated:
			if i in path_entry_name_content[prompt_id]:
				plugins.Plugin.pluginsActivated[i].runInMenu(path_entry_name_content[prompt_id],option=option,menuCompletion=menu_completion,pathEntry=path_entry_name_content,style=style,tmpDir=tmpDir)

		#with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
		#	myfile.write(text+' # '+historyName+'\n')


	else:
		print("ERR: entry not found")
		main()

from rich.panel import Panel
from rich.table import Table
from rich import box

from prompt_toolkit import print_formatted_text, ANSI
console=Console()





if __name__ == "__main__":
    style=settings["theme"]
    console=Console()
    #console.rule(style="red")
    #console.print(Panel("dd"))
    main()

exit()
# nice icon ⏽
