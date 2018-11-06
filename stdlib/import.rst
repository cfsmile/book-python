.. _Installing Packages:

*******************
Installing Packages
*******************


Virtualenv
==========
* What is Virtualenv
* Directories

.. code-block:: text

    venv/
    .venv/

    virtualenv/
    .virtualenv/

    .virtualenv-3.6/
    .virtualenv-3.7/

    venv-3.6/
    venv-3.7/

    .venv-3.6/
    .venv-3.7/

    ~/.virtualenv/.../


Searching
=========
- https://pypi.org
- ``pip search ...``


Installing
==========
- ``Alt+Enter`` on not existing ``import`` -> Install Package
- ``pip install ...``
- ``requirements.txt``
- ``pip install -r requirements.txt``


Using
=====
``import ...``


Importing
=========
.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.path.insert(0, '/path/to/directory')

.. code-block:: text

    game
        __init__.py
        config.py
        api.py
        dragon
            __init__.py
            wawelski.py
            red.py
            black.py
            white.py

.. code-block:: python

    from game.config import RESOLUTION_MAX_X

.. code-block:: python

    from game.dragon import red
    from game.dragon import white


    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

.. code-block:: python

    from game.dragon import *

    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

.. code-block:: python

    from game.dragon.red import RedDragon
    from game.dragon.white import WhiteDragon

    my_dragon1 = RedDragon()
    my_dragon2 = WhiteDragon()

.. code-block:: python

    from game.dragon.red import RedDragon as Smok

    wawelski = Smok()


Assignments
===========

Virtualenv
----------
#. Stwórz virtualenv z instalacją Python
#. Dodaj virtualenv do Python Interpreter w Twoim IDE

Installing from ``requirements.txt``
------------------------------------
#. Stwórz plik ``requirements.txt``
#. Dopisz linijkę ``pycodestyle`` do ``requirements.txt``
#. Niech Twoje IDE zainstaluje bibliotekę automatycznie (kliknięcie w żółty banner)

:About:
    * Filename: ``requirements.txt``
    * Lines of code to write: 1 line
    * Estimated time of completion: 5 min
