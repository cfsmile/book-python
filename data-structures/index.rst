.. _Data Structures:

***************
Data Structures
***************


Simple collections
==================

``tuple``
---------
* Immutable - cannot add, modify or remove elements
* Defining with ``tuple()`` is more readable, but ``()`` is used more often:

    .. code-block:: python

        my_tuple = ()
        my_tuple = tuple()

* Single element ``tuple`` require comma at the end (**important!**)
* Braces are optional:

    .. code-block:: python

        my_tuple = 1,
        my_tuple = (1,)

* Can store any type:

    .. code-block:: python

        my_tuple = 1, 2.0, None, False, 'José'
        my_tuple = (1, 2.0, None, False, 'José')
        my_tuple = tuple(1, 2.0, None, False, 'José')

* Slicing tuple:

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)

        my_tuple[2]             # 3
        my_tuple[-1]            # 5
        my_tuple[:3]            # (1, 2, 3)
        my_tuple[3:]            # (4, 5)
        my_tuple[::2]           # (1, 3, 5)
        my_tuple[1:4]           # (2, 3, 4)

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)

        MIN = 1
        MAX = 4
        my_tuple[MIN:MAX]       # (2, 3, 4)

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)

        BETWEEN = slice(1, 4)
        my_tuple[BETWEEN]       # (2, 3, 4)

* Length of a ``tuple``:

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)
        len(my_tuple)           # 5

``list``
--------
* Mutable - can add, remove, and modify values
* Defining with ``list()`` is more readable, but ``[]`` is used more often

.. code-block:: python

    my_list = []
    my_list = list()

* Brackets are required
* No need for comma for one element ``list``:

    .. code-block:: python

        my_list = [1]
        my_list = list(1)

* Can store any type:

    .. code-block:: python

        my_list = [1, 2.0, None, False, 'José']
        my_list = list(1, 2.0, None, False, 'José')

    .. code-block:: python

        my_list = [1, 2.0, None, False, 'José']

        my_list[1]             # 2.0
        my_list[2:4]           # [None, False]
        my_list[::2]           # [1, None, 'José']
        my_list[-1]            # 'José'

* Can be appended or extended:

    .. code-block:: python

        my_list = [1, 2]

        my_list + [3, 4]        # [1, 2, 3, 4]
        my_list.append(5)       # [1, 2, 3, 4, 5]
        my_list.append([6, 7])  # [1, 2, 3, 4, 5, [6, 7]]
        my_list.extend([8, 9])  # [1, 2, 3, 4, 5, [6, 7], 8, 9]
        my_list.insert(0, 'a')  # ['a', 1, 2, 3, 4, 5, [6, 7], 8, 9]

* Length of a ``list``:

    .. code-block:: python

        my_list = [1, 2, 3]
        len(my_list)            # 3

``set``
-------
* Defining only with ``set()``

    .. code-block:: python

        my_set = set()

* No need for comma for one element ``set``

    .. code-block:: python

        my_set = {1}
        my_set = set(1)

* Only unique values:

    .. code-block:: python

        my_set = {1, 3, 1}       # {1, 3}
        my_set = set([1, 3, 1])  # {1, 3}

* Mutable - can add, remove, and modify values:

    .. code-block:: python

        my_set = {1, 2, 3}       # {1, 2, 3}

        my_set.add(4)            # {1, 2, 3, 4}
        my_set.add(4)            # {1, 2, 3, 4}
        my_set.add(3)            # {1, 2, 3, 4}

        my_set.update([4, 5])    # {1, 2, 3, 4, 5}
        my_set.update({4, 5})    # {1, 2, 3, 4, 5}

* Use of ``set`` operations with special syntax:

    .. code-block:: python

        {1,2} - {2,3}            # {1}        # Subtract
        {1,2} | {2,3}            # {1, 2, 3}  # Sum
        {1,2} & {2,3}            # {2}        # Union
        {1,2} ^ {2,3}            # {1, 3}     # Symmetrical difference
        {1,2} + {3,4}            # TypeError: unsupported operand type(s) for +: 'set' and 'set'

* Slicing ``set``:

    .. code-block:: python

        my_set = {1, 2.0, None, False, 'José'}

        my_set[1]                # 2
        my_set[2:4]              # {None, False}
        my_set[::2]              # {1, None, 'José'}
        my_set[-1]               # 'José'

* Length of a ``set``:

    .. code-block:: python

        my_set = {1, 2, 3}
        len(my_set)              # 3

* Converting ``list`` to ``set`` deduplicate items

    .. code-block:: python

        names = ['Max', 'Иван', 'José', 'Max']

        unique_names = set(names)
        # {'Max', 'Иван', 'José'}

``dict``
--------
* ``dict()`` items order changes!
* Declaring with ``dict()`` is more readable, but ``{}`` is used more often:

    .. code-block:: python

        my_dict = {}
        my_dict = dict()

* Key - Value storage:

    .. code-block:: python

        my_dict = {
            'first_name': 'José',
            'last_name': 'Jiménez'
        }

* Duplicating items are overridden by latter:

    .. code-block:: python

        my_dict = {
            'name': 'José',
            'name': 'Иван',
        }
        # {'name': 'Иван'}

* Key can be any hashable object:

    .. code-block:: python

        my_dict = {
            1961: 'First Human Space Flight',
            1969: 'First Step on the Moon',
        }

* Value can be any object:

    .. code-block:: python

        my_dict = {
            'astronaut': {'first_name': 'José', 'last_name': 'Jiménez'},
            'agency': ['NASA', 'Roscosmos', 'ESA'],
            'age': 42,
        }

Accessing ``dict`` values
-------------------------
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
* ``.get(...)`` returns ``None`` if key not found
* ``.get(...)`` can have default value, if key not found

.. code-block:: python

    data = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
        1961: 'First Human Space Flight',
        1969: 'First Step on the Moon',
    }

    data['last_name']          # 'Jiménez'
    data.get('last_name')      # 'Jiménez'

    data[1961]                 # 'First Human Space Flight'
    data.get(1961)             # 'First Human Space Flight'

    data['agency']             # KeyError: 'agency'
    data.get('agency')         # None
    data.get('agency', 'n/a')  # 'n/a'

Accessing ``dict`` values in bulk
---------------------------------
.. code-block:: python

    my_dict = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    my_dict.keys()    # ['first_name', 'last_name', 'age']
    my_dict.values()  # ['José', 'Jiménez', 42]
    my_dict.items()   # [('first_name', 'José'), ('last_name', 'Jiménez'), ('age', 42)]

``dict`` vs. ``set``
--------------------
* ``set()`` and ``dict()`` both use ``{`` and ``}`` braces:

    .. code-block:: python

        {}                                # dict
        {1}                               # set
        {1, 2}                            # set
        {1: 2}                            # dict
        {1:1, 2:2}                        # dict

* Despite similar syntax, they are different types:

    .. code-block:: python

        my_data = {}
        isinstance(my_data, (set, dict))  # True
        isinstance(my_data, dict)         # True
        isinstance(my_data, set)          # False

        my_data = {1}
        isinstance(my_data, dict)         # False
        isinstance(my_data, set)          # True

        my_data = {1: 1}
        isinstance(my_data, dict)         # True
        isinstance(my_data, set)          # False


Nested collections
==================

``list`` of ``dict``
--------------------
.. code-block:: python

    DATA = [
        {'first_name': 'Max'},
        {'first_name': 'José', 'last_name': 'Jiménez'},
        {'first_name': 'Иван', 'tags': ['astronaut', 'roscosmos', 'space']},
    ]

    DATA[0]                            # {'first_name': 'Max'}
    DATA[0]['last_name']               # KeyError: 'last_name'
    DATA[0].get('tags', 'n/a')         # 'n/a'
    DATA[2].get('tags')                # ['astronaut', 'roscosmos', 'space']
    DATA[2].get('tags')[1]             # 'roscosmos'

Multidimensional lists
----------------------
* Readability counts:

    .. code-block:: python

        array = [[1,2,3],[4,5,6],[7,8,9]]
        array = [[1,2,3], [4,5,6], [7,8,9]]
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        array = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

* Getting element from nested lists:

    .. code-block:: python

        array = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        array[2][1]  # 8

Mixed types
-----------
.. code-block:: python

    array = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
        {'first_name': 'José', 'last_name': 'Jiménez', 'age': 42}
    ]

    array[3]['last_name']  # 'Jiménez'


How Python understands types?
=============================
* Result of a ``type(what)`` for each line:

    .. code-block:: python

        what = 1, 2      # <class 'tuple'>
        what = (1, 2)    # <class 'tuple'>

    .. code-block:: python

        what = 'foo'     # <class 'str'>
        what = ('foo')   # <class 'str'>

        what = 'foo',    # <class 'tuple'>
        what = ('foo',)  # <class 'tuple'>

    .. code-block:: python

        what = 1.       # <class 'float'>
        what = (1.)     # <class 'float'>

        what = .5       # <class 'float'>
        what = (.5)     # <class 'float'>

        what = 1.0      # <class 'float'>
        what = 1        # <class 'int'>

    .. code-block:: python

        what = 10.5     # <class 'float'>
        what = (10.5)   # <class 'float'>

        what = 10,5     # <class 'tuple'>
        what = (10,5)   # <class 'tuple'>

        what = 10.      # <class 'float'>
        what = (10.)    # <class 'float'>

        what = 10,      # <class 'tuple'>
        what = (10,)    # <class 'tuple'>

        what = 10       # <class 'int'>
        what = (10)     # <class 'int'>


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Split train/test
----------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-data-structures-iris-sample`
#. Wyodrębnij nagłówek (pierwsza linia) od danych
#. Ustaw dane z kolejnych linii w losowej kolejności
#. Podziel zbiór na dwie listy w proporcji:

    - dane do uczenia - 80%
    - dane testowe - 20%

:Algorithm:
    #. zapisz nagłówek do zmiennej
    #. zapisz do innej zmiennej dane bez nagłówka
    #. na danych bez nagłówka zastosuj funkcję ``shuffle()``
    #. wylicz punkt przegięcia: długość danych bez nagłówka razy procent
    #. z danych bez nagłówka zapisz do uczenia rekordy od początku do punktu przegięcia
    #. z danych bez nagłówka zapisz do testów rekordy od punktu przegięcia do końca

:About:
    * Filename: ``structures_split_train_test.py``
    * Lines of code to write: 6 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Umiejętność przetwarzania złożonych typów danych
    * Korzystanie z przecięć danych
    * Wykorzystanie funkcji z biblioteki standardowej
    * Konwersja typów
    * Magic Number

:Hints:
    * ``from random import shuffle``
    * ``shuffle()`` modyfikuje dane "in place" i zwraca ``None``

.. literalinclude:: src/data-structures-iris-sample.py
    :name: listing-data-structures-iris-sample
    :language: python
    :caption: Sample Iris databases

