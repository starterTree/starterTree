#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.formatted_text import merge_formatted_text
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.completion import FuzzyWordCompleter, FuzzyCompleter, WordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import CompleteStyle


# from prompt_toolkit.application import run_in_terminal,get_app_or_none
# from prompt_toolkit.shortcuts import prompt
def nerdFontIsPresent():
    detectNerdFont = False
    if not os.system("fc-list | grep -i nerd >/dev/null "):
        detectNerdFont = True
    return detectNerdFont


def mainPrompt(data) -> HTML:
    icon = " >"
    # version=""
    version = "version is version"
    # str(datetime.datetime.now())
    if nerdFontIsPresent: icon = " "  # icon=getIcon(""," >")
    caseVersion = HTML('<aaa style="" fg="red" bg="#444444"> ' + str(version) + '</aaa>')
    if not data["config"]["displayVersion"]: caseVersion= ""
    promptUser = HTML('<aaa style="" fg="white" bg="#444444"> ' + str(data["config"]["name"] + icon) + ' </aaa>')
    return merge_formatted_text([caseVersion, promptUser, " "])


bindings = KeyBindings()


@bindings.add('c-c')
def _(event):
    # " Exit when `c-x` is pressed. "
    event.app.exit()


def execMainPromptSession(data, promptTitle, bottomToolbar=None, plugins=None):
    completer = FuzzyCompleter(NestedCompleter.from_nested_dict(data["menu_completion"]))
    history = FileHistory(data["tmpDir"] + ".history_main")
    styleMainPrompt = Style.from_dict(data["style"]["completionMenu"])
    session = PromptSession(
        mainPrompt(data),
        completer=completer,
        mouse_support=False, style=styleMainPrompt,
        history=history,
        complete_style=CompleteStyle.MULTI_COLUMN,
        key_bindings=bindings)
    try:
        prompt_id = session.prompt(
            placeholder="press space to use completion or up to use history",
            rprompt=None,
            bottom_toolbar=bottomToolbar,
            default=""
        ).replace(" ", "")
    except AttributeError:
        exit()
    historyName = prompt_id
    prompt_id = prompt_id.encode('ascii', errors='ignore').decode()


    prompt_id = "path_" + prompt_id

    option = None
    # print(len(prompt_id.split("--")))
    if len(prompt_id.split("--")) == 2: option = prompt_id.split("--")[1]
    prompt_id = prompt_id.split("--")[0]
    if prompt_id in data["path_entry_name_content"]:
        # print(path_entry_name_content[prompt_id])
        text = prompt_id
        for p in (data["plugins"]):
            if p.getName() in data["path_entry_name_content"][prompt_id]:
                p.runInMenu(data["path_entry_name_content"][prompt_id], data=data, option=option, pathEntry=data["path_entry_name_content"])
                # with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
                #	myfile.write(text+' # '+historyName+'\n')


    else:
        print("ERR: entry not found")
        execMainPromptSession(data, promptTitle, bottomToolbar=bottomToolbar, plugins=plugins)
