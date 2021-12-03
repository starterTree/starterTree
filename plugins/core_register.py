#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    #print(template.render(name='John'))
    return yaml.load(template.render(),Loader=yaml.SafeLoader)


def my_fun(source_dict,menu_completion,path_entry_name,path_entry_name_path):
	for key in source_dict:
		keya=key.encode('ascii',errors='ignore').decode()
		#if "path_"+path_entry_name+keya not in path_entry_name_content:
		path_entry_name_content["path_"+path_entry_name+keya]={}
		path_entry_name_content["path_"+path_entry_name+keya]["type"]="system_st"
		path_entry_name_content["path_"+path_entry_name+keya]["content"]="system_st"
		#path_entry_name_content["path_"+path_entry_name+key]=source_dict[key]

		for subKey in source_dict[key]:
			icon=""
			#path_entry_name_content["path_"+path_entry_name+keya]["tags"]={}
			if not isinstance(source_dict[key][subKey],dict):
				self={}
				self["tags"]=[]
				path_entry_name_content["path_"+path_entry_name+keya]["path"]=path_entry_name_path+"/"
				path_entry_name_content["path_"+path_entry_name+keya]["name"]=keya
				#CONFIGURE SETTINGS
				if subKey in ["starterTree_disableIcon","starterTree_title","starterTree_theme"]: 
					path_entry_name_content["path_"+path_entry_name+keya]["content"]=source_dict[key]
					path_entry_name_content["path_"+path_entry_name+keya]["type"]="settings"
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
					self["tags"]=[]
					path_entry_name_content["path_"+path_entry_name+keya]["tags"]={}
					path_entry_name_content["path_"+path_entry_name+keya]["tags"]=source_dict[key][subKey]
					self["tags"]=source_dict[key][subKey]
				if subKey == keyword_file_content_relative:
					if detectNerdFont: icon=""
					path_entry_name_content["path_"+path_entry_name+keya][subKey]=source_dict[key][subKey]
					menu_completion[icon+key]={}
					#my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)
					my_fun(jinjaFile2yaml(absolute_path_main_config_file+source_dict[key][subKey]),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)

				if subKey in [keyword_gitlab_content_code_prompt_token, keyword_github_content_code_prompt_token, keyword_web_content] :	
					if detectNerdFont: icon=""
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
					#my_fun(yaml.load(open(tmpDir+os.path.basename(source_dict[key][subKey]), 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)
					#print(tmpDir+os.path.basename(source_dict[key][subKey]))
					my_fun(jinjaFile2yaml(tmpDir+os.path.basename(source_dict[key][subKey])),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)	
				#Register Plugins
				if subKey in plugins.Plugin.pluginsActivated:
					if detectNerdFont: icon=plugins.Plugin.pluginsActivated[subKey].getIcon()
					menu_completion[icon+key]={}
					plugins.Plugin.pluginsActivated[subKey].register(configDict=source_dict[key],stDict=path_entry_name_content["path_"+path_entry_name+keya],menuDict=menu_completion[icon+key])	

				#if subKey == keyword_file_content_relative:
					#my_fun(yaml.load(open(absolute_path_main_config_file+source_dict[key][subKey], 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+key)
					
				
			if isinstance(source_dict[key][subKey], dict):
				if detectNerdFont: icon=""
				if "icon" in source_dict[key] and detectNerdFont:
					icon=source_dict[key]["icon"]
				menu_completion[icon+key+""]={}
				menu_completion[icon+key+""]["--list"]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"]={}
				#path_entry_name_content["path_"+path_entry_name+key+"--list"][subKey]=source_dict[key]
				my_fun(source_dict[key], menu_completion[icon+key+""] ,path_entry_name+keya,path_entry_name_path+"/"+keya)
				#del path_entry_name_content["path_"+path_entry_name+keya]
				
menu_completion={}


