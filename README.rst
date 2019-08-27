wscan v2.2
=====
wscan——一个基于协程的轻量级Web目录扫描器

写来平时用来打CTF，探测敏感信息和目录结构的，主要目的还是要优雅 、快捷一点 **:)**

适用于CTF这类网站页面不多，需要敏感文件、目录结构探测的网站扫描

安装
----
:: 

  $ pip install wscan


特性
----

- Fuzz网站目录
- 爬取网站url
- 多协程更效率
- 可随机User-agent
- 自定义Fuzz后缀名
- 指定爬取协程数
- **友好的界面 : )**

Demo
----

.. image:: https://i.loli.net/2018/10/21/5bcbf4e2841b4.gif

用法:
-----

**Type** ``-h`` **for help** :: 

  $ wscan [-u URL] [-f] [-m] [Extend options]


* **-u  URL**:          目标URL  

* **-f**:   启用Fuzz功能

* **-m**:   启用链接爬取功能（就是遍历爬取啦，网站大的话会炸锅）

* **-b  BASE**:  Fuzz的基址 **如:** -b /cms/app.   \[ Default: / \] （将会从/cms/app为基础，在其后面添加字典路径进行Fuzz）

* **-e  EXTEND**:   Fuzz的后缀名. [Default: php]

* **-max   NUM**:     协程最大值. \[ Default: 20 \] 

* **-404 NOT_FOUND**:      自定义404页面的关键字，用于判断自定义404页面。如： "Not found"

* **-s**:       爬取静态资源链接（一般XSS、CSRF等题里面会用到静态资源如js，css，img等）

* **--no-re**:       爬链接的时候禁止重定向

* **-v,-vv**:      -v显示详细信息，-vv显示最详细的信息

* **-h**:       帮助


例子:: 

  $ wscan -u "http://www.example.com/" -f -m 


安装依赖
--------
- Python >=3.5
- aiohttp
- colorama
- bs4

感谢开源作者 `maurosoria <https://github.com/maurosoria>`_开源的 `dirsearch <https://github.com/maurosoria/dirsearch>`_ 为wscan提供的灵感以及Fuzz字典。

English Document
======


wscan——A Fast & Simple web site scanner.
Base on aiohttp and refer to the dirsearch of multi-threading version.

Can both run in Linux & Windows.

Install
----
:: 

  $ pip install wscan


Features
----

- Fuzz web site path
- Mapping a site map
- Multi-co-routine
- User-agent randomization
- Custom extensions
- Custom maximum of co-routine
- Friendly interface

Demo
----

.. image:: https://i.loli.net/2018/10/21/5bcbf4e2841b4.gif

Usage:
-----

**Type** ``-h`` **for help** :: 

  $ wscan [-u URL] [-f] [-m] [Extend options]


* **-u  URL**:          Target URL.   

* **-f**:   Fuzz target url with dictionary .

* **-m**:   Crawl all URL on the target to get a map. 

* **-b  BASE**:  Base URL of fuzzing **e.g** -b /cms/app.   \[ Default: / \]

* **-e  EXTEND**:   Suffix name used for fuzzing. [Default: php]

* **-max   NUM**:     Max num of co-routine. \[ Default: 20 \] 

* **-404 NOT_FOUND**:       Customize a 404 identification, it'll be used as a keyword for searching text. e.g. "Not found"

* **-s**:       Crawl static resources when mapping target.

* **--no-re**:       Don't redirect when requesting. 

* **-v,-vv**:      Show more detail.

* **-h**:       Show this help message and exit.


Example :: 

  $ wscan -u "http://www.example.com/" -f -m 


Requires
--------
- Python >=3.5
- aiohttp
- colorama
- bs4





