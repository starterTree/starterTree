#!/usr/bin/env python
# -*- coding: utf-8 -*-

def jinjaFile2yaml(jinjaFile):
    with open(jinjaFile) as file_:
        template = Template(file_.read())
    return yaml.load(template.render(),Loader=yaml.SafeLoader)


