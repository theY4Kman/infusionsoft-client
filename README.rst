infusionsoft-client
===================

A simple-to-use `Infusionsoft XML-RPC API <https://developer.infusionsoft.com/docs/xml-rpc/>`_ client, with included stubs for code sense. Python 3.5+ only (but pull requests welcome :smirk:).



Installation
------------

.. code-block:: bash

    pip install infusionsoft-api



Quickstart
----------

First, initialize the client with your API URL and API key:

.. code-block:: python

    import infusionsoft
    infusionsoft.initialize('https://myapp.infusionsoft.com/api/xmlrpc', '098f6bcd4621d373cade4e832627b4f6')


And use the ``infusionsoft`` like a regular `xmlrpc.client.ServerProxy <https://docs.python.org/3/library/xmlrpc.client.html>`_:

.. code-block:: python

    import infusionsoft
    contact_id = infusionsoft.ContactService.add({'FirstName': 'Johnny'})



Generate Code Stubs
-------------------

Shipped with ``infusionsoft-api`` is code to download the official Infusionsoft XML-RPC docs, parse them with `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_, and generate Python 3.5-compatible stubs for all methods.

To generate these yourself, first install the extra requirements:

.. code-block:: bash

    pip install -r stub-requirements.txt

Then run the ``generate_stubs()`` function, which will return a string:

.. code-block:: python

    from infusionsoft.gen_stubs import generate_stubs
    source = generate_stubs()
