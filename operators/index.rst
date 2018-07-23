.. _Operators:

*********
Operators
*********


General operators
=================
.. csv-table:: Universal operators
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-general.csv


Numerical types operators
=========================
.. csv-table:: Numerical types operators
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-numerical.csv


Bitwise operators
=================
- ``|`` - OR
- ``&`` - AND
- ``~`` - NOT
- ``^`` - XOR
- ``<<`` - Shift left
- ``>>`` - Shift right

.. code-block:: python

    0 ^ 0  # 0
    1 ^ 1  # 0
    1 ^ 0  # 1
    0 ^ 1  # 1
    8 ^ 5  # 13

.. code-block:: text

    1000  # 8 (binary)
    0101  # 3 (binary)
    ----  # APPLY XOR ('vertically')
    1101  # result = 13 (dec)


Operator precedence
====================
.. csv-table:: Operator precedence
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-precedence.csv


Assignments
===========

Even and odd numbers
--------------------
#. napisz program, który wczyta od użytkownika ciąg znaków
#. sprawdzi czy jest to liczba parzysta, czy nieparzysta

:Założenia:
    * Nazwa pliku: ``operators_even_odd.py``
    * Szacunkowa długość kodu: około 5 linii
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie
    * wykorzystanie operatorów matematycznych

:Podpowiedź:
    * Zero jest parzyste: https://en.wikipedia.org/wiki/Parity_of_zero
    * Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
    * Użyj dzielenia modulo ``%``
    * Zwróć uwagę, że operator ``%`` działa modulo tylko na ``int`` oraz na ``float``. Przy ``str`` ma zupełnie inne znaczenie.

Integers and floats
-------------------
#. Wczytaj liczbę od użytkownika (poda tylko ``int`` albo ``float``)
#. Wyświetl informację czy jest to liczba całkowita, czy niecałkowita.

:Założenia:
    * Nazwa pliku: ``operators_integers.py``
    * Szacunkowa długość kodu: około 7 linii
    * Maksymalny czas na zadanie: 10 min

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie

:Podpowiedź:
    * Liczba całkowita to taka, której część dziesiętna nie występuje lub jest równa zero.
    * Możesz to sprawdzić dzieląc liczbę z resztą przez *1* i sprawdzając resztę z dzielenia.
    * Zwróć uywagę, że ``input()`` zawsze zwraca ``str`` wiec trzeba rzutowac na ``int``, ale wtedy tracimy informację czy wczesniej mielismy ``float``
