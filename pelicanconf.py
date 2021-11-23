#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jelmer Vernooij'
SITENAME = 'Dulwich'
SITEURL = ''

PATH = 'content'

THEME = 'iris'

TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/dulwich/dulwich'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'assets']
SITEMAP = {'format': 'xml'}
MENUITEMS = (
    ("Home", "index.html"),
    ("Downloads", "downloads.html"),
    ("Getting Started", "getting-started.html"),
    ("Contributing", "contributing.html"),
    ("Help", "help.html"),
    )

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

INDEX_SAVE_AS = 'news.html'

STATIC_PATHS = ['releases']
