#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prompt_toolkit.completion import FuzzyWordCompleter,FuzzyCompleter,WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from modules.output.rich import Tableau as Tableau
from prompt_toolkit.history import FileHistory
import os
from prompt_toolkit.styles import Style
from .output_rich import Tableau as Tableau
tmpDir=os.environ['HOME']+'/.starterTree/'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)


bindings = KeyBindings()
@bindings.add('c-c')
def _(event):
#" Exit when `c-x` is pressed. "
	event.app.exit()


detectNerdFont= False
if not os.system("fc-list | grep -i nerd >/dev/null "):
    detectNerdFont= True

def fill_tableau(n,tableau_keys,path_entry_name_content_entry,tableau):
	tableau_lines=[]
	tableau_lines.append(n)
	for i in tableau_keys:
		if i in path_entry_name_content_entry:
			if ( i == "content" or i =="description") and "type" in path_entry_name_content_entry and path_entry_name_content_entry["type"] == "www":
				tableau_lines.append("[link="+path_entry_name_content_entry[i]+"]"+path_entry_name_content_entry[i]+"[/link]")
			else:
				tableau_lines.append(path_entry_name_content_entry[i])
		else:
			tableau_lines.append("")
	tableau.add_row(row=tableau_lines)


def getPromptSearch(path_entry_name_content,default_promptSearch="all",style=None):
	if default_promptSearch=="all":
		default_promptSearch=""
	completer=WordCompleter(
		[
		    "name=",
		    "tag=",
		    "type=",
		    "path=",
		    "display=",
		    "hide=",
		    "ssh_cmd",
		    #"tag",
		    #"exe",
		    #"action"
		],
		meta_dict={
		    "name=": "support regex case insitive",
		    #"name=": " support regex case insitive",
		    "tag=": "exact tag,case insitive",
		    "ssh_cmd" :"execute an command on selected servers, if prompt is empty, it's start session interactively",
		    #"tag=": " exact tag,case insitive",
		    "display=": "display column",
		    "hide=": "hide column",
		},
		ignore_case=True,
	)
   
	icon=" search >"
	if detectNerdFont: icon=" "
	history = FileHistory(tmpDir+".history_search")
	session = PromptSession(icon+" ",completer=completer,style=style,key_bindings=bindings,history=history)
	#prompt= session.prompt(pre_run=session.default_buffer.start_completion,default=default_promptSearch,rprompt=get_rprompt).replace('"','')
	try:
		prompt= session.prompt(default=default_promptSearch).replace('"','')
	except:
		exit()
	prompt=prompt.encode('ascii',errors='ignore').decode()
	prompt_and_default="not type=system_st AND not type=settings display=type,tags,description  "+prompt
	if prompt == "":
		prompt="all"
	if prompt[0:5] == "debug":
		prompt_and_default="display=type,tags,description  "+prompt
	if prompt[0:6] == "config":
		prompt_and_default="display=type,tags,description AND type=settings "+prompt
	result=[]
	tableau_keys={}
	for i in prompt_and_default.split(" "):
		if i.split("=")[0] in "display": 
			if len(i.split("=")) == 2:
				for t in i.split("=")[1].split(","):
					if t is not "":
						tableau_keys[t]=""
		if i.split("=")[0] in "hide": 
			if len(i.split("=")) == 2:
				for t in i.split("=")[1].split(","):
					if t is not "":
						tableau_keys.pop(t,"")

	headings=[]
	headings.append("N°")
	for i in tableau_keys:
		headings.append(i)
	tableau=Tableau(headings,detectNerdFont)
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

		#tableau=Tableau(['N°','Path','Name','Type','Tags','Content'])

		for r in path_entry_name_content:
			queryT="" 
			if len(path_entry_name_content[r]) > 0:
				#print(prompt.split(" "))
				prec=""
				precCat=" "
				for i in prompt_and_default.split(" "):
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
								if not i.split("=")[1].split(",") == "":
									queryT=queryT+"("+" "
								for t in i.split("=")[1].split(","):
									if t is not "":
										if 'tags' in path_entry_name_content[r] and (t in path_entry_name_content[r]["tags"]) :
											queryT=queryT+nextOperator+str(True)+" "
										else: 	
											queryT=queryT+nextOperator+str(False)+" "
										nextOperator="and "
										if prec== "not":
											nextOperator="or "
								if not i.split("=")[1].split(",") == "":
									queryT=queryT+")"+" "

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
					if i in "and,or,not,(,)":
						queryT=queryT+i+" "
					if i.split("=")[0] in ["tag","name","type","path","and","not","or","(",")"]: prec=i
					#if i.split("=")[0] not in '""," "': prec=i
				#print(queryT)
				if queryT.replace(" ","") == "" or eval(str(queryT)) :
					n=n+1
					result.append(r)
					path_entry_name_content[r]["tmp_id"]=n
					fill_tableau(str(n),tableau_keys,path_entry_name_content[r],tableau)
			
		tableau.draw(icon+" "+prompt)
		if "ssh_cmd" in prompt.split(" "):
			print("ssh_cmd")
			try:
				ssh_cmd(result)
				
			except AttributeError:  
				pass

		getPromptSearch(path_entry_name_content=path_entry_name_content,default_promptSearch=prompt,style=style)
						#os.system("ssh -t"+path_entry_name_content[r][ssh_module_keyword]+ "blabla")

#								for r in path_entry_name_content:
#							if len(path_entry_name_content[r]) > 0:
#									query=query+str(bool(re.search(pattern,r)))+" "
	else:
		n=0
		for r in path_entry_name_content:
			if len(path_entry_name_content[r]) > 0:
				n=n+1
				#setNoneForValue(path_entry_name_content[r],["path","name","type","tags"])
				fill_tableau(str(n),tableau_keys,path_entry_name_content[r],tableau)
				#tableau.add_row([str(n),path_entry_name_content[r]["path"],path_entry_name_content[r]["name"],path_entry_name_content[r]["type"],path_entry_name_content[r]["tags"]])
		#getPromptSearch("name=")
		tableau.draw(icon+" "+prompt)
		#getPromptSearch(prompt)
		getPromptSearch(path_entry_name_content=path_entry_name_content,default_promptSearch=prompt,style=style)
		pass # tout afficher/prendre

dataYaml="""
search:
  search: mode    
"""

def runInMenu(args):
    getPromptSearch(path_entry_name_content=args["pathEntry"],style=args["style"])   

from plugins.Plugin import Plugin,pluginsActivated
plugin=Plugin(namePlugin="search",dataYaml=dataYaml,runInMenu=runInMenu,icon=" ",options=["debug"])
