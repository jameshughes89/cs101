*******
Lab #10
*******

Before Kattis
=============

This lab relates to topics discussed in :doc:`class 13 </topic13>` and :doc:`class 13b </topic13b>`.

Let's make a small program with classes. We'll make a program that will store a contact list of people. 

We want 2 classes, and another script to interact with the objects we create. 

Person
======

Start by making a simple object to store information for a ``Person``. Create a ``Person`` class. 

If using PyCharm or Spyder, open an empty python file in your working directory/project. Call it *Person.py*

**Attributes**

* A first name (``_first_name``)
* A last name (``_last_name``)
* An email (``_email``)

There, that's it for now. We can add more later if we want. 

**Methods**

* Constructor
* Getters/setters for the attributes. 
    * eg: ``get_first_name(self)``, ``set_first_name(self, newFirstName)``
* The repr method (``__repr__``)
    * You decide what should be returned here to give us a string representation of the object. Just come up with something reasonable. 
    * My output looked like this 
        ``Smith, Greg:	gsmith@xfts.ca``
	
* The equals method (``__eq__``)
    * You decide what it is for two ``Person`` objects to be equivalent. 
	
That's about it for the ``Person`` object. It's pretty simple. 

ContactList
===========

Now let's make a class called ``ContactList`` to hold onto a list of ``Person`` objects. If using PyCharm or Spyder, open another empty python file in your working directory/project. Call it *ContactList.py*. Be sure to import the ``Person`` class at the top of this file.

**Attributes**

* A list of friends

That's all I think we'll need for now. 

**Methods**

* The constructor
    * We don't really need to give this any parameters actually (except we need ``self``). 
    * Here we *could* pass it a list I guess, but let's not.
    * We do want a list attribute though.

* add_friend --- a method to add a ``Person`` object to the contact list.
    * See that. **We need to create a Person OBJECT**.
    * Here we have a design decision to make. Which parameters should the method get?
        * Should we pass a reference to a ``Person`` object to the method 
            ``def add_friend(self, aPerson):``
			
        * Should we pass the details to make a person to the method? 
            ``def add_friend(self, fName, lName, email):``
		
    * Hard to really say actually. For now let's go with the 2nd option. 
    * The choice will really impact how we *interface* with the objects.
	
	
* ``__repr__``
    * You decide what string should be returned. Just be sure to use the ``__repr__`` for the ``Person`` objects. 
        * How do we convert something to a ``str``?
    * My output looked like this, but do whatever you want really (as long as it makes sense)
	
    .. code-block:: python
    
        Contact List
        0 Sehguh, Semaj:	ssehguh@xfts.ca
        1 Smith, Greg:	gsmith@xfts.ca


If you are stuck on any of this, :doc:`you should have a look here </topic13b>`.		
		
Using Them Together
===================

Create ANOTHER file and put this in it:

.. code-block:: python
    :linenos:	

    #from ContactList import *      # Only need if using multiple files 

    friends_list = ContactList()
    friends_list.add_friend('Semaj', 'Sehguh', 'ssehguh@xfts.ca')
    friends_list.add_friend('Greg', 'Smith', 'gsmith@xfts.ca')

    print(friends_list)
	
Everything should work. If not, ask for help. 

More Special Functions
======================	

Add these to the ``ContactList`` class. 
	
* ``__len__`` --- A method that returns the length of the ``ContactList`` (the length of the list of friends)
    * I wonder how we can then use this to get the ``len`` of the object?
    * Try adding this to the script we're running to test it out
        ``print(len(friends_list))``
    * ``len`` calls the ``__len__`` method. 
	
* ``__getitem__`` --- A method that returns a ``Person`` object from a given index in the list of friends. 
    * Try adding this to the script we're running to test it out
        ``print(friends_list[1])``
    * indexing with ``[x]`` calls the ``__getitem__`` method. 

Testing
=======

You should be able to run the below code and everything should work correctly. If not, ask for help. 


.. code-block:: python
    :linenos:	
	
    # Only need these if using multiple files
    #from Person import *
    #from ContactList import *

    friends_list = ContactList()
    friends_list.add_friend('Semaj', 'Sehguh', 'ssehguh@xfts.ca')
    friends_list.add_friend('Greg', 'Smith', 'gsmith@xfts.ca')

    print(friends_list)
    print(len(friends_list))
    a_friend = friends_list[1]
    print(a_friend)

    # This just makes sure that a_friend is 
    # pointing to a a Person object.
    # If it is, nothing special happens
    # If it's not, it will crash the program
    assert isinstance(a_friend, Person)

    print(a_friend.get_first_name())
    print(a_friend.get_last_name())
    print(a_friend.get_email())
    a_friend.set_first_name('Not')
    a_friend.set_last_name('A')
    a_friend.set_email('Thing')

    print(friends_list)
	
	
Make sure it makes sense to you *why* when we print out ``friends_list`` we now wee an altered person. 	
	

Add Some Things
===============

Now that you have everything working, go add some additional attributes to the ``Person`` class, update methods, add new methods, use the methods in the ``ContactList`` class, etc. Basically I just want you to go nuts and see what you can do. 

Maybe go even loop up other special python methods and see if you can hac them to work in weird ways. 

Kattis Problems
===============

Can you do these with something other than lists? In fact, you might have to for the runtime requirements. You may come up with a perfect solution that will be correct 100% of the time; however, a correct solution is not necessarily a *good* solution. 

1. https://open.kattis.com/problems/everywhere 
2. https://open.kattis.com/problems/babelfish
3. https://open.kattis.com/problems/oddmanout
4. https://open.kattis.com/problems/securedoors
5. https://open.kattis.com/problems/modulo

LeetCode Problems
=================

The following problem is a **classic** CS programming problem.

1. https://leetcode.com/problems/two-sum/

If you finish the lab, go back and work on incomplete problems from previous labs. 

At this point, many of the not-so-difficult problems are totally doable by you now. If you're looking for more problems, or want more practice for tests, etc. sort the Kattis problems by difficulty and have fun. 

If you have somehow finished everything so far, go check out `LeetCode <https://leetcode.com/problemset/all/>`_. Sort the problems by *Acceptance* (click the table header) and start seeing if you can solve some of these problems. 

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
