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

    prompt_id = session.prompt(
        placeholder="press space to use completion or up to use history",
        rprompt=None,
        bottom_toolbar=bottomToolbar,
        default=""
    ).replace(" ", "")
    historyName = prompt_id
    prompt_id = prompt_id.encode('ascii', errors='ignore').decode()
    # except:
    #    print("error")
    #    exit()

    prompt_id = "path_" + prompt_id
    # if  prompt_id in path_entry_name_content_cmd:
    #    if "encryptable" in path_entry_name_content_cmd[prompt_id]:
    #        os.system("cat "+tmpDir+os.path.basename(path_entry_name_content_cmd[prompt_id]["encryptable"])+" | gpg -a --cipher-algo AES256 -c")			
    #    if "encryptable-kube" in path_entry_name_content_cmd[prompt_id]:
    #        os.system("cat "+os.path.basename(path_entry_name_content_cmd[prompt_id]["encryptable-kube"])+" | gpg -a --cipher-algo AES256 -c")			

    #    if keyword_web_content in path_entry_name_content_cmd[prompt_id]:
    #        modules.downloadWebContent.launch(path_entry_name_content=path_entry_name_content,prompt_id=prompt_id,keyword_web_content=keyword_web_content,tmpDir=tmpDir)
    #        #downloadFromUrl(path_entry_name_content[prompt_id.replace("--pull","")][keyword_web_content])
    #    if keyword_gitlab_content_code_prompt_token in path_entry_name_content_cmd[prompt_id]:
    #        downloadFromGitLabWithPromptToken(path_entry_name_content_cmd[prompt_id.replace("","")][keyword_gitlab_content_code_prompt_token])
    #    if keyword_github_content_code_prompt_token in path_entry_name_content_cmd[prompt_id]:
    #        downloadFromGitHubWithPromptToken(path_entry_name_content_cmd[prompt_id.replace("","")][keyword_github_content_code_prompt_token])
    # exit()
    # print(prompt_id)
    option = None
    # print(len(prompt_id.split("--")))
    if len(prompt_id.split("--")) == 2: option = prompt_id.split("--")[1]
    prompt_id = prompt_id.split("--")[0]
    if prompt_id in data["path_entry_name_content"]:
        # print(path_entry_name_content[prompt_id])
        text = prompt_id
        for p in (data["plugins"]):
            if p.getName() in data["path_entry_name_content"][prompt_id]:
                p.runInMenu(data["path_entry_name_content"][prompt_id], option=option, pathEntry=data["path_entry_name_content"])
                # with open(os.environ['HOME']+"/.bash_history", "a") as myfile:
                #	myfile.write(text+' # '+historyName+'\n')


    else:
        print("ERR: entry not found")
        main()
