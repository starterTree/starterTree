#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prompt_toolkit.application import get_app_or_none
from prompt_toolkit import print_formatted_text, ANSI
from rich.console import Console
from rich.table import Table

def get_content_for_rprompt(plugins,path_entry_name_content):
	text=get_app_or_none().current_buffer.text.replace(" ","")
	text=text.encode('ascii',errors='ignore').decode()
	text='path_'+text
	if text in path_entry_name_content:
		result=''
		for i in plugins:
			if i.getName() in path_entry_name_content[text]:
				result=i.getContentForRprompt(stDict=path_entry_name_content[text])

		return result
	else:
		return('')



def getBottomToolbar(plugins,path_entry_name_content):
	result=get_content_for_rprompt(plugins,path_entry_name_content)	
	console=Console()	
	with console.capture() as capture:
	    #grid =Table(expand=False, box=box.SQUARE,show_header=False,show_edge=False,padding=(0,0))
	    grid =Table(expand=False, box=None,show_header=False,show_edge=False,padding=(0,1))
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



def getToolbar(plugins,path_entry_name_content):

    def tto():
        return getBottomToolbar(plugins,path_entry_name_content)

    return tto





