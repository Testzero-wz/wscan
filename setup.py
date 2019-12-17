import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


NAME = "wscan"

DESCRIPTION = "A Fast & Simple web site scanner. "

LONG_DESCRIPTION = read("README.md")

KEYWORDS = "wscan scanner fuzz sitemap base on aiohttp"

AUTHOR = "wz"

AUTHOR_EMAIL = "testzero.wz@gmail.com"

URL = "https://github.com/testzero-wz/wscan/"

VERSION = "2.4.3"

LICENSE = "MIT"
console_scripts = ['wscan=wscan.main:main']
REQUIRED = ["aiohttp", "colorama", "bs4"]
PACKAGES = find_packages()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
    ],
    package_data={
        '': ['*.txt', '*.md'],
        'wscan/fuzz': ['*.txt']
    },
    entry_points={'console_scripts': console_scripts},
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
