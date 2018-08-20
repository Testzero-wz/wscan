import codecs
import os
import sys
from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()




NAME = "wscan"

DESCRIPTION = "A Fast & Simple web site scanner. "

LONG_DESCRIPTION = read("README.rst")

KEYWORDS = "wscan scanner fuzz sitemap"

AUTHOR = "wz"

AUTHOR_EMAIL = "testzero.wz@gmail.com"

URL = "https://github.com/WananpIG/wscan/"

VERSION = "1.0.1"

LICENSE = "MIT"

REQUIRED = ["aiohttp", "colorama"]
PACKAGES = ['lib','fuzz']
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=REQUIRED,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
