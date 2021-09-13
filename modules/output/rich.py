#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rich.console import Console
from rich.table import Table
from rich import box
from rich.columns import Columns
from rich.padding import Padding
from rich.text import Text
from rich.panel import Panel
console = Console()
style=""
#detectNerdFont= False
#if not os.system("fc-list | grep -i nerd >/dev/null "):
#    detectNerdFont= True
#title="  path="

class Tableau:
    def __init__(self, headings,detectNerdFont):
        self.tab = Table(row_styles = ["white on #666666", "white on #444444"],show_lines=False,show_header=True,show_footer=True,box=box.SIMPLE_HEAD,border_style="",show_edge=False, footer_style="bold green",header_style="bold green on #444444",expand=True,collapse_padding=True)
        self.tab.border_style = "bold #444444"
        self.detectNerdFont=detectNerdFont
        #self.tab.border_style = "green"
        for i in headings:
            if i =="Name": 
                self.tab.add_column(i,style="bold green",footer=i)
            elif i =="N°": 
                self.tab.add_column(i,style="bold red",footer=i)
            else: 
                self.tab.add_column(i,footer=i,overflow="fold")
    def getIcon(self,icon,defaultIcon=""):
        if self.detectNerdFont:
            return icon
        return defaultIcon
    def draw(self,title="Result"):
        console.rule("[bold red]"+title)
        console.print(Padding(self.tab,style="on #444444",pad=(1,1,1,1)))
        console.rule("[bold red]"+title)
    def add_row(self,row):
        for i in range(len(row)):
            if type(row[i]) == list:
                #print(type(row[i]))
                content=Text("",overflow="fold")
                for r in range(len(row[i])):
                    icon=''
                    style=''
                    if row[i][r]== "server": icon=self.getIcon(" ");style="bold red"
                    if row[i][r] == "web": icon=self.getIcon(" ");style="bold blue"
                    #r=' '+r+' '
                    #content.append("[white on black] "+r+" ")
                    #content=content+("[white on black] "+r+" [/white on black] ")
                    #content=content+Text(''+r,overflow="fold",style="bold white")+Text(" ")
                    if (r % 2) == 0:
                        #content=content+Text(''+row[i][r],overflow="fold",style="bold #ffffff")+Text(" ")
                        if icon=='': icon=self.getIcon('')
                        if style=='': style="#f2f2f2"
                        content=content+Text(icon+row[i][r],overflow="fold",style=style)+Text(" ")
                    else:
                        if icon=='': icon=self.getIcon('')
                        if style=='': style="#f2f2f2"
                        content=content+Text(icon+row[i][r],overflow="fold",style=style)+Text(" ")
                #row[i]=Padding(Columns(content,padding=(1,1,1,1)),pad=(1,1))
                row[i]=Padding(content,pad=(0,0,0,0),expand=False)
                #row[i]=Columns(content)
            else:
                row[i]=str(row[i])
                if row[i] == "www":
                    row[i]="[bold blue]www"
                if row[i] == "ssh":
                    row[i]="[bold red]ssh"
                if row[i] == "cmd":
                    row[i]="[bold purple]cmd"
        self.tab.add_row(*row)





