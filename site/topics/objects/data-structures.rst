******************************
Objects IV --- Data Structures
******************************

* We have spent much of the course learning how to write algorithms
* But we also saw a few data structures

    * Lists
    * Tuples
    * Sets
    * Dictionaries

* Although these data structures had clear functionality associated with them, we use them as a mechanism for storing and managing data
* They may also provide some other benefits

    * Ability to index
    * Efficient lookups
    * Easy to search
    * Ordering the data
    * Managing duplicates
    * ...

* Consider the ``List``\s we have been using

    * They can be indexed
    * The lists have a beginning and end
    * The elements exist in some order (though, not necessarily *ordered*)
    * They are easy to do a linear search on

* You have all been taking advantage of these features, but the lists are provided to us at a certain level of abstraction
* If you dig deeper and look under the hood, all the functionality of the list needs to be programmed

* Data structures are an important part of a programmers toolbox
* Actually understanding *how* they do what they do is critical
* To start learning about data structures, we will be constructing our own simple collection --- a ``Course`` that will manage ``Student`` objects


Student Class
=============

* The ``Student`` objects are the objects we care about
* But the problem is, we will have many of them and we want a nice way to manage all instances

    * This is where the ``Course`` class comes in, which is covered in the next section

* For now, we will focus on the ``Student`` class --- a simple class to keep track of important student information
* We will also define an ``__eq__`` and ``__repr__`` for the class as they are often handy for testing purposes

.. code-block:: python
    :linenos:

class Student:

    def __init__(self, first_name: str, last_name: str, student_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number

    def __eq__(self, other) -> bool:
        """
        Two students are considered equal if their student numbers are the same. This assumes student numbers are unique
        among students.

        :param other: A student to compare the self Student to
        :type other: Student
        :return: True if the students have the same student number, false otherwise
        :rtype: boolean
        """
        if isinstance(other, Student):
            return self.student_number == other.student_number
        return False

    def __repr__(self) -> str:
        return f"{self.last_name}, {self.first_name}\t{self.student_number}"






Course Class
============


For next class (is anyone actually reading these? You really should!)
=====================================================================

* Read `chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
