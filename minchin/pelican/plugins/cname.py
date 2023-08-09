# -*- coding: utf-8 -*- #
"""
CName
=============

This plugin for Pelican add a *CNAME* file with contents based on ``SITEURL``.
"""

import os

from pelican import signals

__title__ = "minchin.pelican.plugins.cname"
__version__ = "1.3.4"
__description__ = "Pelican plugin that adds a `CNAME` file to the output root. Useful for publishing to Github Pages. Written in Python."
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__url__ = "https://github.com/MinchinWeb/minchin.pelican.plugins.cname"
__license__ = "AGPL-3.0"


def add_cname(p):
    """
    :param p: pelican instance
    :return: None
    """

    cname_path = os.path.join(p.output_path, "CNAME")
    siteurl = p.settings.get("SITEURL", "127.0.0.1:8000")
    if siteurl.startswith("http://"):
        siteurl = siteurl[7:]
    elif siteurl.startswith("https://"):
        siteurl = siteurl[8:]
    elif siteurl.startswith("//"):
        siteurl = siteurl[2:]

    with open(cname_path, "w") as cname_file:
        cname_file.write(siteurl)


def register():
    signals.finalized.connect(add_cname)
