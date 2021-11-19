*******
Lab #11
*******

Before Kattis
=============

**1**

Let's start with something simple. Write a function to do a linear search on a list. So, write a function called ``find_element(thing, inList)`` that will search for ``thing`` in ``inList``. Have this function return ``True`` if it exists in the list, and have it return ``False`` otherwise. 

**2**

Create a new class called ``SomeClass``. This class will be really simple to start. 

* Make it the class ``SomeClass``
* Write a constructor that literally does nothing. Like, no parameters other than ``self``.  Then, I don't know, make the constructor print out a message. Something like "I'm code running in the constructor". This is just so when you test it you know it's running. 

There, that's it for that class for now. 

To finish off part **2**, just create an instance of the object in the original script you created. Make sure the message is printed out. If it didn't something is wrong and you need to ask for help. 

**3**

Now we're going to do something very contrived. If you're wondering *But... Why...* after this one, you're normal. Just do what I'm saying at this point. 

Move the ``find_element(thing, inList)`` function to within the class ``SomeClass``. Just copy and paste it in. There is one key thing you'll have to change. What do all methods in a class need as their first parameter? Make that change. 

Go back to your original script (the not-class one) and call the ``find_element`` method from the ``SomeClass`` object you created. 

**4**

For this bit, we're going to update the constructor for ``SomeClass``. 

* Add 2 parameter to the constructor
    * thing
    * inList

* Now, call the function ``find_element`` from *within* the constructor for ``SomeClass``. Be sure to just pass along the parameters. Be sure to save the result into some attribute called ``self._was_it_there``.

    * You might have a hard time doing this. If so, slow down and think about this...
    * Assume in part **3** we had:
    
    .. code-block:: python
        :linenos:
        
        # from SomeClass import *
        
        anObject = SomeClass()
        anObject.find_element(5, [1,2,3,4,5])
        
    * Here, ``anObject`` is a *pointer to a SomeClass object*
    * Whenever we call a method for an object, **we need a pointer to the object to access the attributes/methods**. 
    * So, when we move calling the method ``find_element`` to within the class, guess how we access the method ``find_element``?

* Write a getter for the only class attribute.    
    
Go back to the not-class part of the code and alter it to be able to still effectively call the ``find_element`` method and then get the result. To do this, you'll just need to call the constructor. The constructor will call the method for us. We then need to ask the object about the ``_was_it_there`` attribute through the getter. 

.. Warning:: 
   If this seemed contrived, it was. If you're wondering what the point was, and how this makes no sense, you're not really wrong. I'm just showing you how to use these things in weird ways. 
   
**5**

Here's the plan for this part. Instead of doing a linear search on a list, let's do a linear search through the file. 

To do this, we'll add some file IO to this constructor. Remember, a constructor is just a method/function, so we can basically do anything we want in here that we can do with any other method/function. 

* Remove the ``inList`` parameter from the constructor. 

* Give the constructor a new parameter, call it ``fileName`` or something. This will be the name of a file we want to open. This file will contain the information for the we want to see if something is in. 

    .. code-block:: python
        :linenos:
        
        # Order doesn't matter here. 
        def __init__(self, fileName, thing):
            ...
        


* We'll use the ``fileName`` parameter to open up a file. :doc:`If you forget how to do this, good news, it's in some of the lecture material </topic12>`. 

There are a bunch of ways we can go about the next bit, but let's do it this way. Instead of just searching through the file, let's just load all the information into a list. Then after it's in the list, we'll just search the list. 

* Create an empty list that we will put the contents of the file in.

.. Warning:: 
   Both the file and list objects do **not** need to be attributes. They can just be local variables (so, like very other variable we've used so far). We *could* make them attributes, but there is no need to here. 
   
* Read the file line by line and put the contents in the list. **You'll probably want to turn these from strings to ints**.
    * Don't know how to read a file line by line? `Good thing Google exists then. <https://www.google.ca/>`_ 

* Remember ``find_element``, a method that needs a ``thing`` and a ``inList``? We can just call this method from within the constructor again but give it the list we just created. 

* Be sure we're setting the attribute ``_was_it_there``.

* The trick now is to figure out how to make this all work. Despite the *trick*, there is no magic here. You should be able to figure this out.
    * Run this with the files :download:`toSearchA<../data/toSearchA.txt>` and :download:`toSearchB<../data/toSearchB.txt>` 
    
* Call the getter for the attribute. 
* print out the result. 
    


Kattis Problems
===============

Go back and work on Kattis problems you have yet to solve. I'm betting there are **A LOT** of the early ones you got stuck on that you could not demolish. 

Remember, the Kattis problems are great for practice, and practice is the only way to get good at programming. 

At this point, many of the not-so-difficult problems are totally doable by you now. If you're looking for more problems, or want more practice for tests, etc. sort the Kattis problems by difficulty and have fun. 

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
