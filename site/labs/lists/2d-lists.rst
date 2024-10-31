********
2D Lists
********

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

* For all exercises

    * Do **not** make a ``vector.py`` file, just use Colab like you have been
    * Use ``assert`` to test instead of their ``test`` function


#. `Chapter 11 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/lists.html#exercises>`_

    * 7
    * 8


#. Write assertion tests for each of your functions above



Before Kattis
=============

.. note::

    Although the below example is a 3x3 matrix (list of lists), your functions should work on any sized matrix. For
    example, 4x4, 5x23, 230x19973.

    In other words, the following is not correct as it will only ever work for a 3x3 matrix.

        .. code-block:: python

            def print_row(mat, row):
                print(mat[row][0])
                print(mat[row][1])
                print(mat[row][2])


Given the following code:

    .. code-block:: python

        two_D = [['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i']]


#. Write a function ``print_row(matrix, row: int):``

    * ``matrix`` is a list of lists (2D list)
    * ``row`` is the specified row to print
    * The function will print out the values from the specified row
    * Each value can be on its own line
    * The function will not return anything
    * Verify correctness by running the function on multiple 2D lists

    .. image:: matRow.png


#. Write a function ``print_column(matrix, column: int):``

    * ``matrix`` is a list of lists (2D list)
    * ``column`` is the specified column to print
    * The function will print out the values from the specified column
    * Each value can be on its own line
    * The function will not return anything
    * Verify correctness by running the function on multiple 2D lists

    .. image:: matCol.png


#. Write a function ``print_down_right(matrix):``

    * ``matrix`` is a list of lists (2D list)
    * The function will print out the values of the matrix diagonal starting in the top left moving down to the right
    * Each value can be on its own line
    * The function will not return anything
    * Verify correctness by running the function on multiple 2D lists

    .. image:: matDiag3.png


#. Write a function ``print_up_right(matrix):``

    * ``matrix`` is a list of lists (2D list)
    * The function will print out the values of the matrix diagonal starting in the bottom left moving up to the right
    * Each value can be on its own line
    * The function will not return anything
    * Verify correctness by running the function on multiple 2D lists

    .. image:: matDiag4.png


#. Write a function ``print_down_left(matrix):``

    * ``matrix`` is a list of lists (2D list)
    * The function will print out the values of the matrix diagonal starting in the top right moving down to the left
    * Each value can be on its own line
    * The function will not return anything
    * Verify correctness by running the function on multiple 2D lists

    .. image:: matDiag5.png


#. Write a function ``print_up_left(matrix):``

    * ``matrix`` is a list of lists (2D list)
    * The function will print out the values of the matrix diagonal starting in the bottom right moving up to the left
    * Each value can be on its own line
    * The function will not return anything
    * Verify correctness by running the function on multiple 2D lists

    .. image:: matDiag6.png


#. To verify that your functions work on arbitrary sized 2D lists, what happens if you run your functions with the following matrix?

        * Ensure each function works as expected
        * If the functions are only printing out three values, there is something wrong

    .. code-block:: python

       four_x_four = [['a', 'b', 'c', 'w'],
                    ['d', 'e', 'f', 'x'],
                    ['g', 'h', 'i', 'y'],
                    ['j', 'k', 'l', 'z']]


Kattis Problems
===============

* You should be using a scrap piece of paper to work out the ideas for the following problems

    * The problems you are to solve are getting too complex to try to solve by just coding
    * Trying to solve problems by just typing away will not yield success


#. https://open.kattis.com/problems/bijele
#. https://open.kattis.com/problems/cold
#. https://open.kattis.com/problems/nastyhacks
#. https://open.kattis.com/problems/grassseed
#. https://open.kattis.com/problems/pet
#. https://open.kattis.com/problems/batterup
#. https://open.kattis.com/problems/aboveaverage
#. https://open.kattis.com/problems/icpcawards
#. https://open.kattis.com/problems/quickbrownfox
#. https://open.kattis.com/problems/nodup
#. https://open.kattis.com/problems/conundrum
#. https://open.kattis.com/problems/bela
#. https://open.kattis.com/problems/kornislav
