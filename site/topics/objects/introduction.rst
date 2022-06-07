**************************
Objects I --- Introduction
**************************


* Objects are a way to combine data and functionality together within our programs
* Motivation for this is, it may help with abstraction and encapsulation
* Further, you may find it a little more natural and analogous to how you think of the world

* Consider the ``List``\s you have been using --- these are objects

    * They have some data associated with them,

        * Their size
        * the information stored in the list

    * But they also have functionality associated with them too

        * ``append``
        * ``remove``


* You are already used to working with some objects (e.g., ``List``)
* But you have not defined your own objects
* In this topic, the basics of how to define your own objects will be covered

	  
Classes vs Objects
==================

* We are going to make ``Circle`` objects
* However, in order to start making our own objects, we first must define a *class*
* A class is simply the code that defines what it means for something to be an object of the class
* For example, we will define a ``Circle`` class, which contains all the information needed for Python to start making instances of ``Circle``\s

    * You can think of the class as the blueprints for making objects

* Going back to ``List``\s

    * There exists a class definition (blueprints) for ``List``\s
    * With the one class, I can then create as many instances of ``List``\s as I want


Circle Class
============

* Just like the rest of the class, we will lean by doing
* In other words, we will define the ``Circle`` class and then make a few instances of ``Circle`` objects

* However, there is one big question --- what is a circle; what data and functionality should it have?

    * Turns out, we get to invent this
    * We decide what data will be stored
    * We decide what functionality it will have

* For our needs, we will have a ``Circle``:

    * Know its radius --- this is an *attribute*, the data
    * Be able to perform basic geometry calculations --- these are *methods*, the functionality


Starting the Class
------------------

* To start writing our ``Circle`` class, we use the ``class`` keyword

.. code-block:: python
    :linenos:

    class Circle:
        """
        A class for representing circle based on its radius. The class provides functionality to perform basic geometry
        calculations (diameter, area, circumference).
        """

* The above example contains the start of the class
* The ``class Circle:`` starts the class

    * Anything indented is part of the ``Circle`` class definition
    * Like how anything indented under an ``if`` is part of the ``if`` block

* The docstring comment is a simple description of the class


Let's Make a Simple Object/ADT
==============================

* All objects/ADTs, regardless of how simple or complex they are, are all build with the same basic things. 

* But we're going to start really simple.

* I want to make an ``EnthusiasticStudent`` **object**
    * What I mean is, someone had to write what a numpy array was... we're going to write what it means to be an ``EnthusiasticStudent``

* To create our own object, all we really need are 3 things:
    * A *constructor*
    * *Attributes/properties*
    * *Methods* (and the constructor is actually a method too)
   
* **Attributes** --- Properties about the object.

* **Methods** --- Things we want our object to do.

* To determine which attributes/properties we want our object to have... well, **we** have to think about it... what do **we** want the object to have?
    * First name
    * Last name
    * Student number
    * Currently average
    * ... (whatever else we want really)
   
* **We** get to make it up!
   
* Same goes for methods. What *methods* do **we** want this object to have?
    * Ask for a higher mark
    * Show off in class how smart they are
    * Work painfully hard on assignments
    * ... (again... whatever else we want   

* Cool.. but how do we tell python all this?   

.. Warning::
    Follow along (for real, having a copy of this on your comp will make your life easier)!!!

1. Write this at the top of some cell in Colab ``class EnthusiasticStudent:``. 

    .. Warning::
        If using PyCharm or Spyder, you can put everything in the same script, or alternatively, you could do the *better* thing and put all classes in their own files. I'd recommend this. 

    * This tells python *Hey, everything that follows is gonna be about the EnthusiasticStudent*
    * Classes do **not** need to be in their own files, but it's often a good call

    .. code-block:: python
        :linenos:
      
        class EnthusiasticStudent:
            '''
            Obv we'll include a nice comment at the top of the class to explain what it's for... right?!

            This EnthusiasticStudent is being used to demonstrate how we can create our own Objects.
		  
            It's going to have a few attributes and some simple functions.
            '''

            # this is it so far :/ 

2. Let's write a constructor

    * It's a special method that tells the computer to *make*, or *initialize* the object.
    * Classes don't have to have constructors, but to use objects the way we want to here we need one
    * It will tell the computer to go create the object somewhere in memory along with running some setup code for us
        * What setup code? Good questions. The answer is... whatever you need!

    .. code-block:: python
        :linenos:
      
        class EnthusiasticStudent:
            '''
            Obv we'll include a nice comment at the top of the class to explain what it's for... right?!

            This EnthusiasticStudent is being used to demonstrate how we can create our own Objects.
		  
            It's going to have a few attributes and some simple functions.
            '''

            def __init__(self):
                '''
                So the above line of code is the special words for python that means CONSTRUCTOR
                Notice that it has parentheses, and a parameter called *self*
                Self is a special variable thing that is a reference to... itself... 
                '''

    * ``def __init__(self, x1, x2, x3, x4, x5,..., xn):`` is how we start our constructor
    * Notice how it can take any number of parameters we want
        * Just like a function/method... because it *is* a method
	  
    * It actually has to take at least one parameter; it has to get a parameter that'll be a reference to itself
        * It doesn't *need* to be called ``self``, however if you don't call if ``self`` the world will hate you
	  
    * ...
    * Wait... 
    * ``self`` is a reference to... itself? ... wut?
    * This is kinda' weird, but totally makes sense
    * It'll become more obvious as we go. 		  

3. Let's keep writing our constructor by adding some meaningful code (setting attributes):

    .. code-block:: python
        :linenos:
      
        class EnthusiasticStudent:
            '''
            Obv we'll include a nice comment at the top of the class to explain what it's for... right?!

            This EnthusiasticStudent is being used to demonstrate how we can create our own Objects.
		  
            It's going to have a few attributes and some simple functions.
            '''

            def __init__(self, first_name='John', last_name='Doe', student_num='000000000', current_avg=0):
                # Let's just set attributes for now
                self.first_name = first_name 
                self.last_name = last_name
                self.student_num = student_num
                self.current_avg = current_avg

``first_name``, ``last_name``, ``student_num``, and ``current_avg`` are attributes I am giving the object. Each *instance* of a ``EnthusiasticStudent`` will have these attributes, but their values will differ between instances. Think about humans. We all have a name attribute, but our individual names will differ. 

 
.. admonition:: Activity
    :class: activity

    Outside the class, type the following (if using an IDE with multiple files in the same project, open up a **new/different** python file in the same project):
   
    .. code-block:: python
        :linenos:
	  
        #from EnthusiasticStudent import *    # Only need this if using multiple files in IDE
        a_student = EnthusiasticStudent()
   
    1. Figure out how to get the first name from ``a_student``

    2. What is the ``type`` of ``a_student``? The ``type`` of ``EnthusiasticStudent``? How about ``EnthusiasticStudent()``?

    3. Create a new, different student, but this time set the first name to something else. Check its attributes. 

    4. Add a print statement saying "im running from inside a constructor" to your constructor right below where we assigned the attributes. Re-run the code above. What happened? Why?

* We can put whatever code we want in the constructor. Just in our case, setting the attributes is enough to get what we want done.
* **NOTE** ``self`` is pretty important here. If you forget the self, would you be creating an attribute for the object, or a local variable for the constructor?   


3. Let's add some functions/methods to this class.

    .. code-block:: python
        :linenos:
      
        class EnthusiasticStudent:
            '''
            Obv we'll include a nice comment at the top of the class to explain what it's for... right?!

            This EnthusiasticStudent is being used to demonstrate how we can create our own Objects.
		  
            It's going to have a few attributes and some simple functions.
            '''

            def __init__(self, first_name='John', last_name='Doe', student_num='000000000', current_avg=0):
                self.first_name = first_name 
                self.last_name = last_name
                self.student_num = student_num
                self.current_avg = current_avg

            def ask_for_higher_mark(self, howHigh):
                print('Hello Professor,\n\nMy name is ' + self.first_name + ' and I am in your CSCI 161 class. I would really like it if you could just give me a ' + str(howHigh) + '%. \n\nThanks,\n' + self.first_name + ' ' + self.last_name)

            def show_off(self):
                print('I got 100 on my last assignment everyone. I\'m a wizard')
                self.first_name = 'Wizard'


            def work_too_hard_on_assignment(self):
                # I left it blank. Add whatever code you want here. Be sure to delete the pass keyword when you do though
                pass	
            
.. admonition:: Activity
    :class: activity

    1. I have no idea what the code would look like in the ``work_too_hard_on_assignment`` function, so just make up your own. Make it do whatever. 

    2. Create an instance of an ``EnthusiasticStudent`` and figure out how to call the functions. Is there an easy way to see all available?

    3. What happens to the attributes of the object after calling ``show_off``?

__repr__
========

There are a lot of other special functions for classes that you don't *need*, but are super handy. Here are 2 cool ones. 

    .. code-block:: python
        :linenos:
      
        def __repr__(self):
            '''
            A method which will return some string representation of the object. This will he handy for debugging and stuff.
            '''
            return 'First Name: ' + self.first_name + '\nlast_name: ' + self.last_name + '\nStudent Number: ' + self.student_num + '\nCurrent Average: ' + str(self.current_avg)

.. admonition:: Activity
    :class: activity

    1. Add this function to your code. 

    2. Now in your other script call the ``__repr__() `` method on the ``a_student`` object.

    3. Call ``print(a_student)``. What happens?
   
    4. Run this ``a = str(a_student)``, and then check out the ``type`` of ``a``. 

__eq__
======

What does it mean for 2 ``EnthusiasticStudent`` objects to be *equal*?

.. admonition:: Activity
    :class: activity

    1. Create 2 instances of an ``EnthusiasticStudent`` object. Call them ``a`` and ``b``.

    2. Call ``a == b``. What happened? How would python know what it means for two ``EnthusiasticStudent`` objects to be equal?

    3. Copy the below code and re-run. 


    .. code-block:: python
        :linenos:
      
        def __eq__(self, anotherThing):
            '''
            A method to check if 2 EnthusiasticStudent are the same. What does it mean for 2 things to be the same? 
            Well, WE get to make that up!
            (Although, we should pick something that makes sense...)
            '''
            return self.student_num == anotherThing.student_num


    4. Now call ``a.__eq__(b)``. What happens?

    5. Now call ``a == b``. What happens?


The above code may also make it somewhat obvious why the ``self`` reference is important. Which instance of the object do we want the ``student_num`` attribute from?

			
For Next Class
==============

* Read `Chapter 16 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html>`_