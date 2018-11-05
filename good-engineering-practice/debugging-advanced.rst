******************
Advanced Debugging
******************


``json.tool``
=============
.. code-block:: console

    $ curl -s http://localhost:8000/contact/api/
    {"contacts": [{"id": 1, "created": "2018-06-13T09:57:55.405Z", "modified": "2018-06-13T10:16:13.975Z", "reporter_id": 1, "is_deleted": false, "first_name": "José", "last_name": "Jiménez", "date_of_birth": "1969-07-24", "email": "jose.jimenez@nasa.gov", "bio": "", "image": "33950257662_d7561fb140_o.jpg", "status": null, "gender": null}, {"id": 2, "created": "2018-06-13T10:26:46.948Z", "modified": "2018-06-13T10:26:46.948Z", "reporter_id": 1, "is_deleted": false, "first_name": "Mark", "last_name": "Watney", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}, {"id": 3, "created": "2018-06-13T10:26:55.820Z", "modified": "2018-06-13T10:26:55.820Z", "reporter_id": 1, "is_deleted": false, "first_name": "Иван", "last_name": "Иванович", "date_of_birth": null, "email": null, "bio": "", "image": "", "status": null, "gender": null}]}

.. code-block:: console

    $ curl -s http://localhost:8000/contact/api/ |python -m json.tool
    {
        "contacts": [
            {
                "id": 1,
                "created": "2018-06-13T09:57:55.405Z",
                "modified": "2018-06-13T10:16:13.975Z",
                "reporter_id": 1,
                "is_deleted": false,
                "first_name": "José",
                "last_name": "Jiménez",
                "date_of_birth": "1969-07-24",
                "email": "jose.jimenez@nasa.gov",
                "bio": "",
                "image": "33950257662_d7561fb140_o.jpg",
                "status": null,
                "gender": null
            },
            {
                "id": 2,
                "created": "2018-06-13T10:26:46.948Z",
                "modified": "2018-06-13T10:26:46.948Z",
                "reporter_id": 1,
                "is_deleted": false,
                "first_name": "Mark",
                "last_name": "Watney",
                "date_of_birth": null,
                "email": null,
                "bio": "",
                "image": "",
                "status": null,
                "gender": null
            },
            {
                "id": 3,
                "created": "2018-06-13T10:26:55.820Z",
                "modified": "2018-06-13T10:26:55.820Z",
                "reporter_id": 1,
                "is_deleted": false,
                "first_name": "Иван",
                "last_name": "Иванович",
                "date_of_birth": null,
                "email": null,
                "bio": "",
                "image": "",
                "status": null,
                "gender": null
            },
        ]
    }


Using ``pdb``
=============
.. code-block:: python

    print('José Jiménez')
    import pdb; pdb.set_trace()
    print('Mark Watney')


``breakpoint()``
================
.. code-block:: python

    print('José Jiménez')
    breakpoint()
    print('Mark Watney')

* ``sys.breakpointhook()``
* ``sys.__breakpointhook__``
* By default, ``sys.breakpointhook()`` implements the actual importing and entry into ``pdb.set_trace()``.
* It can be set to a different function to change the debugger that ``breakpoint()`` enters.

.. code-block:: python

    os.environ['PYTHONBREAKPOINT'] = 'foo.bar.baz'
    breakpoint()    # Imports foo.bar and calls foo.bar.baz()


Using debugger in IDE
=====================

Break Point
-----------

View Breakpoints
~~~~~~~~~~~~~~~~

Mute Breakpoints
~~~~~~~~~~~~~~~~

Poruszanie się
--------------

Step Over
~~~~~~~~~

Step Into My Code
~~~~~~~~~~~~~~~~~

Force Step Into
~~~~~~~~~~~~~~~

Show Execution Point
~~~~~~~~~~~~~~~~~~~~

Step Out
~~~~~~~~

Run to Cursor
~~~~~~~~~~~~~

Resume Program
~~~~~~~~~~~~~~

New Watch
~~~~~~~~~

Frames
------

Previous Frame
~~~~~~~~~~~~~~

Next Frame
~~~~~~~~~~

Threads
~~~~~~~

Scope
-----

Special Variables
~~~~~~~~~~~~~~~~~

* ``__file__``
* ``__name__``
* ``__builtins__``
* ``__doc__``
* ``__loader__``
* ``__spec__``
* ``__package__``

Moduły
~~~~~~

Stałe
~~~~~

Zmienne
~~~~~~~

Wartości funkcji
~~~~~~~~~~~~~~~~

Debugging i Wątki
=================

Debugging i Procesy
===================

Debugging aplikacji sieciowych
==============================
.. code-block:: python

    import logging

    logging.getLogger('requests').setLevel(logging.DEBUG)

Wyciszanie logowania
--------------------
.. code-block:: python

    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime).19s] [%(levelname)s] %(message)s')

    logging.getLogger('requests').setLevel(logging.WARNING)
    log = logging.getLogger(__name__)

    log.debug('to jest moja debugowa wiadomosc')


Assignment
==========

Own ``doctest``
---------------
#. Dla kodu z listingu :numref:`listing-debugging-docstring`
#. Napisz własną uproszczoną implementację ``doctest``
#. Dla uproszczenia przyjmij, że zwracana zawsze będzie tylko jedna linia (bezpośrednio poniżej testu)

.. literalinclude:: src/debugging-docstring.py
    :name: listing-debugging-docstring
    :language: python
    :caption: Debugging with docstring
