# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    n = list(range(low, high + 1))
    min = 0
    max = len(n)

    #Find the midpoint
    while max >= min:
        #finds the average of the min and the difference between max and min.
        MidPoint = math.floor(min + (max - min)/2)
    #check midpoint is the answer
        if n[MidPoint] is actual_number:
            return {"guess": guess, "tries": tries}
        #Higher or lower than midpoint
        elif n[MidPoint] > actual_number:
            #add try
            tries +=1
            guess = n[MidPoint]
            #new maximum
            max = MidPoint - 1
    
        else:
            #add try
            tries += 1
            guess = n[MidPoint]
            #new minimum is the midpoint + 1
            min = MidPoint + 1
    return {"guess": guess, "tries": tries}
    

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))



