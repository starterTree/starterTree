#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def register(config_dict,st_dict):
    st_dict["type"]="www"
    st_dict["content"]=config_dict["www"]
    st_dict["description"]=config_dict["www"]
    st_dict["www"]=config_dict["www"]

def launch(address):
	text = "xdg-open "+address
	os.system(text)   

def getIcon():
    return ""
