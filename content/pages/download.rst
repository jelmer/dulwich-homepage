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

  * `0.19.3 <releases/dulwich-0.19.3.tar.gz>`_ (`0.19.3 GPG signature <releases/dulwich-0.19.3.tar.gz.asc>`_)
  * `0.19.2 <releases/dulwich-0.19.2.tar.gz>`_ (`0.19.2 GPG signature <releases/dulwich-0.19.2.tar.gz.asc>`_)
  * `0.19.1 <releases/dulwich-0.19.1.tar.gz>`_ (`0.19.1 GPG signature <releases/dulwich-0.19.1.tar.gz.asc>`_)
  * `0.19.0 <releases/dulwich-0.19.0.tar.gz>`_ (`0.19.0 GPG signature <releases/dulwich-0.19.0.tar.gz.asc>`_)
  * `0.18.3 <releases/dulwich-0.18.3.tar.gz>`_ (`0.18.3 GPG signature <releases/dulwich-0.18.3.tar.gz.asc>`_)
  * `0.18.2 <releases/dulwich-0.18.2.tar.gz>`_ (`0.18.2 GPG signature <releases/dulwich-0.18.2.tar.gz.asc>`_)
  * `0.18.1 <releases/dulwich-0.18.1.tar.gz>`_ (`0.18.1 GPG signature <releases/dulwich-0.18.1.tar.gz.asc>`_)
  * `0.18.0 <releases/dulwich-0.18.0.tar.gz>`_ (`0.18.0 GPG signature <releases/dulwich-0.18.0.tar.gz.asc>`_)
  * `0.17.3 <releases/dulwich-0.17.3.tar.gz>`_ (`0.17.3 GPG signature <releases/dulwich-0.17.3.tar.gz.asc>`_)
  * `0.17.2 <releases/dulwich-0.17.2.tar.gz>`_ (`0.17.2 GPG signature <releases/dulwich-0.17.2.tar.gz.asc>`_)
  * `0.17.1 <releases/dulwich-0.17.1.tar.gz>`_ (`0.17.1 GPG signature <releases/dulwich-0.17.1.tar.gz.asc>`_)
  * `0.17.0 <releases/dulwich-0.17.0.tar.gz>`_ (`0.17.0 GPG signature <releases/dulwich-0.17.0.tar.gz.asc>`_)
  * `0.16.3 <releases/dulwich-0.16.3.tar.gz>`_ (`0.16.3 GPG signature <releases/dulwich-0.16.3.tar.gz.asc>`_)
  * `0.16.2 <releases/dulwich-0.16.2.tar.gz>`_ (`0.16.2 GPG signature <releases/dulwich-0.16.2.tar.gz.asc>`_)
  * `0.16.1 <releases/dulwich-0.16.1.tar.gz>`_ (`0.16.1 GPG signature <releases/dulwich-0.16.1.tar.gz.asc>`_)
  * `0.16.0 <releases/dulwich-0.16.0.tar.gz>`_ (`0.16.0 GPG signature <releases/dulwich-0.16.0.tar.gz.asc>`_)
  * `0.15.0 <releases/dulwich-0.15.0.tar.gz>`_ (`0.15.0 GPG signature <releases/dulwich-0.15.0.tar.gz.asc>`_)
  * `0.14.1 <releases/dulwich-0.14.1.tar.gz>`_ (`0.14.1 GPG signature <releases/dulwich-0.14.1.tar.gz.asc>`_)
  * `0.14.0 <releases/dulwich-0.14.0.tar.gz>`_ (`0.14.0 GPG signature <releases/dulwich-0.14.0.tar.gz.asc>`_)
  * `0.13.0 <releases/dulwich-0.13.0.tar.gz>`_ (`0.13.0 GPG signature <releases/dulwich-0.13.0.tar.gz.asc>`_)
  * `0.12.0 <releases/dulwich-0.12.0.tar.gz>`_ (`0.12.0 GPG signature <releases/dulwich-0.12.0.tar.gz.asc>`_)
  * `0.11.2 <releases/dulwich-0.11.2.tar.gz>`_ (`0.11.2 GPG signature <releases/dulwich-0.11.2.tar.gz.asc>`_)
  * `0.11.1 <releases/dulwich-0.11.1.tar.gz>`_ (`0.11.1 GPG signature <releases/dulwich-0.11.1.tar.gz.asc>`_)
  * `0.11.0 <releases/dulwich-0.11.0.tar.gz>`_ (`0.11.0 GPG signature <releases/dulwich-0.11.0.tar.gz.asc>`_)
  * `0.10.1 <releases/dulwich-0.10.1.tar.gz>`_ (`0.10.1 GPG signature <releases/dulwich-0.10.1.tar.gz.asc>`_)
  * `0.10.0 <releases/dulwich-0.10.0.tar.gz>`_ (`0.10.0 GPG signature <releases/dulwich-0.10.0.tar.gz.asc>`_)
  * `0.9.10 <releases/dulwich-0.9.10.tar.gz>`_ (`0.9.10 GPG signature <releases/dulwich-0.9.10.tar.gz.asc>`_)
  * `0.9.9 <releases/dulwich-0.9.9.tar.gz>`_ (`0.9.9 GPG signature <releases/dulwich-0.9.9.tar.gz.asc>`_)
  * `0.9.8 <releases/dulwich-0.9.8.tar.gz>`_ (`0.9.8 GPG signature <releases/dulwich-0.9.8.tar.gz.asc>`_)
  * `0.9.7 <releases/dulwich-0.9.7.tar.gz>`_ (`0.9.7 GPG signature <releases/dulwich-0.9.7.tar.gz.asc>`_)
  * `0.9.6 <releases/dulwich-0.9.6.tar.gz>`_ (`0.9.6 GPG signature <releases/dulwich-0.9.6.tar.gz.asc>`_)
  * `0.9.5 <releases/dulwich-0.9.5.tar.gz>`_ (`0.9.5 GPG signature <releases/dulwich-0.9.5.tar.gz.asc>`_)
  * `0.9.4 <releases/dulwich-0.9.4.tar.gz>`_ (`0.9.4 GPG signature <releases/dulwich-0.9.4.tar.gz.asc>`_)
  * `0.9.3 <releases/dulwich-0.9.3.tar.gz>`_
  * `0.9.2 <releases/dulwich-0.9.2.tar.gz>`_
  * `0.9.1 <releases/dulwich-0.9.1.tar.gz>`_
  * `0.9.0 <releases/dulwich-0.9.0.tar.gz>`_ (`0.9.0 GPG signature <releases/dulwich-0.9.0.tar.gz.asc>`_)
  * `0.8.7 <releases/dulwich-0.8.7.tar.gz>`_ (`0.8.7 GPG signature <releases/dulwich-0.8.7.tar.gz.asc>`_)
  * `0.8.6 <releases/dulwich-0.8.6.tar.gz>`_ (`0.8.6 GPG signature <releases/dulwich-0.8.6.tar.gz.asc>`_)
  * `0.8.5 <releases/dulwich-0.8.5.tar.gz>`_ (`0.5.5 GPG signature <releases/dulwich-0.8.5.tar.gz.asc>`_)
  * `0.8.4 <releases/dulwich-0.8.4.tar.gz>`_ (`0.8.4 GPG signature <releases/dulwich-0.8.4.tar.gz.asc>`_)
  * `0.8.3 <releases/dulwich-0.8.3.tar.gz>`_ (`0.8.3 GPG signature <releases/dulwich-0.8.3.tar.gz.asc>`_)
  * `0.8.2 <releases/dulwich-0.8.2.tar.gz>`_ (`0.8.2 GPG signature <releases/dulwich-0.8.2.tar.gz.asc>`_)
  * `0.8.1 <releases/dulwich-0.8.1.tar.gz>`_ (`0.8.1 GPG signature <releases/dulwich-0.8.1.tar.gz.asc>`_)
  * `0.8.0 <releases/dulwich-0.8.0.tar.gz>`_ (`0.8.0 GPG signature <releases/dulwich-0.8.0.tar.gz.asc>`_)
  * `0.7.1 <releases/dulwich-0.7.1.tar.gz>`_ (`0.7.1 GPG signature <releases/dulwich-0.7.1.tar.gz.asc>`_)
  * `0.7.0 <releases/dulwich-0.7.0.tar.gz>`_ (`0.7.0 GPG signature <releases/dulwich-0.7.0.tar.gz.asc>`_)
  * `0.6.2 <releases/dulwich-0.6.2.tar.gz>`_ (`0.6.2 GPG signature <releases/dulwich-0.6.2.tar.gz.asc>`_)
  * `0.6.1 <releases/dulwich-0.6.1.tar.gz>`_ (`0.6.1 GPG signature <releases/dulwich-0.6.1.tar.gz.asc>`_)
  * `0.6.0 <releases/dulwich-0.6.0.tar.gz>`_ (`0.6.0 GPG signature <releases/dulwich-0.6.0.tar.gz.asc>`_)
  * `0.5.0 <releases/dulwich-0.5.0.tar.gz>`_ (`0.5.0 GPG signature <releases/dulwich-0.5.0.tar.gz.asc>`_)
  * `0.4.1 <releases/dulwich-0.4.1.tar.gz>`_ (`0.4.1 GPG signature <releases/dulwich-0.4.1.tar.gz.asc>`_)
  * `0.4.0 <releases/dulwich-0.4.0.tar.gz>`_ (`0.4.0 GPG signature <releases/dulwich-0.4.0.tar.gz.asc>`_)
  * `0.3.3 <releases/dulwich-0.3.3.tar.gz>`_ (`0.3.3 GPG signature <releases/dulwich-0.3.3.tar.gz.asc>`_)
  * `0.3.2 <releases/dulwich-0.3.2.tar.gz>`_ (`0.3.2 GPG signature <releases/dulwich-0.3.2.tar.gz.asc>`_)
  * `0.3.1 <releases/dulwich-0.3.1.tar.gz>`_ (`0.3.1 GPG signature <releases/dulwich-0.3.1.tar.gz.asc>`_)
  * `0.3.0 <releases/dulwich-0.3.0.tar.gz>`_ (`0.3.0 GPG signature <releases/dulwich-0.3.0.tar.gz.asc>`_)
  * `0.2.1 <releases/dulwich-0.2.1.tar.gz>`_ (`0.2.1 GPG signature <releases/dulwich-0.2.1.tar.gz.asc>`_)
  * `0.2.0 <releases/dulwich-0.2.0.tar.gz>`_ (`0.2.0 GPG signature <releases/dulwich-0.2.0.tar.gz.asc>`_)
  * `0.1.0 <releases/dulwich-0.1.0.tar.gz>`_ (`0.1.0 GPG signature <releases/dulwich-0.1.0.tar.gz.asc>`_)

