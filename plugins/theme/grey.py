#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plugins.theme.Theme import Theme

style = {
    "completionMenu": {
        # Token.RPrompt: 'bg:#ff0066 #ffffff',
        # 'session': 'bg:#ffffff #000000',
        'completion-menu.completion': 'bg:#444444 white',
        'completion-menu.completion.current': 'bg:#666666 white',
        'completion-menu.multi-column-meta': 'bg:green blue',
        'completion-menu.completion fuzzymatch.outside': 'fg:white',
        'completion-menu': 'bg:#444444',
        'scrollbar.background': 'bg:#88aaaa',
        'scrollbar.button': 'bg:#222222',
        'bottom-toolbar': '#444444',
        # 'prompt': 'bg:#444444 white',
        # 'arg-toolbar': 'bg:white #00aaaa',
        # 'prompt.arg.text': 'bg:#ffffff #00aaaa',
    }
    , "promptVersion": 'fg="red" bg="#444444"'
    , "PromptUser": 'fg="white" bg="#444444"'
}

theme = Theme("grey",style)
