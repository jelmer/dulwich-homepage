:title: Getting started
:save_as: getting-started.html

Dulwich comes with both a lower-level API and higher-level plumbing ("porcelain").

For example, to use the lower level API to access the commit message of the
last commit::

    >>> from dulwich.repo import Repo
    >>> r = Repo('.')
    >>> r.head()
    '57fbe010446356833a6ad1600059d80b1e731e15'
    >>> c = r[r.head()]
    >>> c
    <Commit 015fc1267258458901a94d228e39f0a378370466>
    >>> c.message
    'Add note about encoding.\n'

And to print it using porcelain::

    >>> from dulwich import porcelain
    >>> porcelain.log('.', max_entries=1)
    --------------------------------------------------
    commit: 57fbe010446356833a6ad1600059d80b1e731e15
    Author: Jelmer Vernooĳ <jelmer@jelmer.uk>
    Date:   Sat Apr 29 2017 23:57:34 +0000

    Add note about encoding.

Further documentation
---------------------

The dulwich documentation can be found `on the web <https://www.dulwich.io/docs/>`_.

`API reference <https://www.dulwich.io/apidocs>`_.
