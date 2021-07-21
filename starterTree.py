#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO voir rempacer icon par entree ? ou/et sinon incruster icone > (ou toutes icons ?) dans le parseur
from sys import exit
#import texttable
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
import texttable as tt
import themes.green
import themes.grey
import modules.downloadWebContent
import modules.openWWW
import modules.ssh
from shlex import quote 
from prompt_toolkit.history import FileHistory
#import colorama 

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
path_entry_name_content_cmd={}
keyword_file_content_relative="file_content_relative"
keyword_web_content="web_content"
keyword_gitlab_content_code_prompt_token="gitlab_api_content_prompt_token"
keyword_github_content_code_prompt_token="github_api_content_prompt_token"
keyword_kubeconfig_file="kubeconfig_file"
keyword_module_cmd="cmd"
keyword_module_cmd_c="cmdP"
www_module_keyword="www"
ssh_module_keyword="ssh"
#modules=""
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
	os.putenv("KUBECONFIG",os.path.version is versionanduser(path_file))
	icon=""
	if detectNerdFont: icon=" "
	os.putenv("ST","Kind-Kind "+icon)
	os.system("bash")
	if file_extension == ".asc":
		os.remove(os.path.version is versionanduser(path_file))
		os.system("echo RELOADAGENT | gpg-connect-agent")
def my_fun(source_dict,menu_completion,path_entry_name,path_entry_name_path):
	for key in source_dict:
		keya=key.encode('ascii',errors='ignore').decode()

		path_entry_name_content["path_"+path_entry_name+keya]={}
		#path_entry_name_content["path_"+path_entry_name+key]=source_dict[key]

		for subKey in source_dict[key]:
			icon=""
			if not isinstance(source_dict[key][subKey],dict):
				path_entry_name_content["path_"+path_entry_name+keya]["path"]=path_entry_name_path+"/"
				path_entry_name_content["path_"+path_entry_name+keya]["name"]=keya
				path_entry_name_content["path_"+path_entry_name+keya]["tags"]={}
				path_entry_name_content_cmd["path_"+path_entry_name+keya+"--show"]={}
				path_entry_name_content_cmd["path_"+path_entry_name+keya+"--show"]["show"]={}
				if subKey == "starterTree_disableIcon":
					global detectNerdFont
					detectNerdFont= False
				if subKey == "starterTree_title":
					global promptTitle
					promptTitle=source_dict[key][subKey]
				if subKey == "starterTree_theme":
					global style
					if source_dict[key][subKey] == "green": style = Style.from_dict(themes.green.completionMenu)
					if source_dict[key][subKey] == "grey":  style = Style.from_dict(themes.grey.completionMenu)
				
				if subKey == "tags":
					path_entry_name_content["path_"+path_entry_name+keya]["tags"]=source_dict[key][subKey]
				if subKey == keyword_kubeconfig_file:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]={}
					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]["encryptable-kube"]=source_dict[key][subKey]
					menu_completion[icon+key]={}

				if subKey == keyword_file_content_relative:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]={}
					my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)

				if subKey in [keyword_gitlab_content_code_prompt_token, keyword_github_content_code_prompt_token, keyword_web_content] :	
					if detectNerdFont: icon=""
					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--pull"]={}
					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--pull"][subKey]=source_dict[key][subKey]
					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]={}
					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]["encryptable"]=source_dict[key][subKey]
					if not os.path.exists(tmpDir+os.path.basename(source_dict[key][subKey])):
						#os.system("curl -L -o "+tmpDir+os.path.basename(source_dict[key][subKey])+" "+source_dict[key][subKey])
						if subKey == keyword_gitlab_content_code_prompt_token: downloadFromGitLabWithPromptToken(source_dict[key][subKey])
						if subKey == keyword_github_content_code_prompt_token: downloadFromGitHubWithPromptToken(source_dict[key][subKey])
						if subKey == keyword_web_content: downloadFromUrl(source_dict[key][subKey])
					menu_completion[icon+key]={}
					my_fun(yaml.load(open(tmpDir+os.path.basename(source_dict[key][subKey]), 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)
				
				if subKey == www_module_keyword:
					path_entry_name_content["path_"+path_entry_name+keya]["type"]=subKey
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				if subKey == ssh_module_keyword:
					path_entry_name_content["path_"+path_entry_name+keya]["type"]=subKey
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				if subKey == keyword_module_cmd:
					path_entry_name_content["path_"+path_entry_name+keya]["type"]=subKey
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				if subKey == keyword_module_cmd_c:
					path_entry_name_content["path_"+path_entry_name+keya]["type"]=subKey
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]=None
				#if subKey == keyword_file_content_relative:
					#my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)
					
				
			if isinstance(source_dict[key][subKey], dict):
				if detectNerdFont: icon=""
				menu_completion[icon+key+""]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"][subKey]=source_dict[key]
				my_fun(source_dict[key], menu_completion[icon+key+""] ,path_entry_name+keya,path_entry_name_path+"/"+keya)
				#del path_entry_name_content["path_"+path_entry_name+keya]
				
menu_completion={}
my_fun(yaml.load(open(file_main, 'r'),Loader=yaml.SafeLoader),menu_completion,"","")

completer =  FuzzyCompleter(NestedCompleter.from_nested_dict(menu_completion))

bindings = KeyBindings()


@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()


#print(type(text))
def get_toolbar():
	return "Bottom toolbar: time=%r" % time.time()


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
		result=path_entry_name_content[text]
		#return HTML('<aaa fg="white" bg="#008888">'+str(result)+'</aaa>')
		#return merge_formatted_text([HTML('<aaa style="bold" fg="white" bg="#444444">'+"'"+str(result)+"'"+'</aaa>'),"dd"])
		return str(result)
		#return [(Token, ' '),(Token.RPrompt, str(result)),]
	else:
		return('')
	#return HTML(get_app_or_none().current_buffer.text)
import datetime
def mainPrompt(title) ->HTML:
	icon=" >"
	#version=""
	version="vversion is version"
	#str(datetime.datetime.now())
	if detectNerdFont: icon=" "
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
			tab = tt.Texttable(max_width=os.get_terminal_size().columns)
			headings = ['N°','Path','Name','Type','Tags']
			tab.set_chars(["_","","","_"])
			tab.header(headings)
			#if 'type' not in path_entry_name_content[r]: path_entry_name_content[r]["type"]="none"
			tab.add_row([path_entry_name_content[r]["tmp_id"],path_entry_name_content[r]["path"],path_entry_name_content[r]["name"],path_entry_name_content[r]["type"],path_entry_name_content[r]["tags"]])
			print()
			print(tab.draw())
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




	
def getPromptSearch(default_promptSearch):
	completer=WordCompleter(
		[
		    "name=",
		    "tag=",
		    "type=",
		    "path=",
		    "tag",
		    "ssh_cmd",
		    "exe",
		    "action"
		],
		meta_dict={
		    "name=": " support regex case insitive",
		    "tag=": " exact tag,case insitive",
		    "ape": "Apes (Hominoidea) are a branch of Old World tailless anthropoid catarrhine primates ",
		    "bat": "Bats are mammals of the order Chiroptera",
		},
		ignore_case=True,
	)
   
	icon=" search >"
	if detectNerdFont: icon=" "
	history = FileHistory(tmpDir+".history_search")
	session = PromptSession(icon+" ",completer=completer,style=style,key_bindings=bindings,history=history)
	#prompt= session.prompt(pre_run=session.default_buffer.start_completion,default=default_promptSearch,rprompt=get_rprompt).replace('"','')
	try:
		prompt= session.prompt(default=default_promptSearch,rprompt=get_rprompt).replace('"','')
	except:
		exit()
	prompt=prompt.encode('ascii',errors='ignore').decode()
	#print(prompt.split(" "))
	result=[]
	tab = tt.Texttable(max_width=os.get_terminal_size().columns)
	headings = ['N°','Path','Name','Type','Tags']
	tab.header(headings)
	tab.set_chars(["_","","","_"])
	tab.set_chars(["_","","","_"])
	#tab.set_cols_align(["l", "c", "c"])
	if not prompt.replace(" ","") == "" :
		query=""

		#		pass 
		#	if i in "AND,OR":
		#		query=query+i+" "
		#	elif len(i.split("=")) == 2:
		#		if not i.split("=")[1] == "":
		#			if i.split("=")[0] == "pattern":
		#				pattern=i.split("=")[1]
		#		query=query+i+" "
		n=0
		for r in path_entry_name_content:
			queryT="" 
			if len(path_entry_name_content[r]) > 0:
				#print(prompt.split(" "))
				prec=""
				precCat=" "
				for i in prompt.split(" "):
					if i == "not":
						if prec == precCat:
							queryT=queryT+"and"+" "
						
					if i.split("=")[0] in "tag,name,type,path": 
						if len(i.split("=")) == 2:
							if prec == precCat:
								queryT=queryT+"and"+" "
							if i.split("=")[0] == "tag" :
								#print(i.split("=")[1].split(","))
								nextOperator=""
								for t in i.split("=")[1].split(","):
									if t is not "":
										if 'tags' in path_entry_name_content[r] and (t.lower() in path_entry_name_content[r]["tags"] or t.upper() in path_entry_name_content[r]["tags"]):
											queryT=queryT+nextOperator+str(True)+" "
										else: 	
											queryT=queryT+nextOperator+str(False)+" "
										nextOperator="and "
							if i.split("=")[0] == "name" :
								queryT=queryT+str(bool(re.search(i.split("=")[1],path_entry_name_content[r]["name"],re.IGNORECASE)))+" "
							if i.split("=")[0] == "path" :
								queryT=queryT+str(bool(re.search(i.split("=")[1],path_entry_name_content[r]["path"],re.IGNORECASE)))+" "
							if i.split("=")[0] == "type" :
								if 'type' in path_entry_name_content[r] and (i.split("=")[1].lower() == path_entry_name_content[r]["type"] or i.split("=")[1].upper() == path_entry_name_content[r]["type"]):
									queryT=queryT+str(True)+" "
								else: queryT=queryT+str(False)+" "

							precCat=i
						else:
							pass
							#if getPromptSearchCat()
					if i in "and,or,not":
						queryT=queryT+i+" "
					if i not in '""," "': prec=i
				#print(queryT)
				if queryT.replace(" ","") == "" or eval(str(queryT)) :
					n=n+1
					result.append(r)
					path_entry_name_content[r]["tmp_id"]=n
					if 'type' not in path_entry_name_content[r]: path_entry_name_content[r]["type"]="none"
					tab.add_row([n,path_entry_name_content[r]["path"],path_entry_name_content[r]["name"],path_entry_name_content[r]["type"],path_entry_name_content[r]["tags"]])
						#tab.add_row([colorama.Style.RESET_ALL+str(n),path_entry_name_content[r]["name"],str(path_entry_name_content[r]["tags"])])
			
		print(tab.draw())
		if "ssh_cmd" in prompt.split(" "):
			print("ssh_cmd")
			try:
				ssh_cmd(result)
				
			except AttributeError:  
				pass

		getPromptSearch(prompt)
						#os.system("ssh -t"+path_entry_name_content[r][ssh_module_keyword]+ "blabla")

#								for r in path_entry_name_content:
#							if len(path_entry_name_content[r]) > 0:
#									query=query+str(bool(re.search(pattern,r)))+" "
	else:
		n=0
		for r in path_entry_name_content:
			if len(path_entry_name_content[r]) > 0:
				n=n+1
				if 'type' not in path_entry_name_content[r]: path_entry_name_content[r]["type"]="none"
				tab.add_row([n,path_entry_name_content[r]["path"],path_entry_name_content[r]["name"],path_entry_name_content[r]["type"],path_entry_name_content[r]["tags"]])
		#getPromptSearch("name=")
		print(tab.draw())
		getPromptSearch(prompt)
		pass # tout afficher/prendre

def main():
	history = FileHistory(tmpDir+".history_main")
	session = PromptSession(mainPrompt(promptTitle), completer=completer, mouse_support=False,style=style, history=history, complete_style=CompleteStyle.MULTI_COLUMN,key_bindings=bindings)
	try:
		#prompt_id=session.prompt(pre_run=session.default_buffer.start_completion,rprompt=get_rprompt,default="").replace(" ","")
		prompt_id=session.prompt(placeholder="press space to use completion or up to use history",rprompt=get_rprompt,default="").replace(" ","")
		historyName=prompt_id
		prompt_id=prompt_id.encode('ascii',errors='ignore').decode()
		for i in prompt_id:
			if i in listIcon:
				pass
				#prompt_id=prompt_id.replace(i,"")
	except:
		#print("error")
		exit()
	if prompt_id == "--search":
		#try:
		getPromptSearch("")
			
		#except Exception as e:  
		#	print(str(e))
		main()

		exit()
	if prompt_id == "--version":
		print("version is git rev-parse HEAD hash")
		exit()
	if prompt_id == "--debug_config":
		print(json.dumps(path_entry_name_content, sort_keys=False, indent=4))
		exit()
	if prompt_id == "--debug_config_cmd":
		print(json.dumps(path_entry_name_content_cmd, sort_keys=False, indent=4))
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
	if  prompt_id in path_entry_name_content_cmd:
		if "show" in path_entry_name_content_cmd[prompt_id]:
			print(path_entry_name_content[prompt_id.replace("--show","")])
		if "encryptable" in path_entry_name_content_cmd[prompt_id]:
			os.system("cat "+tmpDir+os.path.basename(path_entry_name_content_cmd[prompt_id]["encryptable"])+" | gpg -a --cipher-algo AES256 -c")			
		if "encryptable-kube" in path_entry_name_content_cmd[prompt_id]:
			os.system("cat "+os.path.version is versionanduser(path_entry_name_content_cmd[prompt_id]["encryptable-kube"])+" | gpg -a --cipher-algo AES256 -c")			
		if keyword_web_content in path_entry_name_content_cmd[prompt_id]:
			modules.downloadWebContent.launch(path_entry_name_content=path_entry_name_content,prompt_id=prompt_id,keyword_web_content=keyword_web_content,tmpDir=tmpDir)
			#downloadFromUrl(path_entry_name_content[prompt_id.replace("--pull","")][keyword_web_content])
		if keyword_gitlab_content_code_prompt_token in path_entry_name_content_cmd[prompt_id]:
			downloadFromGitLabWithPromptToken(path_entry_name_content[prompt_id.replace("--pull","")][keyword_gitlab_content_code_prompt_token])
		if keyword_github_content_code_prompt_token in path_entry_name_content_cmd[prompt_id]:
			downloadFromGitHubWithPromptToken(path_entry_name_content[prompt_id.replace("--pull","")][keyword_github_content_code_prompt_token])
		exit()

	if  prompt_id in path_entry_name_content:
		text=prompt_id 
		if keyword_kubeconfig_file in path_entry_name_content[prompt_id]:
			startKubectl(path_entry_name_content[prompt_id][keyword_kubeconfig_file])

		if ssh_module_keyword in path_entry_name_content[prompt_id]:
			modules.ssh.launch(pattern= path_entry_name_content[prompt_id][ssh_module_keyword] )

		if www_module_keyword in path_entry_name_content[prompt_id]:
			modules.openWWW.launch(address= path_entry_name_content[prompt_id][www_module_keyword] )

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
		main()

if __name__ == "__main__":
    main()

exit()
# nice icon ⏽
