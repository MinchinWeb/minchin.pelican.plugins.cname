# -*- coding: utf-8 -*- #
"""
CName
=============

This plugin add a *CNAME* file with contents based on ``SITEURL``.
"""

__version__ = '1.0.1'

import os
from pelican import signals

def add_cname(p):
    """ 
    :param p: pelican instance
    :return: None
    """

    cname_path = os.path.join(p.output_path, 'CNAME')
    siteurl = p.settings.get('SITEURL', "127.0.0.1:8000")
    siteurl = siteurl.replace("http://", "")
    siteurl = siteurl.replace("https://", "")
    with open(cname_path, 'w') as cname_file:
        cname_file.write(siteurl)    

def register():
    signals.finalized.connect(add_cname)