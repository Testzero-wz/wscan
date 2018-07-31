wscan
=====

A Fast & Simple web site scanner.
Base on aiohttp and refer to the dirsearch of multi-threading version.
Can both run in Linux & Windows.

Features
-------
- Fuzz web site path
- Mapping a site map
- Multi-co-routine
- User-agent randomization
- Custom extensions
- Custom maximum of co-routine
- Friendly interface

Demo
----

.. image:: https://raw.githubusercontent.com/WananpIG/wscan/master/wscan_test.gif

Usage:
-----

Type *-h* for help

**Usage:** 
wscan.py [-u URL] [-f] [-m] [Extend options]

==============   ===================
Optional arguments  Description
=========        ================================
-h, --help       show this help message and exit
-u URL           Target URL
-f               Fuzz target url with dictionary.
-m               Crawl all URL on the target to get a map of the site.
-max MAX_NUM     Max num of co-routine. [Default: 20]
-b BASE          Base URL of fuzz e.g -b /cms/app [Default: /]
-e EXTEND        Suffix name used in fuzz [Default: php]
--no-img         Don't crawl image url when mapping target
--no-re          Don't redirect when requesting
-v               Show more detail
-vv              Show the most detailed details
=========        ================================

Example: wscan.py -u "http://www.example.com/" -f -m -v



requires
--------
- Python >=3.5
- aiohttp
- colorama



