=====
CName
=====

``CName`` is a plugin for `Pelican <http://docs.getpelican.com/>`_, a static
site generator written in Python.

``CName`` creates a *CNAME* file in the root of your output directory. This is
useful when you are publishing your site to `GitHub Pages
<https://pages.github.com/>`_ on a `custom domain
<https://help.github.com/articles/using-a-custom-domain-with-github-pages/>`_.


.. image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.cname.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.cname/
    :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
   :target: https://github.com/MinchinWeb/minchin.pelican.plugins.cname/blob/master/CHANGELOG.rst
   :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.plugins.cname?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.cname/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.plugins.cname.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/minchin.pelican.plugins.cname/blob/master/License.txt
    :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.plugins.cname.svg?style=flat
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.cname/
    :alt: Download Count


Installation
============

The easiest way to install ``CName`` is through the use of pip. This will also
install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.cname

Then, in your ``pelicanconf.py`` file, add ``CName`` to your list of plugins:

.. code-block:: python

  PLUGINS = [
              # ...
              'minchin.pelican.plugins.cname',
              # ...
            ]

And that's it! No further configuration is needed.


Usage
=====

No configuration is needed. The value places in the *CNAME* files is based on
your ``SITEURL`` setting.


Credits
=======

Based on the `original code
<https://github.com/getpelican/pelican-plugins/pull/566>`_ by `Dmitriy Kalinin
<http://lazycoder.ru/>`_.
