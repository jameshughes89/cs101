*****
Debug
*****

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

* There are no exercises to complete before this lab



Before Kattis
=============

**1**

Using ``print`` statements, fix this code...

.. code-block:: python

    def count_numbers_up_to(n):
        '''
        This function adds up all the numbers from 0 - n exclusively.
        Eg. 5 -> 0 + 1 + 2 + 3 + 4 -> 10

        :param n: The number we are counting to. Note we do not count n
        :return: The sum of the numbers
        '''

        total = 0
        c = 0
        while c < n:
            c += 1
            total += c
        
        return total

**2**

Using pencil and paper, fix this code...

.. code-block:: python

    def find_max_index(aList):
        '''
        This function takes a list and returns the INDEX of where the largest
        element is inside the list. If there are multiple copies of the max,
        it will return only the index of the first occurrence

        :param aList: A list of integers
        :return: The index where the first max number is
        '''
        curMax = aList[0]
        curMaxIndex = 0
        c = 0
        while c < len(aList):
            if aList[c] > curMax:
                curMax = aList[c]
                curMaxIndex += 1
            
            c +=1

        return curMaxIndex

	  
**3**

Using delta debugging (comment out all code, and then start un-commenting the code one-ish line at a time), fix this code... **HINT**: You're going to want to combine this strategy with the ``print`` strategy.  

.. code-block:: python

    def ones_in_corners(n):
        '''
        Creates an nxn matrix full of 0s, except the corners of the matrix
        will have 1s in it.
        eg. ones_in_corners(3) would give us
        1 0 1
        0 0 0
        1 0 1


        :param n: the size of the square matrix
        :return:
        '''
	  
        # setup a single row of n ' ' (space) chars
        row = ['0'] * n

        # now we will make the mat have n rows
        mat = [row] * n

        # the following four lines make it so only
        # the corners of the matrix has 1s
        mat[0][0] = '1'
        mat[0][n-1] ='1'
        mat[n-1][0] = '1'
        mat[n-1][n-1] = '1'
        return mat	  
	  
	    
**4 Using a debugger**

To get our hands dirty, let's start by re-fixing one of the above problems with a debugger. 

Obviously you should know where the problem is given that you fixed this above, but still go through this exercise. 


.. code-block:: python
    :linenos:
    
    def find_max_index(aList):
        '''
        This function takes a list and returns the INDEX of where the largest
        element is inside the list. If there are multiple copies of the max,
        it will return only the index of the first occurrence

        :param aList: A list of integers
        :return: The index where the first max number is
        '''
        curMax = aList[0]
        curMaxIndex = 0
        c = 0
        while c < len(aList):
            if aList[c] > curMax:
                curMax = aList[c]
                curMaxIndex += 1

            c +=1

        return curMaxIndex

    print(find_max_index([5,2,8,9,5,4,3]))


1. Copy this into PyCharm.
2. Set a *break point* on line 13 **NOTE, THIS WILL PROBABLY BE A DIFFERENT LINE NUMBER WHEN YOU COPY IT**	 
3. Start the **debugger**. 
4. Add a *watch* for the condition on line 13 (``c < len(aList)``)
5. Add a *watch* for the condition on like 14 (``aList[c] > curMax``)
6. Now you will press the *step into* button. Take your time with this, for real. If you don't, you're using the debugger wrong and it won't actually be helpful. This is where the magic happens. The trick is to (a) do **not** skip a step, (b) do **not** make any assumptions, (c) critically think about what *should* happen if the code was correct, and compare your hypothesis to what is *actually* happening, (d) oh, and TAKE YOUR TIME. 

7. I know you know where the problem is, so just spay special attention to what your hypothesis for ``curMaxIndex`` should be when ``curMax`` is set to 8, and how the code actually reacts.
	  

**5 Use whatever you want now**

I'm just going to throw a bunch of buggy code your way. Fix it however you want. 

.. code-block:: python
    :linenos:
    
    def make_a_string_from_list(a):
        '''
        Take a list, and convert it to a string version of the contents of the list
        eg.
        a = [1,2,'a','b']
        return '12ab'
        
        :param a: the list we want turned into a string
        :return: a string version of the list
        '''

        # always have to start with an
        # empty string when string building
        s = ''
        for thing in a:
            s = str(a) + s

        return s

    # maStr should be '12ab'
    maStr = make_a_string_from_list([1,2,'a','b'])
    print(maStr)


.. code-block:: python
    :linenos:
    
    def grocery_bill(a, b):
        prices = {'apple': 0.40, 'banana': 0.50}
        my_purchase = {'apple': a, 'banana': a}
        grocery_bill = 0
        for fruit in my_purchase:
            grocery_bill = prices[fruit] * my_purchase[fruit]
        return 'I owe the grocer ' + str(grocery_bill)
   
    # Should be 2.90
    print(grocery_bill(1, 5))

``set_up_game`` is tricky because it's hard to even discover that there is a problem. Test this a lot to see if you can find the error. 
   
.. code-block:: python
    :linenos:
    
    def set_up_game(size):
        '''
        Sets up the game board based to be the size we want.
        It will be size x size. Eg. 3x3 if size is 3
        Will be a list of lists
        [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
        
        :param size: The size of the world. Will be size x size.
        :return: The list of lists representing the game world. 
        '''
        a = [' '] * size
        b = [a] * size
        return b

.. code-block:: python
    :linenos:
    
    def give_me_5_words():
        '''
        This function will ask the user for 5 words.
        It will print out the full word they entered
        And also add the full word to a list that will be returned
        
        :return: The list of the 5 words they entered
        '''
        
        a = []
        for _ in range(5):
            word = input('Gimmie: ')
            a.append(word[0])
            print('You gave me the word: ' + a[0])
            return a

    '''
    Should work like this in:
    Gimmie: ab
    You gave me the word: ab
    Gimmie: bc
    You gave me the word: bc
    Gimmie: cd
    You gave me the word: cd
    Gimmie: ef
    You gave me the word: ef
    Gimmie: gh
    You gave me the word: gh
    ['ab', 'bc', 'cd', 'ef', 'gh']
    '''
    print(give_me_5_words())
	  
.. code-block:: python
    :linenos:
    
    def message(text, plain, encryp):
        '''
        Perform a simple encription.
        Eg.
        plaintext  =  list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        encryptedtext=list('DEFGHIJKLMNOPQRSTUVWXYZABC')
        message("This is a test", plaintext, encryptedtext)
        should result in:
            THIS IS A TEST
            has been encrypted to:
            WKLV LV D WHVW
		 
        :param text: The message to encript
        :param plain: The alphabet that the text exists in
        :param encryp: The alphabet that we want o encript to. order matters.
        :return:
        '''

        text = text.upper()
        dictionary = dict(zip(plain, encryp))
        newmessage = ''
        i = 0
        for char in text:
            try:
                newmessage += dictionary[i]
            except:
                newmessage += ' '
            i = i + 1
        print(text, '\nhas been encrypted to:')
        print(newmessage)

    plaintext = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    encryptedtext = list('DEFGHIJKLMNOPQRSTUVWXYZABC')
    message("This is a test", plaintext, encryptedtext)  

This one is very buggy :( 

.. code-block:: python
    :linenos:  
    
    import random

    guesses_made = 0

    name = input('Hello! What is your name?\n')

    number = random.randint(1, 20)
    print('Well, {0}, I am thinking of a number between 1 and 20. You get 6 guesses.'.format(name))

    while guesses_made < 6:

        guess = int(input('Take a guess: '))

        guesses_made += 0

        if guess < number:
            print('Your guess is too low.')

        if guess < number:
            print('Your guess is too high.')

        if guess = number:
            break

    if guess == number:
        print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
    else:
        print('Nope. The number I was thinking of was {0}'.format(number))



Kattis Problems
===============

I'm willing to bet that in previous weeks you were working on Kattis problems that you couldn't quite debug. You may have been close, or way off, but the problem was you were stuck wondering how best to *fix* your code. Now that you're equipped with the debugger, go back and work on them! Seriously, GO BACK! But make use of this debugger. Whenever you can, USE THE DEBUGGER. Stuck on Kattis? DEBUGGER! Stuck on assignment? DEBUGGER! Stuck in life? DEBUGGER?

If you're done everything I have listed so far, try some of the *easy* Kattis problems on the website that I didn't assign. 


LeetCode Problems
=================

If you have somehow finished everything so far, go check out `LeetCode <https://leetcode.com/problemset/all/>`_. Sort the problems by *Acceptance* (click the table header) and start seeing if you can solve some of these problems. 
