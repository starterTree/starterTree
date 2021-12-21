#!/usr/bin/env python
# -*- coding: utf-8 -*-
themes = []


class Theme:
    def __init__(self, name, styleDict=None):
        self.name = name
        self.styleDict = styleDict
        themes.append(self)

    def getName(self):
        return self.name

    def getStyle(self):
        return self.styleDict

import plugins.theme.themes.ListThemes