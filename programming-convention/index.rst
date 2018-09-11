.. _Software Engineering Conventions:

********************************
Software Engineering Conventions
********************************


PEP 8 - Style Guide for Python Code
===================================

Tabs or spaces?
---------------
* 4 spacje
* IDE zamienia tab na 4 spacje

Line length
-----------
* 79 znaków
* soft wrap
* co z monitorami 4k?
* najbardziej kontrowersyjna klauzula

File encoding
-------------
* UTF-8

Comments
--------
* Better named functions and variables

Commented code?
---------------
* NO!
* Never commit files with commented code

Author name or revision version
-------------------------------
* Do not put author name or revision version to the files
* Version Control System is responsible for that

Naming convention
-----------------
* ``zmienne``
* ``STALE``
* ``NazwyKlas``
* ``nazwy_metod()`` i ``nazwy_funkcji()``
* ``nazwymodulow``, ``nazwy_modulow``
* ``self``
* ``cls``

Using ``__`` and ``_`` in names
-------------------------------

Single or double quotes?
------------------------
* Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
* Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
* Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia.
* Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.
* Ma to znaczenie przy ``doctest``, który zawsze korzysta z pojedynczych i rzuca errorem jak są podwójne

.. code-block:: python

    print('it\'s José\'s book')
    print("it's José's book")

.. code-block:: python

    print('<a href="http://python.astrotech.io">Python and Machine Learning</a>')

Indents
-------
.. literalinclude:: src/convention-indent-good.py
    :language: python
    :caption: Good

.. literalinclude:: src/convention-indent-bad.py
    :language: python
    :caption: Bad

Brackets
--------
.. code-block:: python

    vector = [
        1, 2, 3,
        4, 5, 6,
    ]

    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )

    vector = [
        1, 2, 3,
        4, 5, 6]

    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f')

Line continuation
-----------------
Linie możemy łamać poprzez stawianie znaku ukośnika ``\`` na końcu:

.. code-block:: python

    with open('/path/to/some/file/you/want/to/read') as file1, \
            open('/path/to/some/file/being/written', mode='w') as file2:
        content = file1.read()
        file2.write(content)

.. code-block:: python

    class Server:
        def __init__(self, username, password, host='localhost'
                     port=80, secure=False):

            if not instance(username, str) or not instance(password, str) or
                    not instance(host, str) or not instance(secure, bool) or
                    (not instance(port, int) and 0 < port <= 65535):
                raise TypeError(f'One of your parameters is incorrect type')
                
         def __str__(self):
            if secure:
                protocol = 'https'
            else:
                protocol = 'http'

            return f'{protocol}://{self.username}:{self.password}@{self.host}:{self.port}/'

    server = Server(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        secure=True,
    )

Blank lines
-----------
.. code-block:: python

    class Server:
        def __init__(self, username, password, host='localhost'
                     port=80, secure=False):

            if not instance(username, str):
                raise TypeError(f'Username must be str')

            if not instance(password, str):
                raise TypeError(f'Password must be str')

            if not instance(port, int):
                raise TypeError(f'Port must be int')
            elif: 0 < port <= 65535
                raise ValueError(f'Port must be 0-65535')

        def __str__(self):
            if secure:
                protocol = 'https'
            else:
                protocol = 'http'

            return f'{protocol}://{self.username}:{self.password}@{self.host}:{self.port}/'

Whitespace in function calls
----------------------------
.. code-block:: python

    spam(ham[1], {eggs: 2})        # Good
    spam( ham[ 1 ], { eggs: 2 } )  # Bad

.. code-block:: python

    spam(1)     # Good
    spam (1)    # Bad

.. code-block:: python

    do_one()    # Good
    do_two()    # Good
    do_three()  # Good

    do_one(); do_two(); do_three()                  # Bad

    do_one(); do_two(); do_three(long, argument,    # Bad
                                 list, like, this)  # Bad

Whitespace in slices
--------------------
.. code-block:: python

    ham[1:9]                          # Good
    ham[1:9:3]                        # Good
    ham[:9:3]                         # Good
    ham[1::3]                         # Good
    ham[1:9:]                         # Good

    ham[1: 9]                         # Bad
    ham[1 :9]                         # Bad
    ham[1:9 :3]                       # Bad

.. code-block:: python

    ham[lower:upper]                  # Good
    ham[lower:upper:]                 # Good
    ham[lower::step]                  # Good

    ham[lower : : upper]              # Bad

.. code-block:: python

    ham[lower+offset : upper+offset]  # Good
    ham[: upper_fn(x) : step_fn(x)]   # Good
    ham[:: step_fn(x)]                # Good

    ham[lower + offset:upper + offset]    # Bad

.. code-block:: python

    ham[:upper]             # Good
    ham[ : upper]           # Bad
    ham[ :upper]            # Bad

Whitespace in assignments
-------------------------
.. code-block:: python

    x = 1                   # Good
    y = 2                   # Good
    long_variable = 3       # Good

    x             = 1       # Bad
    y             = 2       # Bad
    long_variable = 3       # Bad

.. code-block:: python

    i = i + 1               # Good
    i=i+1                   # Bad

.. code-block:: python

    submitted += 1          # Good
    submitted +=1           # Bad

Whitespace in math operators
----------------------------
.. code-block:: python

    x = x*2 - 1             # Good
    x = x * 2 - 1           # Bad

.. code-block:: python

    hypot2 = x*x + y*y      # Good
    hypot2 = x * x + y * y  # Bad

.. code-block:: python

    c = (a+b) * (a-b)      # Good
    c = (a + b) * (a - b)  # Bad

Whitespace in accessors
-----------------------
.. code-block:: python

    dct['key'] = lst[index]     # Good
    dct ['key'] = lst[ index ]  # Bad

Whitespace in functions
-----------------------
:Good:
    .. code-block:: python

        def complex(real, imag=0.0):
            return magic(r=real, i=imag)

:Bad:
    .. code-block:: python

        def complex(real, imag = 0.0):
            return magic(r = real, i = imag)

Whitespace in conditionals
--------------------------
:Good:
    .. code-block:: python

        if foo == 'blah':
            do_blah_thing()

:Bad:
    .. code-block:: python

        if foo == 'blah': do_blah_thing()

        if foo == 'blah': one(); two(); three()

        if foo == 'blah': do_blah_thing()
        else: do_non_blah_thing()

Whitespace in exceptions
------------------------
:Good:
    .. code-block:: python

        try:
            do_something()
        except Exception:
            pass

:Bad:
    .. code-block:: python

        try: something()
        finally: cleanup()

Conditionals
------------
:Good:
    .. code-block:: python

        if greeting:
            pass

:Bad:
    .. code-block:: python

        if greeting == True:
            pass

        if greeting is True:
            pass


Negative Conditionals
---------------------
:Good:
    .. code-block:: python

        if name is not None:
            pass

:Bad:
    .. code-block:: python

        if not name is None:  # if (! name == null) {}
            pass

    .. code-block:: python

        usernames = {'José', 'Max', 'Иван'}

        # if (! usernames.contains('José')) {}
        if not 'José' in usernames:
            print('I do not know you')
        else:
            print('Hello my friend')

Checking if not empty
---------------------
:Good:
    .. code-block:: python

        if sequence:
            pass

        if not sequence:
            pass

:Bad:
    .. code-block:: python

        if len(sequence):
            pass

        if not len(sequence):
            pass

Explicit return
---------------
:Good:
    .. code-block:: python

        def foo(x):
            if x >= 0:
                return math.sqrt(x)
            else:
                return None

:Bad:
    .. code-block:: python

        def foo(x):
            if x >= 0:
                return math.sqrt(x)

Explicit return value
---------------------
:Good:
    .. code-block:: python

        def bar(x):
            if x < 0:
                return None
            return math.sqrt(x)
:Bad:
    .. code-block:: python

        def bar(x):
            if x < 0:
                return
            return math.sqrt(x)

Imports
-------
* Każdy z importów powinien być w osobnej linii
* importy systemowe na górze
* importy bibliotek zewnętrznych poniżej systemowych
* importy własnych modułów poniżej bibliotek zewnętrznych
* jeżeli jest dużo importów, pomiędzy grupami powinna być linia przerwy

:Good:
    .. code-block:: python

        import os
        import sys
        from random import shuffle
        from subprocess import Popen
        from subprocess import PIPE
        import requests
        import numpy as np

    .. code-block:: python

        import os
        import sys
        from random import shuffle
        from subprocess import Popen, PIPE
        import requests
        import numpy as np

:Bad:
    .. code-block:: python

        import sys, os, requests, numpy

    .. code-block:: python

        import sys, os
        import requests, numpy

Whitespace with type annotations
--------------------------------
:Good:
    .. code-block:: python

        def function(first: str):
            pass

        def function(first: str = None):
            pass

        def function() -> None:
            pass

        def function(first: str, second: str = None, limit: int = 1000) -> int:
            pass

:Bad:
    .. code-block:: python

        def function(first: str=None):
            pass

        def function(first:str):
            pass

        def function(first: str)->None:
            pass


PEP 20 - The Zen of Python
==========================
.. code-block:: python

    import this

Most important rules
--------------------

English
^^^^^^^
* Explicit is better than implicit.
* Simple is better than complex.
* Readability counts.
* Special cases aren't special enough to break the rules.
* If the implementation is hard to explain, it's a bad idea.

Polish
^^^^^^
* Wyrażone wprost jest lepsze niż domniemane.
* Proste jest lepsze niż złożone.
* Czytelność się liczy.
* Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.
* Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.

Full Text
---------

English
^^^^^^^
* Beautiful is better than ugly.
* **Explicit is better than implicit.**
* **Simple is better than complex.**
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* **Readability counts.**
* **Special cases aren't special enough to break the rules.**
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* **If the implementation is hard to explain, it's a bad idea.**
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

Polish
^^^^^^
* Piękne jest lepsze niż brzydkie.
* **Wyrażone wprost jest lepsze niż domniemane.**
* **Proste jest lepsze niż złożone.**
* Złożone jest lepsze niż skomplikowane.
* Płaskie jest lepsze niż wielopoziomowe.
* Rzadkie jest lepsze niż gęste.
* **Czytelność się liczy.**
* **Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.**
* Choć praktyczność przeważa nad konsekwencją.
* Błędy zawsze powinny być sygnalizowane.
* Chyba że zostaną celowo ukryte.
* W razie niejasności powstrzymaj pokusę zgadywania.
* Powinien być jeden -- i najlepiej tylko jeden -- oczywisty sposób na zrobienie danej rzeczy.
* Choć ten sposób może nie być oczywisty jeśli nie jest się Holendrem.
* Teraz jest lepsze niż nigdy.
* Chociaż nigdy jest często lepsze niż natychmiast.
* **Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.**
* Jeśli rozwiązanie jest łatwo wyjaśnić, to może ono być dobrym pomysłem.
* Przestrzenie nazw to jeden z niesamowicie genialnych pomysłów -- miejmy ich więcej!


Magic number i magic string
===========================
* NO!


``pycodestyle``
===============
* Previously known as ``pep8``
* Python style guide checker.
* ``pycodestyle`` is a tool to check your Python code against some of the style conventions in ``PEP 8``
* Plugin architecture: Adding new checks is easy
* Parseable output: Jump to error location in your editor
* Small: Just one Python file, requires only stdlib
* Comes with a comprehensive test suite

Installation
------------
.. code-block:: console

    pip install pycodestyle

Usage
-----
.. code-block:: console

    pycodestyle FILENAME.py

.. code-block:: console

    pycodestyle DIRECTORY/*.py

.. code-block:: console

    pycodestyle DIRECTORY/

.. code-block:: console

    pycodestyle --statistics -qq DIRECTORY/

.. code-block:: console

    pycodestyle --show-source --show-pep8 FILENAME.py

Configuration
-------------
* ``setup.cfg``

.. code-block:: ini

    [pycodestyle]
    max-line-length = 120
    ignore = E402,W391


Assignment
==========

Cleanup your file
-----------------
#. Install ``pycodestyle``
#. Run ``pycodestyle`` on your last script
#. Fix all errors
#. Run ``pycodestyle`` on directory with all of your scripts
#. Fix all errors

:About:
    * Lines of code to write: 2 lines
    * Estimated time of completion: 5 min

:Co zadanie sprawdza:
    * Umiejętność czytania komunikatów
    * Umiejętność pracy z terminalem
    * Utrzymywanie konwencji PEP8
