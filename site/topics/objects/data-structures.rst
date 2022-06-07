*******************************
Objects III --- Data Structures
*******************************

More complexity
===============

* Let's make a slightly more complex object. 
* What if I want to make ``MyStudents`` object. 
* It will basically just be an object that holds a list of my EnthusiasticStudents
* It will also have the class name


But first... a convention
=========================

* Let's go look at out ``EnthusiasticStudent`` object and make one small change

    .. code-block:: python
        :linenos:
      
        class EnthusiasticStudent:
            '''
            Obv we'll include a nice comment at the top of the class to explain what it's for... right?!

            This EnthusiasticStudent is being used to demonstrate how we can create our own Objects.
		  
            It's going to have a few attributes and some simple functions.
            '''

            def __init__(self, first_name='John', last_name='Doe', student_num='000000000', current_avg=0):
                self._first_name = first_name 
                self._last_name = last_name
                self._student_num = student_num
                self._current_avg = current_avg

            def ask_for_higher_mark(self, howHigh):
                print('Hello Professor,\n\nMy name is ' + self._first_name + ' and I am in your CSCI 161 class. I feel that I deserve a higher mark on the last assignment because I am the chosen one. I would really like it if you could just give me a ' + str(howHigh) + '%. \n\nThanks,\n' + self._first_name + ' ' + self._last_name)

            def show_off(self):
                print('I\'m going to ask a question about something really really really really advanced in an attempt to impress everyone and assume I\'m a wizard')
                self._first_name = 'Wizard'


            def work_too_hard_on_assignment(self):
                # I left it blank. Add whatever code you want here. Be sure to delete the pass keyword when you do though
                pass	
				
				
            def __repr__(self):
                '''
                A method which will return some string representation of the object. This will he handy for debugging and stuff.
                '''
                return 'First Name: ' + self._first_name + '\nlast_name: ' + self._last_name + '\nStudent Number: ' + self._student_num + '\nCurrent Average: ' + str(self._current_avg)


            def __eq__(self, anotherThing):
                '''
                A method to check if 2 EnthusiasticStudent are the same. What does it mean for 2 things to be the same?
                Well, WE get to make that up!
                (Although, we should pick something that makes sense...)
                '''
                return self._student_num == anotherThing.get_student_num()

            # just a getter (see below)
            def get_first_name(self):
                return self._first_name
				
            # just another getter (see below)
            def get_student_num(self):
                return self._student_num

* I added *underscores* to each of the attributes
* This makes them *private*
    * kinda...
	
Public/Private
==============

* Long story short...
* **Public** attributes/methods are visible outside the class
* **Private** attribute/methods are **NOT** visible outside the class

* When we make something private, it's like saying...
    * This attribute/method cannot be called anywhere else other than from within the code in the class. 
	* *James will now show you an example*

* Why do we care?
* It's all about encapsulation and design
* A well designed program will probably have public and private attribute/methods

* In Python, the convention for our private variables is to put an underscore in front. 

* The idea is, if I'm using the object someone else wrote, I don't need to know about what I don't need to know about...
* Let me put it this way.
    * You have all used lists
	* We know how to use them
	* We don't know how they work
	* We don't know what attributes they have
	* But that's OK
	
* Or how about this?
    * Imagine a car
    * Do you know how to drive a car?
        * gas, break, steer
    * Does the way you *interface* with the car matter if, say, the car is electric or gas?
    * A gas and electric car are built very different on the inside, but that didn't really impact the way you interface with the object.
   
* Don't worry too much if the point is still a little lost on you, it will get cleared in CSCI 162.

Getters/Setters
===============

* So how do we interface with the attributes if we make them all private?
* Getters and setters!

* It's so simple it's silly really
* Here is an example with getting/setting ``_student_num``

    .. code-block:: python
        :linenos:
      
        def get_student_num(self):
            return self._student_num
		
        def set_student_num(self, student_num):
            self._student_num = student_num
        
* Does it feel silly doing this?
* Yes, good, you're normal
* But again, motivation for this will reallllly come next semester. 
    * Teaser: We can control how the attributes are interacted with. 
    * We can enforce data integrity rules
        * Eg. Ensure all Student Numbers are 9 chars long. 

.. admonition:: Activity
    :class: activity

    * Try this example and see what happens when you change a private attribute without control on the modification.

    .. code-block:: python
            :linenos:

            a_student = EnthusiasticStudent("Bob", "Ross", "007")

            # A user manually changes the private attibute
            a_student._student_num = 5

            print(a_student)

    * What is the problem?
    * How can ``set_student_num()`` help us?


MyStudents
==========

* Ok, we want an object to hold onto ``EnthusiasticStudent`` objects
* What attributes do we want?
    * Name
    * List of the EnthusiasticStudents
	


    .. code-block:: python
        :linenos:
      
        class MyStudents:
            

            def __init__(self, name='DEFAULT_NAME'):
                self._class_name = name
                self._list_of_students = []
				
			
* That was easy
* Notice that we did **not** give the constructor a parameter for the ``self._list_of_students`` attribute. We don't need to!

* Let's write a method to add a student to the class

    .. code-block:: python
        :linenos:
		
        def add_student(self, fN, lN, sN, avg):
            a_student = EnthusiasticStudent(fN, lN, sN, avg)
            self._list_of_students.append(a_student)

* Let's write a method to search the list of EnthusiasticStudents for a student with a specific first name. Return ``True`` if it's in the list, ``False`` otherwise. 

    .. code-block:: python
        :linenos:
		
        def find_student(self, fName):
            for student in self._list_of_students:
                if fName == student.get_first_name():    # this assumes we wrote a getter/setter
                    return True
            return False
			
* __repr__
    * How should we convert the ``MyStudents`` object into a string?
			
    .. code-block:: python
        :linenos:	
    
            def __repr__(self):
                s = self._class_name + '\n'
                for student in self._list_of_students:
                    # Below we just convert the student to a string.
                    # the str(student) will automatically call the 
                    # the student's __repr__ method.
                    s += str(student) + '\n\n'    # Will work because we have a __repr__ for EnthusiasticStudent written

                return s	
	


Putting it Together
===================
	
    .. code-block:: python
        :linenos:	
		
        # Only need these if using multiple files
        #from EnthusiasticStudent import *
        #from MyStudents import *

        some_class = MyStudents('CSCI 161')
        some_class.add_student('Greg', 'Allen', '54321', 98)
        some_class.add_student('Bob','Smith', '12345', 50)
        print(some_class.find_student('Bob'))

        print(some_class)
		
		
For next class (is anyone actually reading these? You really should!)
=====================================================================

* Read `chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
