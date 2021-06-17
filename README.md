<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    
  </a>

  <h3 align="center">StarterTree</h3>

  <p align="center">
    command launcher organised in a tree structure with autocompletion <br>
    <br />
  <!--
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<!--
![Product Name Screen Shot][product-screenshot]](https://i.imgur.com/yct5sjZ.gif)


Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description`

-->
### Built With

* Python3 with module [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)




<!-- GETTING STARTED -->
## Getting Started



### Prerequisites


* Linux system (not yet tested on windows)
* Python3  (only if you do not use the binary in release section)


### Installation

1. Download the release and create symlink
   ```bash  
   cd /opt 
   sudo curl -L 'https://github.com/thomas10-10/az/releases/download/v0.2/starterTree.tar.gz' | sudo tar -xz   
   ```

2. Create symlink
   ```bash
   sudo ln -s /opt/starterTree/starterTree /usr/local/bin/t
   ```
   <!--  curl -L ’https://github.com/thomas10-10/az/releases/download/v0.1/az.tar.gz' | tar -xz - -C az --strip-components=1 -->


<!-- USAGE EXAMPLES -->
## Usage
A configuration must be in ~/.config/starterTree/config.yml .
Otherwise you can specify the path of the config file as an argument:
` t /tmp/myconfig.yml`
>and you can use the alias command to encapsulate the config file:
` alias t="t /tmp/myconfig.yml"`
or to manage several different configurations:
` alias toto1="t /other/myconfig.yml"`
` alias toto2="t /other/anOtherconfig.yml"`
 
there is a sample configuration file in git depot `exampleConfig/config.yml`
  
```yaml
main: #create menu main
  toto: # create menu toto
    link1: # create entry link1 who own attribute cmd
      cmd: "xdg open google.com" # if link1 is chosen, this command will be executed
      link1_2: # create sub entry link1_2 who own attribute cmd
        cmd: "xdg open google.fr" # if link1_2 is chosen, this command will be executed
    link2:
      cmdP: "xdg open google.fr" # if link2 is chosen, this command will be executed after a confirmation
    bibi: #create menu bibi
      file_content_relative: dir/otherConf.yml # load the following config file in the section bibi
  
 ```

<!--
_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap
an improved interface with a space to display the description of an entry is planned


<!--
See the [open issues](https://github.com/github_username/repo_name/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



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


