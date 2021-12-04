#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def writeConfig(path,content):
    with open(path,"w") as f:
            f.write(content)
    filename, file_extension = os.path.splitext(path)
    if file_extension == ".asc":
            os.system("gpg --batch --yes --out "+path+" -d "+path )

def downloadFromGitLabWithPromptToken(url,tmpDir):
    print(url)
    token=prompt('token like ezzfegzgezcH: ', is_password=True)
    r = requests.get(url, headers={'PRIVATE-TOKEN':token})
    rep='\n'.join(r.json()["content"].split('\n')[1:])
    writeConfig(tmpDir+os.path.basename(url),rep)

def downloadFromGitHubWithPromptToken(url,tmpDir):
    print(url)
    token=prompt('token like ezzfegzgezcH: ', is_password=True)
    r = requests.get(url, headers={'Authorization':'token '+token,'Accept': 'application/vnd.github.v4.raw'})
    rep='\n'.join(r.text.split('\n')[1:])
    writeConfig(tmpDir+os.path.basename(url),rep)

def downloadFromUrl(url,tmpDir):
    r = requests.get(url)
    writeConfig(tmpDir+os.path.basename(url),r.text)




#					path_entry_name_content["path_"+path_entry_name+keya]["content"]=source_dict[key][subKey]
#					path_entry_name_content["path_"+path_entry_name+keya]["description"]=subKey
#					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--pull"]={}
#					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--pull"][subKey]=source_dict[key][subKey]
#					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]={}
#					path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]["encryptable"]=source_dict[key][subKey]
#					if not os.path.exists(tmpDir+os.path.basename(source_dict[key][subKey])):
#						#os.system("curl -L -o "+tmpDir+os.path.basename(source_dict[key][subKey])+" "+source_dict[key][subKey])
#						if subKey == keyword_gitlab_content_code_prompt_token: downloadFromGitLabWithPromptToken(source_dict[key][subKey])
#						if subKey == keyword_github_content_code_prompt_token: downloadFromGitHubWithPromptToken(source_dict[key][subKey])
#						if subKey == keyword_web_content: downloadFromUrl(source_dict[key][subKey])
#					menu_completion[icon+key]={}

def run_web_content(args):
    downloadFromUrl(args["objet"][namePlugin_web],args["tmpDir"])

def run_web_content_gitlab(args):
    downloadFromUrl(args["objet"][namePlugin_web],args["tmpDir"])

def run_web_content_gihub(args):
    downloadFromUrl(args["objet"][namePlugin_web],args["tmpDir"])

from plugins.Plugin import Plugin,pluginsActivated
plugin=Plugin(namePlugin="gitlab_api_content_prompt_token",demoDataYaml=demoDataYaml,runInMenu=run_web_content_gitlab,icon="",options=["debug"])
plugin=Plugin(namePlugin="github_api_content_prompt_token",demoDataYaml=demoDataYaml,runInMenu=run_web_content_github,icon="",options=["debug"])
plugin=Plugin(namePlugin_web="web_content",demoDataYaml=demoDataYaml,runInMenu=run_web_content,icon="",options=["debug"])
