
![logo](https://i.imgur.com/nHDBrIC.png)
# StarterTree
command launcher and ssh connection manager organised in a tree structure with autocompletion <br>

![](https://i.imgur.com/BD5IpJM.png)

**with search mode by tag**

![](https://i.imgur.com/R9UEoVa.png)


## About The Project

### Built With

* Python3 with module [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)

<!-- GETTING STARTED -->
## Getting Started



### Prerequisites


* Linux system


### Installation

Download and install

```
curl -L https://raw.githubusercontent.com/starterTree/starterTree/master/install.sh | bash
```

or

```bash  
cd /opt 
sudo curl -L "https://github.com/starterTree/starterTree/releases/download/$(basename $(curl -fsSLI -o /dev/null -w %{url_effective} https://github.com/starterTree/starterTree/releases/latest))/starterTree.tar.gz" | sudo tar -xz 
sudo ln -s /opt/starterTree/starterTree /usr/local/bin/t
```

<!--  curl -L ’https://github.com/thomas10-10/az/releases/download/v0.3/az.tar.gz' | tar -xz - -C az --strip-components=1 -->

to enable icons, you must install nerd fonts [nerdFonts](https://www.nerdfonts.com/font-downloads)

#### UPDATE 

since version 0.7 you can update with:
```
#update to last versiob
t > --update
#update to precise version
t > --update=v0.7
```

<!-- USAGE EXAMPLES -->
## Usage
to run:
```
$ t
```
A configuration must be in `~/.config/starterTree/config.yml`

you need press key space or tab to use autocomplete 

There is a sample configuration file in git depot `exampleConfig/config.yml`
    
Otherwise you can specify the path of the config file as an argument:
```
 t /tmp/myconfig.yml
```
>and you can use the alias command to encapsulate the config file:
` alias t="t /tmp/myconfig.yml"`
or to manage several different configurations:
` alias toto1="t /other/myconfig.yml"`
` alias toto2="t /other/anOtherconfig.yml"`
or run starterTree via bind:
`bind -x '"\C-p":t'`





<!-- LICENSE -->
<!--
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
<!--
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
<!--
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username



