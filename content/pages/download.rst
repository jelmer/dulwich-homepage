:title: Downloads
:save_as: downloads.html

pypi
====

Dulwich releases are published on pypi, and pip is probably the easiest way to
install it if your distribution doesn't ship it.

By default, Dulwich' setup.py will attempt to build and install the optional C
extensions. The reason for this is that they significantly improve the performance
since some low-level operations that are executed often are much slower in CPython.

If you don't want to install the C bindings, specify the --pure argument to setup.py::

    $ pip install dulwich --global-option="--pure"

Note that you can also specify --global-option in a
[requirements.txt](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers)
file, e.g. like this::

    dulwich --global-option=--pure

From a git checkout
===================

The main Git repository for Dulwich lives at https://github.com/dulwich/dulwich::

    $ git clone https://github.com/dulwich/dulwich dulwich

By default, Dulwich' setup.py will attempt to build and install the optional C
extensions. The reason for this is that they significantly improve the performance
since some low-level operations that are executed often are much slower in CPython.

To install Dulwich without building the C extensions, run::

    $ python setup.py --pure install

Tarballs
========

.. include:: tarballs.rst

