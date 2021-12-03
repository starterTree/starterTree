#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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


					path_entry_name_content["path_"+path_entry_name+keya]["content"]=source_dict[key][subKey]
					path_entry_name_content["path_"+path_entry_name+keya]["description"]=subKey
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

def run_web_content(args):



from plugins.Plugin import Plugin,pluginsActivated
plugin=Plugin(namePlugin="gitlab_api_content_prompt_token",demoDataYaml=demoDataYaml,runInMenu=runInMenu,icon="",options=["debug"])
plugin=Plugin(namePlugin="github_api_content_prompt_token",demoDataYaml=demoDataYaml,runInMenu=runInMenu,icon="",options=["debug"])
plugin=Plugin(namePlugin="web_content",demoDataYaml=demoDataYaml,runInMenu=run_web_content,icon="",options=["debug"])
