# JGD: Jimut's Git Downloader

[![DOI](https://zenodo.org/badge/183674017.svg)](https://zenodo.org/badge/latestdoi/183674017)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)
![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)
![Contribute](https://img.shields.io/badge/-contribute-0a0a0a.svg?style=flat&colorA=0a0a0a)

This program scraps and download every public repo present out there!
It doesn't uses auth/token. Useful when you just need to download files of a folder, and not the whole repo.


#### DEMOS:

<a href="https://www.youtube.com/watch?v=jq9o54D2ySo" alt="YT video" target="_blank"><img src="img/jgd.png" alt="jgd youtube image"></a>

#### Installation

```
$ git clone https://github.com/Jimut123/jgd
$ cd jgd
$ sudo python setup.py install
$ jgd -h
usage: jgd [-h] url

positional arguments:
  url         URL is mandatory! Please provide URL to folder/repo of Public
              repository.

optional arguments:
  -h, --help  show this help message and exit

```



#### Pros:
* No need to download the whole repo, scrap it.
* Downloads files, folders 
* Doesn't uses any kind of token

#### Cons:
* Need to reclone it everytime the repo is updated, this is not GIT!


#### USAGE:
```
python jgd.py <any-git-folder-url>
python jgd.py <any-git-repo-url>
```
#### Install the requirements:
```
sudo pip install -r requirements.txt
```

## [LICENSE](https://github.com/Jimut123/jgd/edit/master/LICENSE)
```
 GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2019-20 Jimut Bahan Pal, <https://jimut123.github.io/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
```

#### Author:
* [Jimut Bahan Pal](https://jimut123.github.io)
