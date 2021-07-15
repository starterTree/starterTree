#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ce module permet 


# pre traitement
# input path_entry_name_content_cmd path_entry_name keya subKey source_dict tmpDir
def preLaunch(path_entry_name_content_cmd,path_entry_name,keya,key,source_dict,subKey,tmpDir,menu_completion):
	if detectNerdFont: icon=""
	#utils.encryptable(path_entry_name_content_cmd,path_entry_name,keya,key,source_dict,subKey)
	#utils.pull(path_entry_name_content_cmd,path_entry_name,keya,key,source_dict,subKey)
	path_entry_name_content_cmd["path_"+path_entry_name+keya+"--pull"]={}
	path_entry_name_content_cmd["path_"+path_entry_name+keya+"--pull"][subKey]=source_dict[key][subKey]
	path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]={}
	path_entry_name_content_cmd["path_"+path_entry_name+keya+"--encrypt"]["encryptable"]=source_dict[key][subKey]
	if not os.path.exists(tmpDir+os.path.basename(source_dict[key][subKey])):
		#os.system("curl -L -o "+tmpDir+os.path.basename(source_dict[key][subKey])+" "+source_dict[key][subKey])
		downloadFromUrl(source_dict[key][subKey],tmpDir)
	menu_completion[icon+key]={}
	my_fun(yaml.load(open(tmpDir+os.path.basename(source_dict[key][subKey]), 'r'),Loader=yaml.SafeLoader),menu_completion[icon+key],path_entry_name+keya,path_entry_name_path+"/"+keya)
#


# realtime si selectionné
def launch(path_entry_name_content,prompt_id,keyword_web_content,tmpDir):
	downloadFromUrl(path_entry_name_content[prompt_id.replace("--pull","")][keyword_web_content],tmpDir)



# fonction interne
# url tmpDir
def downloadFromUrl(url,tmpDir):
	r = requests.get(url)
	with open(tmpDir+os.path.basename(url),"w") as f:
		f.write(r.text)
	filename, file_extension = os.path.splitext(tmpDir+os.path.basename(url))
	if file_extension == ".asc":
		os.system("gpg --batch --yes --out "+tmpDir+os.path.basename(url)+" -d "+tmpDir+os.path.basename(url) )



