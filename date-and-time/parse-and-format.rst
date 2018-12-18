**********************
Parsing and Formatting
**********************


Date and time formats
=====================
* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Date formats
------------
* Which format is a formal standard in USA?
* Which format is a formal standard in Germany?
* Which format is a formal standard in Poland?

.. code-block:: text

    4/12/61
    April 12, 1961

    12.4.1961
    12.04.1961

    12 IV 1961
    12.IV.1961

    12/4/1961
    12/04/1961

    12 kwietnia 1961
    12 kwiecień 1961

Time formats
------------
* Which time is a midnight?
* Which time is a noon?

.. code-block:: text

    12:00 am
    12:00 pm
    12:00
    23:59
    24:00
    0:00
    00:00

ISO 8601 Standard
-----------------
* Dates:

    .. code-block:: text

       1961-04-12

* Date and time

    .. code-block:: text

        1961-04-12T06:07:00

* Date and time with microseconds

    .. code-block:: text

        1961-04-12T06:07:00.123456


Table of date and time parsing and formatting parameters
========================================================
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

.. csv-table:: Tabelka parametrów formatowania i parsowania dat i czasu
    :header-rows: 1
    :file: data/datetime-formatting.csv


``f-string`` formatting
=======================
.. literalinclude:: src/datetime-format.py
    :language: python
    :caption: Datetime formatting as string with ``f'...'``


Format to string
================
.. literalinclude:: src/datetime-strftime.py
    :language: python
    :caption: Datetime formatting as string with ``.strftime()``


Parsing dates
=============
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. literalinclude:: src/datetime-parse.py
    :language: python
    :caption: Datetime parsing from string


Assignments
===========

From ISO date format
--------------------
* Filename: ``datetime_from_iso.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-time-from-iso`

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl pierwszą datę w formacie Amerykańkim "Miesiąc Dzień, Rok Godzina:Minuta AM/PM"
#. Wyświetl drugą datę w formacie Niemieckim "Dzień.Miesiąc.Rok"

.. code-block:: python
    :name: listing-time-from-iso
    :caption: Convert ``str`` from ISO date format to ``datetime`` objects

    gagarin = '1961-04-12T06:07:00.123456'
    armstrong = '1969-07-21T14:56:15.123456'

To ISO date format
------------------
* Filename: ``datetime_to_iso.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Input data:

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl ``date1`` w formacie ISO, tj. "Rok-Miesiąc-DzieńTGodzina:Minuta:Sekunda.UłamkiSekund"
#. Wyświetl ``date2`` w formacie ISO samą datę, tj. bez czasu

.. code-block:: python
    :name: listing-time-to-iso
    :caption: Convert ``str`` to ``datetime`` objects and print as ISO date format

    date1 = 'April 12, 1961 2:07 local time'
    date2 = '"07/21/69 2:56:15 AM UTC"'

:Hint:
    * Wpisz "local time" jako zwykły tekst do ``strptime``
    * Znaki znaki cudzysłowia jako znaczki do ``strptime``
