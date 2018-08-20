wscan v2.0
=====

A Fast & Simple web site scanner.
Base on aiohttp and refer to the dirsearch of multi-threading version.

Can both run in Linux & Windows.

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

.. image:: https://raw.githubusercontent.com/WananpIG/wscan/master/demo.gif

Usage:
-----

**Type** ``-h`` **for help** :: 

  $ wscan.py [-u URL] [-f] [-m] [Extend options]

  
* **-u  URL**:          Target URL.   

* **-f**:   Fuzz target url with dictionary .

* **-m**:   Crawl all URL on the target to get a map. 

<<<<<<< HEAD
* **-b  BASE**:  Base URL of fuzzing **e.g** -b /cms/app.   \[ Default: / \]

* **-e  EXTEND**:   Suffix name used for fuzzing. [Default: php]

* **-max   NUM**:     Max num of co-routine. \[ Default: 20 \] 

* **-404 NOT_FOUND**:       Customize a 404 identification, it'll be used as a keyword for searching text. e.g. "Not found"

* **-s**:       Crawl static resources when mapping target.

* **--no-re**:       Don't redirect when requesting. 

* **-v,-vv**:      Show more detail.

* **-h**:       Show this help message and exit.
=======
* **-b  BASE**:  Base URL of fuzz **e.g** -b /cms/app.   \[ Default: / \]

* **-e  EXTEND**:   Suffix name used in fuzz.  \[ Default: php \]

* **-max   NUM**:     Max num of co-routine. \[ Default: 20 \] 

* **--no-img**:       Don't crawl image url when mapping target. 

* **--no-re**:       Don't redirect when requesting. 

* **-v**:      Show more detail.  

* **-vv**:      Show the most detailed details. 

* **-h**:       Show this help message and exit. 
>>>>>>> b8a386b4b7a35f549d9671c8934a5617f5f70ffa


Example :: 

  $ wscan.py -u "http://www.example.com/" -f -m 


Requires
--------
- Python >=3.5
- aiohttp
- colorama
- bs4





