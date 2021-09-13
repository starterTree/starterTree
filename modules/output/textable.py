#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import texttable as tt


class Tableau:
    def __init__(self, headings):
        self.headings = headings
        self.tab = tt.Texttable(max_width=os.get_terminal_size().columns)
        self.tab.set_chars(["_","","","_"])
        self.tab.header(self.headings)
    def draw(self):
        print(self.tab.draw())
    def add_row(self,row):
        self.tab.add_row(row)



