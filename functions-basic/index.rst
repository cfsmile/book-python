.. _Function Basics:

***************
Function Basics
***************


Function definition
===================
* Funkcje pozwalają na wielokrotne używanie tego samego kodu.
* Znacznie poprawiają także czytelność kodu i go porządkują.

.. code-block:: python

    def hello():
        print('My name José Jiménez')

    hello()
    # José Jiménez

Returning values
================
* Słowo kluczowe ``return`` wskazuje funkcji jaką wartość ma dana funkcja zwrócić.
* Wykonanie linii ze słowem kluczowym ``return`` kończy wykonywanie funkcji.

.. code-block:: python

    def hello():
        return 'hello world'

    output = hello()

    print(output)
    # 'hello world'

.. code-block:: python

    def hello():
        return 'hello world'
        print('This will not be executed')

    output = hello()

    print(output)
    # 'hello world'

Returning simple types
----------------------
.. code-block:: python

    def function():
        return 42

    def function():
        return 13.37

    def function():
        return 'José Jiménez'

    def function():
        return (42, 13.37, 'José Jiménez')

    def function():
        return 42, 13.37, 'José Jiménez'

    def function():
        return [42, 13.37, 'foobar']

    def function():
        return {42, 13.37, 'José Jiménez'}

    def function():
        return {'first_name': 'José', 'last_name': 'Jiménez'}

    def function():
        return True

    def function():
        return None

    def function():
        print('hello')
        # Python will ``return None`` implicitly, if return is not specified

Returning nested types
----------------------
.. code-block:: python

    def function():
        return [
            {'astro': 'Peck'},
            {'astro': 'Иванович', 'agency': {'name': 'roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('mercury', 'apollo')},
        ]


Function arguments
==================
Argumenty funkcji to wartości na których ta funkcja wykonuje operacje. W idealnym przypadku wartość wyjściowa funkcji powinna zależeć jedynie od jej argumentów.

.. code-block:: python

    def add(a, b):
        return a + b

    add(1, 2)
    # 3

Type annotations
----------------
* Od Python 3.5
* Kod w języku python wykona się nawet jeśli typ nie zgadza się z adnotacją!
* Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
* Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add(1, 2.5)
    # 3.5

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add('José', 'Jiménez')
    # 'JoséJiménez'

.. note:: więcej na ten temat w rozdziale dotyczącym :numref:`Type Annotation`

Named arguments
---------------
* Każdy argument ma swoją nazwę przez którą uzyskujemy dostęp do wartości argumentu w ciele funkcji.
* Ta nazwa może też być używana do przypisania wartości przy wywołaniu funkcji.

.. code-block:: python

    def minus(a, b):
        return a - b

    minus(2, 1)      # 1
    minus(1, 2)      # -1
    minus(a=2, b=1)  # 1
    minus(b=1, a=2)  # 1
    minus(2, b=1)    # 1
    minus(a=2, 1)    # SyntaxError: positional argument follows keyword argument

Arguments with default value
----------------------------
* Argument funkcji może mieć wartość domyślną.
* Funkcja przyjmie tą wartość jeżeli użytkownik nie zdefiniuje tego argumentu.
* Argumenty z wartością domyślną muszą być skrajnie po prawej stronie.

.. code-block:: python

    def hello(name='José Jiménez'):
         print(name)

    hello('Иван Иванович')        # Иван Иванович
    hello(name='Иван Иванович')   # Иван Иванович
    hello()                       # José Jiménez

.. code-block:: python

    def server(username, password, host='127.0.0.1', port=80, ssl=False, keep_alive=1, persistent=False):
        print('Connecting...')

    server('admin', 'admin', 'localhost', 80, False, 1, True)

    server(host='localhost', username='admin', password='admin', ssl=True, keep_alive=1, persistent=True)

    server(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )


Naming convention
=================
* Nie robimy camelCase
* Używanie ``_`` w nazwach (snake_case) - // Python - snake ;)
* W Pythonie nie ma private/protected/public
* Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne
* Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe
* Nazwy opisowe funkcji zamiast komentarza
* ``print_()`` - when name collision
* ``__nazwa_funkcji()`` - name mangling


Variable scope
==============
* ``globals()``
* ``locals()``

.. code-block:: python

    def add(a, b):
        c = 3
        print(locals())

    add(1, 2)
    # {'a': 1, 'b': 2, 'c': 3}


Recurrence
==========
* Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekurencję.

.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


Assignments
===========

Number to string
----------------
#. Napisz funkcję ``number_to_str``
#. Funkcja zamieni dowolnego ``int`` lub ``float`` na formę tekstową

    .. code-block:: python

        number_to_str(1969)    # 'one nine six nine'
        number_to_str(31337)   # 'three one three three seven'
        number_to_str(13.37)   # 'one three and three seven'
        number_to_str(31.337)  # 'three one and three three seven'

:About:
    * Filename: ``functions_numstr_simple.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Number to human readable
------------------------
#. Napisz funkcję ``number_to_str``
#. Funkcja zamieni dowolnego ``int`` lub ``float`` na formę tekstową
#. Funkcja musi zmieniać wartości na poprawną gramatycznie formę
#. Max 6 cyfr przed przecinkiem
#. Max 5 cyfr po przecinku

    .. code-block:: python

        number_to_str(1969)   # 'one thousand nine hundred sixty nine'
        number_to_str(13.37)  # 'thirteen and thirty seven hundredths'
        number_to_str(31337)  # 'thirty one thousand three hundred thirty seven'
        number_to_str(31.337) # 'thirty one three hundreds thirty seven thousands'

:About:
    * Filename: ``functions_numstr_human.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Roman numbers
-------------
#. Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.
#. Napisz drugą funkcję, która dokona procesu odwrotnego.

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Sprawdzanie czy element istnieje w ``dict``
    * Rzutowanie i konwersja typów

:About:
    * Filename: ``functions_roman.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min
