.. _Syntax:

******
Syntax
******


Indentation instead of braces
=============================
* Python uses indentation instead of braces
* 4 spaces indentation, no tabs
* Code indented on the same level belongs to block:

    .. code-block:: python

        if True:
            print('First line of the true statement')
            print('Second line of the true statement')
            print('Third line of the true statement')
        else:
            print('This is false')


End of lines
============
* No semicolon (``;``) at the end of lines
* ``\r\n`` and ``\n`` are good:

    .. code-block:: python

        print('Hello!\nHow are you?')
        print('Hello!\r\nHow are you?')

Comments
========

Line comments
---------------
* Indent must be on the same level as block indent
* Hash (``#``), space and then comment:

    .. code-block:: python

        # José Jiménez says hello
        print('My name... José Jiménez')

Inline comments
---------------
* Source code, two spaces, hash (``#``), space and then comment:

    .. code-block:: python

        print('My name... José Jiménez')  # José Jiménez says hello

Multiline comments
------------------
* Both single and double are good
* Single quotes ``'''``
* Double quotes ``"""``
* Double quotes are more common:

    .. code-block:: python

        """
        We choose to go to the Moon!
        We choose to go to the Moon in this decade and do the other things,
        not because they are easy, but because they are hard;
        because that goal will serve to organize and measure the best of our energies and skills,
        because that challenge is one that we are willing to accept, one we are unwilling to postpone,
        and one we intend to win, and the others, too.
        """

Docstring
---------
* Docstring is a first multiline comment in:

    * File / Module
    * Class
    * Method / Function

* It is accessible in ``__doc__`` property of an object
* Used for generating ``help()`` documentation

    .. code-block:: python

        def apollo_dsky(noun, verb):
            """
            This is the Apollo Display Keyboard
            It takes noun and verb
            """
            print(f'Program selected. Noun: {noun}, verb: {verb}')

* Used for ``doctest``

    .. code-block:: python

        def add(a, b):
            """
            Sums two numbers.

            >>> add(1, 2)
            3
            """
            return a + b


Commented out code
------------------
* Never!
* Use Version Control System instead - e.g.: ``git blame``
* IDE has Local history (modifications) and you can compare file


Variables and constants
=======================

Variable declaration
--------------------
.. code-block:: python

    my_variable = 10
    my_variable = 'ehlo world'

Constant declaration
--------------------
.. code-block:: python

    MY_CONSTANT = 10
    MY_CONSTANT = 'ehlo world'

Variables vs. constants
-----------------------
* Python do not distinguish between variables and constants
* Constants uses uppercase letters for names
* Variables uses lowercase letters for names
* Python allows you to change "constants" but it's a bad practice

Types
-----
* Since Python 3.5
* Type hints throws SyntaxError in Python before 3.5
* Type hints or type annotations
* It is not required, and never will be (quote from Guido van Rossum, Python BDFL)
* To check types you have to use IDE or modules like ``mypy`` lub ``pyre-check``
* Types are used extensively in system libraries
* More and more documentations on the internet use types

.. code-block:: python

    name: str = 'José Jiménez'
    age: int = 30

Type inference
--------------
* Static Typing (Java, C++, Swift)

    .. code-block:: java

        String name = new String("José Jiménez")

* Dynamic Typing (Python, PHP, Ruby)

    .. code-block:: python

        name = str('José Jiménez')
        name = 'José Jiménez'

    .. code-block:: python

        name: str = str('José Jiménez')  # Type annotations

        # Type annotations (type hinting not forcing)
        # this will work, but IDE should warn
        name: str = 10


More advanced topics
====================
.. note:: The topic will be continued in chapter: :ref:`Software Engineering Conventions`
