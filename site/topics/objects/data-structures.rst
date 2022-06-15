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

* But as a convention, to let yourself and other programmers know, all attributes and methods that are *not* to be accessed directly start with an underscore


.. code-block:: python
    :linenos:

    class Course:

        # init and/or other methods not shown for brevity

        def size(self) -> int:
            return len(self._students)

        def add(self, student: Student):
            self._students.append(student)


* For ``size``, we just hijack the ``len`` of the ``_students`` list and return that value
* Similarly for ``add``, we can make use of the list's ``append`` method

* The methods to ``remove`` a ``Student`` and check if the ``Course`` ``contains`` a specific ``Student`` both need a linear search

    * Find the ``Student`` to be removed, if it exists
    * Check if the ``Student`` is actually in the ``Course``

* To eliminate any duplicate code, we can write a helper method --- ``_find``

    * Like the attribute ``_students``, the method ``_find`` is not really indented to be used outside the class, thus, by convention, it starts with an underscore

* ``_find`` will me a method that performs the linear search on the list

    * If the specified ``Student`` is found within the ``_students`` list, return the index of where it is
    * If the ``Student`` is *not* found, return a sentinel value --- ``-1``
    * The ``-1`` sentinel value is a special value with meaning within the context of the algorithm --- *not found*

.. code-block:: python
    :linenos:
    :emphasize-lines: 16

    class Course:

        # init and/or other methods not shown for brevity

        def _find(self, student: Student) -> int:
            """
            Returns the index of the first occurrence of a given Student if it exists. If it does not exist, return a
            sentinel value of -1.

            :param student: The student to search for
            :type student: Student
            :return: Index of the student, or -1 if it is not found
            :rtype: int
            """
            for i, s in enumerate(self._students):
                if s == student:
                    return i
            return -1


* In the above ``_find`` method, we actually make use of the ``Student`` class' ``__eq__`` method

    * ``s == student`` calls the ``__eq__`` magic method from the ``Student`` class

* Overall, the ``_find`` method is not particularly remarkable --- it's a linear search
* With ``_find`` written, the ``remove`` and ``contains`` methods are simple to write

.. code-block:: python
    :linenos:

    class Course:

        # init and/or other methods not shown for brevity

        def contains(self, student: Student) -> bool:
            return -1 != self._find(student)

        def remove(self, student: Student):
            if not self.contains(student):
                raise ValueError("No such student to remove")
            else:
                self._students.pop(self._find(student))


* ``contains`` just calls ``_find`` and checks if the sentinel value was returned
* ``remove`` checks if the ``Student`` exists, and if it does, it removes it

    * Note that if the ``Student`` is not found, an exception is raised by the method

* The last method we will add to the ``Course`` class is the ``__repr__`` magic method
* Since we wrote the ``__repr__`` method for the ``Student`` class, we know how to format the string for an individual ``Student`` object
* However, the ``Course`` class is a collection of ``Student`` objects

.. code-block:: python
    :linenos:

    class Course:

        # init and/or other methods not shown for brevity

        def __repr__(self) -> str:
            s = ""
            for student in self._students:
                s += str(student) + "\n"
            return s


* In the above example, we start with an empty string ``s``
* Then, we loop over all ``Student`` objects within the ``_students`` list, and for each ``Student``

    * Convert them to a string ``str``, which automatically calls the ``Student`` ``__repr__`` magic method on the individual instance
    * Appends a newline to the end of the string
    * And then appends the whole new string to tne end of the string ``s``

* What's interesting here is how the ``Course`` class' ``__repr__`` makes use of the ``Student`` class' ``__repr__``
* Below is an example of a ``Course`` object and it's string representation

.. code-block:: python
    :linenos:

    my_course = Course("CS101")
    my_course.add(Student("Bob", "Smith", 123456789))
    my_course.add(Student("Jane", "Doe", 987654321))
    my_course.add(Student("Niles", "MacDonald", 192837465))
    my_course.add(Student("Jane", "Doe", 987654321))
    print(my_course)

    # Results in
    # Smith, Bob    123456789
    # Doe, Jane 987654321
    # MacDonald, Niles  192837465
    # Doe, Jane 987654321

* The string printed out is one single string that spans multiple lines


For Next Class
==============

* `Check out the tests for the Student class <https://github.com/jameshughes89/cs101/blob/main/test/test_student.py>`_
* `Check out the tests for the Course class <https://github.com/jameshughes89/cs101/blob/main/test/test_course.py>`_