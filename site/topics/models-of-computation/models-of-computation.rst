*********************
Models of Computation
*********************

* As we have progressed through the course, we have gained an intuition of how everything works
* Everything we have done up until this point is *Computer Science*
* However, computer science is a very broad field with many subfields, and programming is only a part of it
* Although all these subfields are different from one another, most, if not all, have the same core underlying fundamentals

* Up until this point in the course, how much thought has been given to

    * *What is computation?*
    * *What is a computer?*
    * *What enables a computer to do what it does?*
    * *What can a computer compute?*

* These ideas are a very big part of what computer science is
* Since this is an introductory course preparing you for computer science degrees, it would be prudent to take time to become aware of the foundational ideas
* Further, it provides an opportunity to consider the underlying mathematics of everything we have done so far

    * The mathematics provides a formal and precise way to demonstrate what problems can or cannot be solved with a given computational system

* Due to the requisite knowledge required to really get into these ideas, this topic presents a high-level introduction of the underlying ideas
* Although kept at a high-level, it should be sufficient to contextualize computational systems
* Further, it will help you gain an appreciation of the levels of abstraction between you, a programmer, and the fundamental truths of our universe that enable computation


Finite State Machines/Automata (FSM/FSA)
========================================

* The computers you use, like those that sit on your desks, are only one type of computer within one class of computational systems

* We can define a very very very very simple computer in terms of 
    * Input 
    * Output
    * States
    
* With this, we can spend time thinking about what exactly a simple little computer like this can do

    * What types of problems this computer can solve

* FSMs are **VERY** simple computers
* But, just because they're simple, doesn't mean we can't use them
* In fact, these extraordinarily simple computers are used to solve many problems we deal with every day

    * Vending Machines
    * Traffic Lights
    * Elevators
    * Locks/Safe
    * Regular Expressions 

* Let's say we want a lock that has the combination **7, 7, 3**
* Below is a representation of a FSM for that lock

.. image:: FSM_lock.png

* The FSM receives input, and depending on the input the FSM's state may change
* If the FSM receives input such that the machine halts on the accepting state (double circled state), then, in this context, the lock would open
* For example, if the machine receives the input **7, 7, 3**, the final state would be the accepting state

* The above lock example started with what the correct sequence is, and then a FSM was designed for it
* But we can also start from a FSM and ask, *what kinds of inputs does this machine accept?*

.. image:: FSM_regex.png

.. admonition:: Activity
    :class: activity

    Consider how the lock example hits the accepting state after seeing **7, 7, 3**.

    What input strings can this machine accept? What I mean is, what strings will get this machine to it's final state?


* Think of how simple this computational system is, while also considering how powerful it is in terms of the problems it could solve
* Computer Scientists like to think about *what else can a computer this powerful do?*
    

Pushdown Automata (PDA) and Context-Free Grammars 
=================================================

* FSMs, although powerful, are very limited in the types of problems they can be used for
* If we want to solve more *complex* problems, we need a more powerful machine

    * But what exactly is a more complex problem?

* Pushdown Automatas (PDAs) are strictly more powerful when compared to FSMs

    * They can solve more problems than FSMs
    * Anything a FSM can do, a PDA can do
    * But there are many things a PDA can do that a FSM cannot

* PDAs have a mechanism for memory, which is what gives them an edge over FSMs

    * A pushdown is an old name for a stack
    * The memory is the informatioon stored in the stack

* Getting into the theoretical construction of a PDA is beyond what we will consider here, but we can discuss what we can do with them
* PDAs recognize what we call Context-Free Grammars (CFG)
* Here's an example of doing the same thing as the 2nd FSM with a CFG

    :math:`S \rightarrow aA`

    :math:`S \rightarrow bB`

    :math:`A \rightarrow aA`

    :math:`A \rightarrow b`

    :math:`B \rightarrow bB`

    :math:`B \rightarrow a`

* Here, the upper case letters are special symbols that mean you can replace them in a string with whatever is on the right hand side
* The lower case letters are just letters

* Start with S

    * String: :math:`S`

* We have two options, let's go with the first

    * String: :math:`aA`

* We now have an A, so let's go with the first options

    * String: :math:`aaA`

* Let's do it again

    * String: :math:`aaaA`

* Let's do it 4 more times

    * String: :math:`aaaaaaaA`

* Now let's go with the second option

    * String: :math:`aaaaaaab`

* No more upper case letters, so we're done.

    * String: :math:`aaaaaaab`

    
* Here's another CFG

    :math:`S \rightarrow aSa`
    
    :math:`S \rightarrow bSb`
    
    :math:`S \rightarrow \epsilon`
    
    :math:`\epsilon` --- empty string


* An interesting note about this one is, no matter how hard you try, it is provably impossible to create a FSM that accepts the same set of strings


.. admonition:: Activity
    :class: activity
   
    What strings can this system create? Try to generate a few strings and see if you can generalize and see the big
    picture of what it's doing exactly.


* Another one   

    :math:`S \rightarrow SS`
    
    :math:`S \rightarrow (S)`

    :math:`S \rightarrow ()`

    :math:`S \rightarrow \epsilon`


.. admonition:: Activity
    :class: activity
   
    What strings can this system create? Try to generate a few strings and see if you can generalize and see the big
    picture of what it's doing exactly.


* Although the PDAs are more *powerful* than FSMs, they are still limited in what they can do
* But the point is, despite their limitations, they can still do quite a bit
* And the PDAs are, by definition, computers capable of processing information


Context-Sensitive Grammars
==========================

* If we have context matter, we can get more interesting resulting strings than we could with CFGs
* With Context-Sensitive Grammars (CSGs), the rule (left hand side) can only be applied if the correct *context* exists

    * For example, in the below set of rules, the :math:`Ab` rule can only be applied if the string contains :math:`Ab`


    :math:`S \rightarrow abc`
    
    :math:`S \rightarrow aAbc`
    
    :math:`Ab \rightarrow bA`
    
    :math:`Ac \rightarrow Bbcc`
    
    :math:`bB \rightarrow Bb`
    
    :math:`aB \rightarrow aa`
    
    :math:`aB \rightarrow aaA`


* The strings that this CSG can generate are rather interesting, and it is impossible to create a FSM or use CFGs to accept/generate the same set of strings


.. admonition:: Activity
    :class: activity

    What strings can this system create? Try to generate a few strings and see if you can generalize and see the big
    picture of what it's doing exactly.


* Like the CFGs, CSGs have limitations
* But like before, that does not mean they are not capable of solving/addressing many problems
* Again, these are *computers*, by definition


Turing Machines 
===============

.. image:: TuringMachine.jpg
    :target: https://en.wikipedia.org/wiki/Turing_machine

* Turing Machines are even more powerful models of computation
* The types of languages/strings that Turing Machines work with are called *Recursively Enumerable Languages*
* The computers we use today are computationally equivalent to  these

    * They're not built like these, but they are as powerful
    * Can solve the same problems

* Given the relative complexity of Turing Machines, it is difficult to cover them here

    * Don't worry, you will learn all about them later in your computer science degree

* Turing machines are made up of

    * An infinitely long (sufficiently long) linear *tape* that can have symbols written to it --- the tape is memory
    * A *read/write head* that can more left and right, and read symbols from and write symbols to the tape
    * A *state register* to keep track of some internal state
    * A finite *table of instructions* that instructs how to operate the read/write head given the current state --- the table is a program

* Although Turing Machines are more complex than the other models of computation, the takeaway is that these still remarkably simple models of computation are sufficient for implementing any computer program
* Computers we use today, although built differently, are computationally equivalent to Turing Machines

* The point is, Turing Machines were formalized in 1936
* Everything we do on a computer is built upon these simple ideas
* Every program you have written so far is built on these ideas
* Fortunately, we were able to program our computers with Python at a much higher level of abstraction
* But ultimately, all that is possible because of the levels of abstraction that came before Python


.. admonition:: Activity
    :class: activity

    Can you define another class of computational system strictly more powerful than a Turing Machine?


For Next Class
==============

* `Read Chapter 18 <http://openbookproject.net/thinkcs/python/english3e/recursion.html>`_


