#!/usr/bin/env python
# -*- coding: utf-8 -*-






def launch(path_entry_name_content,prompt_id,keyword_module_opn):
	text = "xdg-open "+path_entry_name_content[prompt_id][keyword_module_opn]
	os.system(text)   

