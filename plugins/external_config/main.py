#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from modules.utils import my_fun,jinjaFile2yaml
from rich.panel import Panel
from rich.table import Table
from getpass import getpass
from rich.console import Group

def writeConfig(path,content):
    with open(path,"w") as f:
            f.write(content)
    filename, file_extension = os.path.splitext(path)
    if file_extension == ".asc":
            os.system("gpg --batch --yes --out "+path+" -d "+path )
    return path

def loadData(args,configFile):
    icon = args["self"].getIcon()
    if "icon" in args["configDict"]:
        icon = args["configDict"]["icon"]


    key_menu_completion = (icon + args["key"]).replace(" ", "⠀")
    #args["menu_completion"][key_menu_completion] = {}
    my_fun(
        source_dict=jinjaFile2yaml(configFile),
        menu_completion=args["menu_completion"][key_menu_completion],
        path_entry_name=args["path_entry_name"] + args["key"],
        path_entry_name_path=args["path"] + args["key"],
        plugins=args["data"]["plugins"],
        data=args["data"],
        tab=args["tab"]
    )



def downloadFromGitLabWithPromptToken(url,tmpDir):
    print(url)
    token=getpass('token like ezzfegzgezcH: ')
    #token=getpass('token like ezzfegzgezcH: ', is_password=True)
    r = requests.get(url, headers={'PRIVATE-TOKEN':token})
    token=""
    rep='\n'.join(r.json()["content"].split('\n')[1:])
    return writeConfig(tmpDir+url.replace('/','°' ),rep)
    #return writeConfig(tmpDir+os.path.basename(url),rep)

def downloadFromGitHubWithPromptToken(url,tmpDir):
    print(url)
    token=getpass('token like ezzfegzgezcH: ')
    r = requests.get(url, headers={'Authorization':'token '+token,'Accept': 'application/vnd.github.v4.raw'})
    token=""
    rep='\n'.join(r.text.split('\n')[1:])
    writeConfig(tmpDir+url.replace('/','°' ),rep)

def downloadFromUrl(url,tmpDir):
    r = requests.get(url)
    return writeConfig(tmpDir+url.replace('/','°' ),r.text)

demoDataYaml="""
demo_web_content:
  web_content: https://raw.githubusercontent.com/starterTree/starterTree/dev/plugins/external_config/tests/test_web_content.yml
"""


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

def register_web_content(args):
    #path=os.path.basename(args["configDict"]["web_content"])
    path=args["tmpDir"]+args["configDict"]["web_content"].replace('/','°')
    #if not os.path.exists(args["tmpDir"] + os.path.basename(args["configDict"]["web_content"])):
    if not os.path.exists(path):
        downloadFromUrl(args["configDict"]["web_content"],args["tmpDir"])
    loadData(args,path)

def run_web_content(args):
    if args["option"] == "pull" :
        downloadFromUrl(args["objet"]["web_content"], args["tmpDir"])


def register_web_content_gitlab(args):
    path=args["tmpDir"]+args["configDict"]["gitlab_api_content_prompt_token"].replace('/','°')
    if not os.path.exists(path):
        downloadFromGitLabWithPromptToken(args["configDict"]["gitlab_api_content_prompt_token"],args["tmpDir"])
    loadData(args,path)

def run_web_content_gitlab(args):
    if args["option"] == "pull" :
        downloadFromGitLabWithPromptToken(args["objet"]["gitlab_api_content_prompt_token"], args["tmpDir"])



def register_web_content_github(args):
    path=args["tmpDir"]+args["configDict"]["github_api_content_prompt_token"].replace('/','°')
    if not os.path.exists(path):
        downloadFromGitHubWithPromptToken(args["configDict"]["github_api_content_prompt_token"],args["tmpDir"])
    loadData(args,path)

def run_web_content_github(args):
    if args["option"] == "pull" :
        downloadFromGitHubWithPromptToken(args["objet"]["github_api_content_prompt_token"], args["tmpDir"])



def preview(args):
    from rich.padding import Padding
    from rich.columns import Columns
    a=[]
    for i in args["element"]["preview"][args["element"]["key_menu_completion"]]:
        if i  not in ["--list","--pull"] :
            a.append(i)
    user_renderables = [Padding("[bold on white]"+user, expand=True) for user in a]
    return(Columns(user_renderables))

def getContentForRprompt(args):
    nameLeft = ""
    for i in (args["self"].getTitleIcon() + args["element"]["title"].upper()):
        nameLeft = nameLeft + "[bold on white]" + i + "" + "\n"
    grid = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 1))
    grid.add_column(style=args["self"].titleColor)
    grid2 = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 1))
    grid2.add_row("[bold #444444 on white]\n" + args["element"]["description"] + "\n")
    # grid2.add_row(Markdown("`bash` "))     # markdown is possible !
    grid2.add_row(Plugin.displayTags(args["element"]["tags"]))
    grid3 = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 0))
    #grid3.add_row(Panel.fit(preview(args),title=args["self"].getTitleIcon(),style="bold on green"))
    grid3.add_row(preview(args))
    gridDescPrev = Table(expand=False, box=None, show_header=False, show_edge=False, padding=(0, 1))
    gridDescPrev.add_row(grid2,Panel.fit(preview(args),title=args["self"].getTitleIcon()+" "+args["element"]["path"]+args["element"]["name"],style="bold on green"))
    grid.add_row(nameLeft,gridDescPrev )
    grid.add_row("","[bold on white] from cached file: "+args["element"][args["element"]["type"]])
    return Group(grid)



import Plugin

plugin=Plugin.Plugin(namePlugin="gitlab_api_content_prompt_token",title="git",demoDataYaml=demoDataYaml,afterRegister=register_web_content_gitlab,runInMenu=run_web_content_gitlab,icon=" ",titleIcon="",options=["pull"],getCustomContentForRprompt=getContentForRprompt)
plugin=Plugin.Plugin(namePlugin="github_api_content_prompt_token",title="git",demoDataYaml=demoDataYaml,afterRegister=register_web_content_github,runInMenu=run_web_content_github,icon=" ",titleIcon="",options=["pull"],getCustomContentForRprompt=getContentForRprompt)
plugin=Plugin.Plugin(namePlugin="web_content",title="web",demoDataYaml=demoDataYaml,afterRegister=register_web_content,runInMenu=run_web_content,icon=" ",titleIcon="",options=["pull"],getCustomContentForRprompt=getContentForRprompt)
