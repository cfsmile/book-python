.. _Control Flow Statements:

***********************
Control Flow Statements
***********************


Conditional Statements
======================

``if``
------
* Simple syntax:

    .. code-block:: python

        if True:
            print('First line of the true statement')

* Multiline blocks:

    .. code-block:: python

        if True:
            print('First line of the true statement')
            print('Second line of the true statement')
            print('Third line of the true statement')

* Negative values:

    * ``False``
    * ``0``
    * ``0.0``
    * ``()`` - empty ``tuple``
    * ``{}`` - empty ``dict``
    * ``[]`` - empty ``list``
    * ``''`` - empty ``str``
    * ``set()`` - empty ``set``
    * ``None``

* Positive values: any other values
* Checking for simple value

    .. code-block:: python

        name = 'José Jiménez'

        if name == 'José Jiménez':
            print('My name... José Jiménez')

* Checking if value is in range

    .. code-block:: python

        age = 7

        if 0 <= age < 18:
            print('Age is between [0, 18)')

* Checking if has value

    .. code-block:: python

        name = None

        if name:
            print(f'My name... {name}')
        else:
            print('Name is not defined')

``else``
--------
* Optional
* Executed when condition is not met
* Checking if variable is certain value:

    .. code-block:: python

        name = 'José Jiménez'

        if name == 'José Jiménez':
            print('My name... José Jiménez')
        else:
            print('Your name is different')

* Multiline blocks:

    .. code-block:: python

        if True:
            print('First line of the true statement')
            print('Second line of the true statement')
            print('Third line of the true statement')
        else:
            print('First line of the false statement')
            print('Second line of the false statement')
            print('Third line of the false statement')

Inline ``if``
-------------
.. code-block:: python

    ip = '127.0.0.1'

    if '.' in ip:
        protocol = 'IPv4'
    else:
        protocol = 'IPv6'

.. code-block:: python

    ip = '127.0.0.1'

    protocol = 'IPv4' if '.' in ip else 'IPv6'


``elif`` and ``switch``
=======================

``elif``
--------
* Used to check for additional condition if first is not met
* In other languages is known as ``else if``

.. code-block:: python

    country = 'Poland'

    if country == 'USA':
        print('Hello')
    elif country == 'Germany':
        print('Guten tag!')
    elif country == 'Poland':
        print('Witaj!')
    else:
        print('...')

No ``switch`` statement?!
-------------------------
* ``switch`` in Object Oriented Programming is considered a bad practise
* `PEP 275 <https://www.python.org/dev/peps/pep-0275/>`_

.. code-block:: python

    if name == 'José Jiménez':
        print('My name... José Jiménez')
    elif name == 'Иван Иванович':
        print('Your name is Иван Иванович')
    elif name == 'Mark Watney':
        print('Your name is Mark Watney')
    else:
         print('Your name is other')

.. code-block:: python

    switch = {
        'English': 'Hello',
        'Russian': 'Здравствуйте',
        'German': 'Guten Tag',
        'Polish': 'Witaj',
    }

    what = 'French'
    switch.get(what, "Sorry, I don't know")
    # "Sorry, I don't know"

.. code-block:: python

    def switch(key):
        return {
            'English': 'Hello',
            'Russian': 'Здравствуйте',
            'German': 'Guten Tag',
            'Polish': 'Witaj',
        }.get(key, "Sorry, I don't know")

    switch('Russian')       # 'Здравствуйте'
    switch('French')        # "Sorry, I don't know"


Complex expressions
===================

``and``
-------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' and last_name == 'Jiménez':
        print('My name... José Jiménez')
    else:
        print('Your name is different')


``or``
------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' or first_name == 'Max':
        print('Your name is José or Max')
    else:
        print('Your name is different')


mixed
-----
* Use parenthesis for explicit order

    .. code-block:: python

        first_name = 'José'
        last_name = 'Jiménez'

        if (first_name == 'José' and last_name == 'Jiménez')
                or (first_name == 'Mark' and last_name == 'Watney'):
            print('Your name is José Jiménez or Mark Watney')
        else:
            print('Your name is different')


Control Statements
==================

``in``
------
* works with ``tuple``, ``dict``, ``list``, ``set`` and ``str``
* ``in`` checks whether value is in other collection

    .. code-block:: python

        usernames = {'José Jiménez', 'Pan Twardowski', 'Mark Watney'}

        if 'José Jiménez' in usernames:
            print(True)
        else:
            print(False)

* ``in`` checks whether ``str`` is a part of another ``str``

    .. code-block:: python

        text = 'My name... José Jiménez'

        if 'José' in text:
            print(True)
        else:
            print(False)

``not``
-------
* ``not`` negates (logically inverts) condition

.. code-block:: python

    name = None

    if not name:
        print('Name is not defined')

.. code-block:: python

    usernames = {'José', 'Max', 'Иван'}

    if 'José' not in usernames:
        print('Not found')

``is``
------
.. code-block:: python

    name = None

    if name is None:
        print('Name is not defined')

.. code-block:: python

    name = None

    if name is not None:
        print(name)


Assignments
===========

Conditioning on user input
--------------------------
#. Napisz program, który poprosi użytkownika o wiek
#. Użytkownik będzie podawał tylko i wyłącznie ``int`` lub ``float``
#. Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest "dorosła" czy "niepełnoletnia"

:About:
    * Filename: ``ifelse_input.py``
    * Lines of code to write: 6 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie
    * Magic Number

Classification of blood pressure in adults
------------------------------------------
* Source: https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings

#. Poniższa tabelka przedstawia klasyfikację ciśnienia krwi, wg. American Heart Association

    .. csv-table:: Classification of blood pressure in adults
        :file: data/if-blood-pressure.csv
        :header-rows: 1

#. Użytkownik wprowadza ciśnienie w formacie ``XXX/YY``, gdzie:

    - ``XXX`` to wartość ciśnienia skurczowego (ang. *systolic*)
    - ``YY`` to wartość ciśnienia rozkurczowego (ang. *diastolic*)

#. Daj informację użytkownikowi o klasyfikacji ciśnienia
#. W przypadku gdy wartości ciśnienia skurczowego i ciśnienia rozkurczowego należą do różnych kategorii, należy przyjąć kategorię wyższą

:About:
    * Filename: ``ifelse_blood_pressure.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Rzutowanie i konwersja typów
    * Instrukcje warunkowe
    * Złożone instrukcje warunkowe
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Definiowanie zmiennych i stałych w programie
