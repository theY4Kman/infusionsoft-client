infusionsoft-client
===================

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://github.com/theY4Kman/infusionsoft-client/blob/master/LICENSE
    
.. image:: https://badges.gitter.im/they4kman/infusionsoft-client.png
    :target: https://gitter.im/infusionsoft-client/Lobby
    
.. image:: https://badge.fury.io/py/infusionsoft-client.svg
    :target: https://badge.fury.io/py/infusionsoft-client

A simple-to-use `Infusionsoft XML-RPC API <https://developer.infusionsoft.com/docs/xml-rpc/>`_ client, with included stubs for code sense. Python 3.5+ only (but pull requests welcome :smirk:).



Installation
------------

.. code-block:: bash

    pip install infusionsoft-client



Quickstart
----------

First, initialize the client with your app name and API key:

.. code-block:: python

    import infusionsoft
    infusionsoft.initialize('myapp', '098f6bcd4621d373cade4e832627b4f6')


And use the ``infusionsoft`` like a regular `xmlrpc.client.ServerProxy <https://docs.python.org/3/library/xmlrpc.client.html>`_:

.. code-block:: python

    import infusionsoft
    contact_id = infusionsoft.ContactService.add({'FirstName': 'Johnny'})



Setting XML-RPC Client Options
------------------------------

Any extra kwargs passed to ``initialize()`` will be passed along to ``xmlrpc.client.ServerProxy``.

.. code-block:: python

    import infusionsoft
    infusionsoft.initialize('myapp', '098f6bcd4621d373cade4e832627b4f6', use_builtin_types=True)

Some kwargs of interest are:

 - ``use_builtin_types``: whether to utilize native Python types, rather than wrappers such as ``xmlrpc.client.DateTime`` or ``xmlrpc.client.Binary``. **I recommend turning this on**. It will be turned on by default in the next major/breaking release.
 - ``verbose``: set to ``True`` to print out the request and response bodies for each RPC call.
 - ``allow_none``: whether to allow ``None`` to be sent over the wire. Infusionsoft, in general, doesn't allow ``None`` (which is ``nil`` in XML-RPC parlance). If a field in a response is null, Infusionsoft will simply not send it.

See `the docs <https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy>`_ for more info.



Usage with Django
-----------------

``infusionsoft-client`` includes a Django integration out of the box. Just add it to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'infusionsoft.contrib.django',
    )

And add your app name and API key to your settings:

.. code-block:: python

    INFUSIONSOFT_APP_NAME = 'myapp'
    INFUSIONSOFT_API_KEY = '098f6bcd4621d373cade4e832627b4f6'


Pass extra configuration to the XML-RPC client with ``INFUSIONSOFT_CLIENT_OPTIONS``:

.. code-block:: python

    INFUSIONSOFT_CLIENT_OPTIONS = {
        'use_builtin_types': True,
    }



Getting All Rows of a Query
---------------------------

Some API calls are paginated, and require multiple calls to retrieve all results. This can be a pain, and you may find yourself writing the same code over and over. To this end, ``infusionsoft-client`` provides a ``consume()`` generator function, which will consume all pages of any query function.

To use it, create a lambda (or regular) function taking ``page`` and ``limit`` as arguments which performs your paginated API call, and pass it to ``consume()``:

.. code-block:: python

    import infusionsoft
    from infusionsoft.query import consume

    query_fn = lambda page, limit: (
        infusionsoft.DataService.query('mytable', limit, page, ['Id']))

    # Use with a for-loop, to avoid storing all rows in memory:
    for row in consume(query_fn):
        do_stuff(row)

    # Or retrieve all rows at once
    all_rows = list(consume(query_fn))


Generate Code Stubs
-------------------

Shipped with ``infusionsoft-client`` is code to download the official Infusionsoft XML-RPC docs, parse them with `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_, and generate Python 3.5-compatible stubs for all methods.

To generate these yourself, first install the extra requirements:

.. code-block:: bash

    pip install -r stub-requirements.txt

Then run the ``generate_stubs()`` function, which will return a string:

.. code-block:: python

    from infusionsoft.gen_stubs import generate_stubs
    source = generate_stubs()
