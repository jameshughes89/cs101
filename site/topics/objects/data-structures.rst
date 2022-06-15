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


* Above is the entire ``Student`` class
* The only functionality is defined in the magic methods
* The main purpose of the ``Student`` class is to store data

* Notice the ``__eq__`` defines equality for the ``Student`` class strictly on the ``student_number`` attribute

    * The ``first_name`` and ``last_name`` values may change for a ``Student``
    * However, the ``student_number`` of each ``Student`` should be unique and not change

* Also notice how the ``__repr__`` is not following the ``ClassName(attributes)`` format
* For the purpose of this program, a more specialized format is more appropriate


Course Class
============

* The ``Course`` class will be a collection of ``Student`` objects
* Ultimately, the ``Student`` objects will be stored in a ``List``, but we want to make use of a class to add specific functionality we care about

* We will have the ``Course`` class control access to the list of ``Students`` through methods

    * A method to add a ``Student`` to the list
    * A method to remove a ``Student`` from the list
    * A method to get the size of the course --- the number of ``Student`` objects in the list
    * A method to check if a given ``Student`` exists in the ``Course``
    * ``__repr__`` method


.. code-block:: python
    :linenos:

    class Course:
        """
        A collection of students enrolled in a course. This class manages the individual Students and provides simple
        enrollment details.
        """

        def __init__(self, course_name: str):
            self.course_name = course_name
            self._students = []


* Above is the constructor for the class
* The only two attrivutes the class has are ``course_name`` and ``_students``
* Notice how the ``Students`` attribute starts with an underscore ``_``
* We don't really want to access the list of ``Student`` objects directly
* Instead, to give us more control over how the list is used, we want to add and remove ``Students`` through the methods we write in the class
* Nothing will actually stop us from accessing the list directly

    * ``some_course._students``

* But as a convention, to let yourself and other programmers know, all attributes that are *not* to be accessed directly start with an underscore



For Next Class
==============

* Read `Chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
