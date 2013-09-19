#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jaka Hudoklin'
AUTHOR_EMAIL = u'jakahudoklin@gmail.com'
SITENAME = u'Jaka Hudoklin'
SITEURL = 'http://www.jakahudoklin.com/'

TIMEZONE = 'Europe/Ljubljana'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('', 'http://www.github.com/offlinehacker'),
    ('', 'http://www.facebook.com/offlinehacker'),
    ('', 'http://www.twitter.com/offlinehacker')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = "theme/"
GRV_URL = "https://sl.gravatar.com/avatar/07de32bbf131a9bd6f9678105b05f84a?s=300"
WHAT_DO_I_THINK = "I am about to start some great projects and need some young enthusiastic people willing to share that enthusiasm, I need a team"
GOOGLE_ANALYTICS = "UA-44181448-1"
