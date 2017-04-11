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



Getting All Rows of a Query
---------------------------

Some API calls are paginated, and require multiple calls to retrieve all results. This can be a pain, and you may find yourself writing the same code over and over. To this end, ``infusionsoft-client`` provides a ``consume()`` generator function, which will consume all pages of any query function.

To use it, create a lambda (or regular) function taking ``page`` and ``limit`` as arguments which performs your paginated API call, and pass it to ``consume()``:

.. code-block:: python

    import infusionsoft
    from infusionsoft.query import consume

    query_fn = lambda page, limit: infusionsoft.DataService.query('mytable', limit, page, ['Id'])

    # Use with a for-loop, to avoid storing all rows in memory:
    for row in consume(query_fn):
        do_stuff(row)

    # Or retrieve all rows at once
    all_rows = list(consume(query_fn))



Usage with Django
-----------------

``infusionsoft-client`` doesn't require anything special to work with Django, but it does offer recommendations.

First, put your Infusionsoft API URL and key in your settings.py:

.. code-block:: python

    INFUSIONSOFT_API_URL = 'https://myapp.infusionsoft.com/api/xmlrpc'
    INFUSIONSOFT_API_KEY = '098f6bcd4621d373cade4e832627b4f6'

Then call ``initialize()`` in your Django ``AppConfig.ready`` hook in your `apps.py <https://docs.djangoproject.com/en/1.10/ref/applications/>`_ (Django 1.9+):

.. code-block:: python

    from django.apps import AppConfig
    from django.conf import settings

    import infusionsoft

    class MyAppConfig(AppConfig): # Our app config class
        name = 'my_app'
        verbose_name = 'My Application'

        def ready(self):
            infusionsoft.initialize(settings.INFUSIONSOFT_API_URL,
                                    settings.INFUSIONSOFT_API_KEY)


Note: this apps.py should usually live in the same folder as your root urls.py. If this is the first you're creating your apps.py (which is not necessary, usually), you'll also need to put this line in your package's __init__.py:

.. code-block:: python

    default_app_config = 'my_app.apps.MyAppConfig'

If you're on Django 1.8 or below, you can put the ``initialize()`` call at the bottom of your models.py:

.. code-block:: python

    from django.conf import settings
    from django.db import models

    import infusionsoft

    # Your models here...

    infusionsoft.initialize(settings.INFUSIONSOFT_API_URL,
                            settings.INFUSIONSOFT_API_KEY)


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
