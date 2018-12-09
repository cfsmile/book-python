********************
Pandas ``DataFrame``
********************


* 2-dimensional object
* Each column ``Series`` and have name
* All columns has common indexes
* Operations can be executed on columns or rows


Creating
========

Simple ``pd.DataFrame``
-----------------------
.. code-block:: python

    values = np.arange(16).reshape(4, 4)
    indexes = range(4)
    columns = range(4)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #     0   1   2   3
    # 0   0   1   2   3
    # 1   4   5   6   7
    # 2   8   9  10  11
    # 3  12  13  14  15

With ``date`` indexes
---------------------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "1970-01-01", "0.131926", "-1.825204", "-1.909562", "1.274718"
    "1970-01-02", "0.084471", "-0.932586", "0.160637", "-0.275183"
    "1970-01-03", "-1.308835", "-0.285436", "-0.757591", "-0.042493"
    "1970-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "1970-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"
    "1970-01-06", "1.361922", "-0.827940", "0.400024", "0.047176"

With custom values in columns
-----------------------------
.. code-block:: python

    df = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('1961-04-12'),
                        'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D' : np.array([3] * 4, dtype='int32'),
                        'E' : pd.Categorical(["test", "train", "test", "train"]),
                        'F' : 'foo' })

.. csv-table:: DataFrame
    :header-rows: 1

    "", "A", "B", "C", "D", "E", "F"
    "0", "1.0", "1961-04-12", "1.0", "3", "test", "foo"
    "1", "1.0", "1961-04-12", "1.0", "3", "train", "foo"
    "2", "1.0", "1961-04-12", "1.0", "3", "test", "foo"
    "3", "1.0", "1961-04-12", "1.0", "3", "train", "foo"

With multiple rows
------------------
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'C': 3}])

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C"
    "0", "1.0", "2.0", "NaN"
    "1", "NaN", "NaN", "3.0"


Properties
==========
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

Indexes
-------
.. code-block:: python

    df.index
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03', '1970-01-04', '1970-01-05', '1970-01-06'],
    #               dtype='datetime64[ns]', freq='D')

Columns
-------
.. code-block:: python

    df.columns
    # Index(['A', 'B', 'C', 'D'], dtype='object')


Slicing
=======

Slicing by index
----------------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

.. code-block:: python

    df[1:3]
    #                    A         B         C         D
    # 1970-01-02  0.084471 -0.932586  0.160637 -0.275183
    # 1970-01-03 -1.308835 -0.285436 -0.757591 -0.042493


Slicing by columns
------------------
.. code-block:: python

    df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('1961-04-12'),
                         'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                         'D' : np.array([3] * 4, dtype='int32'),
                         'E' : pd.Categorical(["test", "train", "test", "train"]),
                         'F' : 'foo' })

.. code-block:: python

    df.E
    # 0     test
    # 1    train
    # 2     test
    # 3    train
    # Name: E, dtype: category
    # Categories (2, object): [test, train]

.. code-block:: python

    df['E']
    # 0     test
    # 1    train
    # 2     test
    # 3    train
    # Name: E, dtype: category
    # Categories (2, object): [test, train]

.. code-block:: python

    df[['A', 'B']]

.. csv-table::
    :header-rows: 1

    "", "A", "B"
    "0", "1.0", "1961-04-12"
    "1", "1.0", "1961-04-12"
    "2", "1.0", "1961-04-12"
    "3", "1.0", "1961-04-12"


Filtering
=========
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

.. code-block:: python

    df[df.B > 0.5]

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "1970-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "1970-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"


Locating values
===============
* Zalecane jest używanie zoptymalizowanych funkcji Pandas
* ``iloc`` integer locate (bez where i innych bajerów)

.. warning::
    * Start and the stop are included.
    * This is different behavior than Python slices!

.. code-block:: python

    values = [[1, 2], [4, 5], [7, 8]]
    indexes = ['cobra', 'viper', 'sidewinder']
    columns = ['max_speed', 'shield']

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #             max_speed  shield
    # cobra               1       2
    # viper               4       5
    # sidewinder          7       8

Single label
------------
* Note this returns the row as a Series

.. code-block:: python

    df.loc['viper']
    # max_speed    4
    # shield       5
    # Name: viper, dtype: int64

List of labels
--------------
* Note using ``[[]]`` returns a DataFrame

.. code-block:: python

    df.loc[['viper', 'sidewinder']]
    #             max_speed  shield
    # viper               4       5
    # sidewinder          7       8

Single label for row and column
-------------------------------
.. code-block:: python

    df.loc['cobra', 'shield']
    # 2

Slice with labels for row and single label for column
-----------------------------------------------------
* Note that both the start and stop of the slice are included

.. code-block:: python

    df.loc['cobra':'viper', 'max_speed']
    # cobra    1
    # viper    4
    # Name: max_speed, dtype: int64

Boolean list with the same length as the row axis
-------------------------------------------------
.. code-block:: python

    df.loc[[False, False, True]]
    #             max_speed  shield
    # sidewinder          7       8

Conditional that returns a boolean Series
-----------------------------------------
.. code-block:: python

    df.loc[df['shield'] > 6]
    #             max_speed  shield
    # sidewinder          7       8

Conditional that returns a boolean Series with column labels specified
----------------------------------------------------------------------
.. code-block:: python

    df.loc[df['shield'] > 6, ['max_speed']]
    #             max_speed
    # sidewinder          7

Callable that returns a boolean Series
--------------------------------------
.. code-block:: python

    df.loc[lambda df: df['shield'] == 8]
    #             max_speed  shield
    # sidewinder          7       8

Set value for all items matching the list of labels
---------------------------------------------------
.. code-block:: python

    df.loc[['viper', 'sidewinder'], ['shield']] = 50
    #             max_speed  shield
    # cobra               1       2
    # viper               4      50
    # sidewinder          7      50

Set value for an entire row
---------------------------
.. code-block:: python

    df.loc['cobra'] = 10
    #             max_speed  shield
    # cobra              10      10
    # viper               4      50
    # sidewinder          7      50

Set value for an entire column
------------------------------
.. code-block:: python

    df.loc[:, 'max_speed'] = 30
    #             max_speed  shield
    # cobra              30      10
    # viper              30      50
    # sidewinder         30      50

Set value for rows matching callable condition
----------------------------------------------
* Important!

.. code-block:: python

    df.loc[df['shield'] > 35] = 0
    #             max_speed  shield
    # cobra              30      10
    # viper               0       0
    # sidewinder          0       0

Slice with integer labels for rows
----------------------------------
* Note that both the start and stop of the slice are included

.. code-block:: python

    values = [[1, 2], [4, 5], [7, 8]]
    indexes = [1, 2, 3]
    columns = ['max_speed', 'shield']

    df = pd.DataFrame(values, index=indexes, columns=)
    #    max_speed  shield
    # 1          1       2
    # 2          4       5
    # 3          7       8

    df.loc[1:2]
    #    max_speed  shield
    # 2          1       2
    # 3          4       5


Accessing values
================
* Access a single value for a row/column pair by integer position
* Use iat if you only need to get or set a single value in a DataFrame or Series
* ``iat`` integer at (bez where i innych bajerów)

.. code-block:: python

    df = pd.DataFrame([[0, 2, 3],
                       [0, 4, 1],
                       [10, 20, 30]], columns=['A', 'B', 'C'])
    #     A   B   C
    # 0   0   2   3
    # 1   0   4   1
    # 2  10  20  30

Get value at specified row/column pair
--------------------------------------
.. code-block:: python

    df.iat[1, 2]
    # 1

Set value at specified row/column pair
--------------------------------------
.. code-block:: python

    df.iat[1, 2] = 10
    df.iat[1, 2]
    # 10

Get value within a series
-------------------------
.. code-block:: python

    df.loc[0].iat[1]
    # 2


Modifying values
================
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'C': 3}])

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C"
    "0", "1.0", "2.0", "NaN"
    "1", "NaN", "NaN", "3.0"

Adding column
-------------
.. code-block:: python

    df['Z'] = ['aa', 'bb']

=== === === === ==
    A   B   C   Z
=== === === === ==
0   1.0 2.0 NaN aa
1   NaN NaN 3.0 bb
=== === === === ==

Remove missing values
---------------------
* ``any`` : If any ``NA`` values are present, drop that row or column
* ``all`` : If all values are ``NA``, drop that row or column

.. code-block:: python

    df = pd.DataFrame([{'A': 1, 'B': 2}, {'B': 2, 'C': 3}])

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   NaN 2.0 3.0
=== === === ===

.. code-block:: python

    df.dropna(how='all')

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   NaN 2.0 3.0
=== === === ===

.. code-block:: python

    df.dropna(how='any')

=== === === ===
    A   B   C
=== === === ===

.. code-block:: python

    df.dropna(how='any', axis=1)

=== ===
    B
=== ===
0   2.0
1   2.0
=== ===

Fill ``NA``/``NaN`` values using the specified method
-----------------------------------------------------
* ``ffill``: propagate last valid observation forward to next valid backfill
* ``bfill``: use NEXT valid observation to fill gap

.. code-block:: python

    df.fillna(0.0)

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   NaN 2.0 3.0
=== === === ===

.. code-block:: python

    values = {'A': 5, 'B': 7, 'C': 9}
    df.fillna(values)

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 9.0
1   5.0 2.0 3.0
=== === === ===

.. code-block:: python

    df.fillna(method='ffill')

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   1.0 2.0 3.0
=== === === ===

.. code-block:: python

    df.fillna(method='bfill')

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 3.0
1   NaN 2.0 3.0
=== === === ===

Transpose
---------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

.. code-block:: python

    df.T
    df.transpose()

=== ========== =========== ========== ========== ========== ==========
    1970-01-01  1970-01-02 1970-01-03 1970-01-04 1970-01-05 1970-01-06
=== ========== =========== ========== ========== ========== ==========
A   0.131926    0.084471   -1.308835  -0.974425  0.589973   1.361922
B   -1.825204   932586     -0.285436  1.327082   0.748417   -0.827940
C   -1.909562   0.160637   -0.757591  -0.435516  -1.680741  0.400024
D   1.274718    -0.275183  -0.042493  1.328745   0.510512   0.047176
=== ========== =========== ========== ========== ========== ==========


Displaying values
=================
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

First ``n`` records
-------------------
.. code-block:: python

    df.head(2)
    #                    A         B         C         D
    # 1970-01-01  0.131926 -1.825204 -1.909562  1.274718
    # 1970-01-02  0.084471 -0.932586  0.160637 -0.275183

Last ``n`` records
------------------
.. code-block:: python

    df.tail(3)
    #                    A         B         C         D
    # 1970-01-04 -0.974425  1.327082 -0.435516  1.328745
    # 1970-01-05  0.589973  0.748417 -1.680741  0.510512
    # 1970-01-06  1.361922 -0.827940  0.400024  0.047176


Sorting
=======
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

Sort by index
-------------
.. code-block:: python

    df.sort_index(ascending=False) # default axis=0
    df.sort_index(ascending=False, inplace=True)

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "1970-01-06", "1.361922", "-0.827940", "0.400024", "0.047176"
    "1970-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"
    "1970-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "1970-01-03", "-1.308835", "-0.285436", "-0.757591", "-0.042493"
    "1970-01-02", "0.084471", "-0.932586", "0.160637", "-0.275183"
    "1970-01-01", "0.131926", "-1.825204", "-1.909562", "1.274718"

Sort by columns
---------------
.. code-block:: python

    df.sort_index(axis=1, ascending=False)

.. csv-table::
    :header-rows: 1

    "", "D", "C", "B", "A"
    "1970-01-01", "1.274718 ", "-1.909562", "-1.825204", "0.131926"
    "1970-01-02", "-0.275183", "0.160637", "-0.932586", "0.084471"
    "1970-01-03", "-0.042493", "-0.757591", "-0.285436", "-1.308835"
    "1970-01-04", "1.328745", "-0.435516", "1.327082", "-0.974425"
    "1970-01-05", "0.510512", "-1.680741", "0.748417", "0.589973"
    "1970-01-06", "0.047176", "0.400024", "-0.827940", "1.361922"

Sort by values
--------------
.. code-block:: python

    df.sort_values('B')
    df.sort_values('B', inplace=True)

    # można sortować po wielu kolumnach (jeżeli wartości w pierwszej będą równe)
    df.sort_values(['B', 'C'])
    df.sort_values(['B', 'C'])

=========== =========== =========== =========== =========
            A           B           C           D
=========== =========== =========== =========== =========
1970-01-01  0.131926    -1.825204   -1.909562   1.274718
1970-01-02  0.084471    -0.932586   0.160637    -0.275183
1970-01-06  1.361922    -0.827940   0.400024    0.047176
1970-01-03  -1.308835   -0.285436   -0.757591   -0.042493
1970-01-05  0.589973    0.748417    -1.680741   0.510512
1970-01-04  -0.974425   1.327082    -0.435516   1.328745
=========== =========== =========== =========== =========


Statistics
==========
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

Arithmetic mean
---------------
.. code-block:: python

    df.mean()
    # A   -0.078742
    # B    0.241929
    # C    0.110231
    # D   -0.092946
    # dtype: float64

Descriptive stats
-----------------
.. code-block:: python

    df.describe()
    #               A          B          C          D
    # count  6.000000   6.000000   6.000000   6.000000
    # mean  -0.078742   0.241929   0.110231  -0.092946
    # std    0.690269   0.845521   0.746167   1.207483
    # min   -0.928127  -0.931601  -0.812575  -1.789321
    # 25%   -0.442016  -0.275899  -0.359650  -0.638282
    # 50%   -0.202288   0.287667  -0.045933  -0.332729
    # 75%    0.189195   0.882916   0.733453   0.902115
    # max    1.062487   1.190259   1.036800   1.323504

Percentiles
-----------
.. code-block:: python

    values = np.array([[1, 1], [2, 10], [3, 100], [4, 100]])
    columns = ['a', 'b']

    df = pd.DataFrame(values, columns=columns)
    #    a    b
    # 0  1    1
    # 1  2   10
    # 2  3  100
    # 3  4  100

.. code-block:: python

    df.quantile(.1)
    # a    1.3
    # b    3.7
    # dtype: float64

.. code-block:: python

    df.quantile([.1, .5])
    #        a     b
    # 0.1  1.3   3.7
    # 0.5  2.5  55.0

Other methods
-------------
.. csv-table:: Descriptive statistics
    :header-rows: 1

    "Function", "Description"
    "``count``", "Number of non-null observations"
    "``sum``", "Sum of values"
    "``mean``", "Mean of values"
    "``mad``", "Mean absolute deviation"
    "``median``", "Arithmetic median of values"
    "``min``", "Minimum"
    "``max``", "Maximum"
    "``mode``", "Mode"
    "``abs``", "Absolute Value"
    "``prod``", "Product of values"
    "``std``", "Unbiased standard deviation"
    "``var``", "Unbiased variance"
    "``sem``", "Unbiased standard error of the mean"
    "``skew``", "Unbiased skewness (3rd moment)"
    "``kurt``", "Unbiased kurtosis (4th moment)"
    "``quantile``", "Sample quantile (value at %)"
    "``cumsum``", "Cumulative sum"
    "``cumprod``", "Cumulative product"
    "``cummax``", "Cumulative maximum"
    "``cummin``", "Cumulative minimum"


Grouping
========
* Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns.

.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

By count of elements
--------------------
.. code-block:: python

    df.groupby('D').size()
    #         D
    # -1.789321    1
    # -0.709686    1
    # -0.424071    1
    # -0.241387    1
    #  1.283282    1
    #  1.323504    1
    # dtype: int64

By mean of elements
-------------------
.. code-block:: python

    df.groupby('D').mean()
    #         D          A          B          C
    # -1.789321   0.257330   1.190259   0.074459
    # -0.709686  -0.459565   0.827296   0.953118
    # -0.424071   1.062487  -0.251961  -0.424092
    # -0.241387  -0.928127  -0.931601   1.036800
    # 1.283282   -0.015208   0.901456  -0.812575
    # 1.323504   -0.389369  -0.283878  -0.166324

Example
-------
.. code-block:: python

    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C' : np.random.randn(8),
                       'D' : np.random.randn(8)})

    #      A      B          C          D
    # 0  foo    one   0.239653  -1.505271
    # 1  bar    one   0.567327  -0.109503
    # 2  foo    two   1.726200  -0.401514
    # 3  bar  three  -1.145225   1.379611
    # 4  foo    two  -0.808037   1.148953
    # 5  bar    two   0.883013  -0.347327
    # 6  foo    one   0.225142  -0.995694
    # 7  foo  three  -0.484968  -0.547152

    df.groupby('A').mean()
    #   A         C          D
    # bar  0.101705   0.307594
    # foo  0.179598  -0.460136


Joins
=====
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df1 = pd.DataFrame(values, index=indexes, columns=columns)
    df2 = pd.DataFrame([ {'A': 1, 'B': 2},
                         {'C': 3}])

Left Join
---------
.. code-block:: python

    df1.join(df2, how='left', rsuffix='_2')  # gdyby była kolizja nazw kolumn, to dodaj suffix '_2'

.. code-block:: python

    df1.merge(df2, right_index=True, left_index=True, how='left', suffixes=('', '_2'))

Outer Join
----------
.. code-block:: python

    df1.merge(df2)
    df1.merge(df2, how='outer')

Append
------
* jak robi appenda, to nie zmienia indeksów (uwaga na indeksy powtórzone)
* nowy dataframe będzie miał kolejne indeksy

.. code-block:: python

    df1.append(df2)
    df1.append(df2, ignore_index=True)

Concat
------
* Przydatne przy łączeniu dataframe wczytanych z wielu plików
.. code-block:: python

    pd.concat([df1, df2])
    pd.concat([df1, df2], ignore_index=True)
    pd.concat([df1, df2], join='inner')


Practical Example
=================
.. code-block:: python

    import pandas as pd
    from reach.importer.models import Spreadsheet


    df = pd.read_excel(
        io='filename.xls',
        encoding='utf-8',
        parse_dates=['from', 'to'],  # list of columns to parse for dates
        sheet_name=['Sheet 1'],
        skip_blank_lines=True,
        skiprows=1,
    )

    # Rename Columns to match database columns
    df.rename(columns={
        'from': 'date_start',
        'to': 'date_end',
    }, inplace=True)

    # Drop all records where "Name" is empty (NaN)
    df.dropna(subset=['name'], how='all', inplace=True)

    # Add column ``blacklis`` with data
    df['blacklist'] = [True, False, True, False]

    # Change NaN to None
    df.fillna(None, inplace=True)

    # Choose columns
    columns = ['name', 'date_start', 'date_end', 'blacklist']

    return df[columns].to_dict('records')


Assignments
===========

Iris Dirty
----------
* https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-dirty.csv

#. Mając dane Irysów przekonwertuj je na ``DataFrame``
#. Pomiń pierwszą linię z metadanymi
#. Zmień nazwy kolumn na:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Podmień wartości w kolumnie species

    - 0 -> 'setosa',
    - 1 -> 'versicolor',
    - 2 -> 'virginica'

#. Ustaw wszystkiw wiersze w losowej kolejności i zresetuj index
#. Wyświetl pierwsze 5 i ostatnie 3 wiersze
#. Wykreśl podstawowe statystyki opisowe

:About:
    * Filename: ``pandas_iris_dirty.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

Iris Clean
----------
* https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-clean.csv

#. Mając dane Irysów przekonwertuj je na ``DataFrame``
#. Podaj jawnie ``encoding``
#. Pierwsza linijka stanowi metadane (nie wyświetlaj jej)
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Przefiltruj ``inplace`` kolumnę 'Petal length' i pozostaw wartości powyżej 2.0
#. Dodaj kolumnę ``datetime`` i wpisz do niej dzisiejszą datę (UTC)
#. Dodaj kolumnę ``big_enough`` i dla wartości 'Petal width' powyżej 1.0 ustawi ``True``, a dla mniejszych ``False``
#. Pozostaw tylko kolumny 'Sepal length', 'Sepal width' oraz 'Species'
#. Wykreśl podstawowe statystyki opisowe

:About:
    * Filename: ``pandas_iris_clean.py``
    * Lines of code to write: 25 lines
    * Estimated time of completion: 25 min

Cars
----
#. Stwórz ``DataFrame`` samochody z:

    - losową kolumną liczb całkowitych przebieg z przedziału [0, 200 000]
    - losową kolumną spalanie z przedziału [2, 20]

#. Dodaj kolumnę marka:

    - jeżeli samochód ma spalanie [0, 5] marka to VW
    - jeżeli samochód ma spalanie [6, 10] marka to Ford
    - jeżeli samochód ma spalanie 11 i więcej, marka to UAZ

#. Dodaj kolumnę pochodzenie:

    - jeżeli przebieg poniżej 100 km, pochodzenie nowy
    - jeżeli przebieg powyżej 100 km, pochodzenie uzywany
    - jeżeli przebieg powyżej 100 000 km, pochodzenie z niemiec

#. Przeanalizuj dane statystycznie

    - sprawdź liczność grup
    - wykonaj analizę statystyczną

#. Pogrupuj dane po marce i po pochodzenie

:About:
    * Filename: ``pandas_cars.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 45 min

EVA
---
#. Na podstawie podanych URL:

    * https://www.worldspaceflight.com/bios/eva/eva.php
    * https://www.worldspaceflight.com/bios/eva/eva2.php
    * https://www.worldspaceflight.com/bios/eva/eva3.php
    * https://www.worldspaceflight.com/bios/eva/eva4.php

#. Scrappuj stronę wykorzystując ``pandas.read_html()``
#. Połącz dane wykorzystując ``pd.concat``
#. Przygotuj plik ``CSV`` z danymi dotyczącymi spacerów kosmicznych

:About:
    * Filename: ``pandas_eva.py``
    * Lines of code to write: 25 lines
    * Estimated time of completion: 30 min
