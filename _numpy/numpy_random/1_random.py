import numpy as np 

"""
What is a Random Number?
    Random number does NOT mean a different number every time.
    Random means something that can not be predicted logically. 
"""

"""
Pseudo Random and True Random:
    Computer work on programs, and programs are definitive set of instructions. 
     So it means there must be some algorithm to generate a random number as well. 

    If there is a program to generate random number it can be predicted, thus it is not truly random. 

    Random numbers generated through a generation algorithm are called pseudo random. 

    Can we make trult random numbers? 
    Yes. In order to generate a truly random number on our computers we need to get the random data from some outisde source. 
     This outside source is generally our keystrokes, mouse movements, data on network etc. 

    We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or the basis of application is the randomness. (Digital roulete wheels)
"""

"""
Generate Random Number:
    NumPy offers the random module to work with random numbers. 
"""
from numpy import random 

x = random.randint(100)
print(x)


"""
Generate Random Float:
    The random module's rand() method returns a random float between 0 and 1. 
"""
x = random.rand()
print(x)


"""
Generate Random Array:
    In NumPy we work with arrays we can use the two methods from the above examples to make random arrays. 
    
    Integer:
    The randin() method takes a size parameter where we can specify the shape of an array. 
"""
x = random.randint(100, size=(5))
print(x)

print()

x = random.randint(100, size=(3,5))
print(x)

print()

"""
    Floats:
    The rand() method also allows we to specify the shape of the array. 
"""
x = random.rand(5)
print(x)

print()

x = random.rand(3,5)
print(x)

print()

"""
Generate Random Number From Array:
    The choice() method allows us to generate a random value based on an array of values.
    The choice() method takes an array as a parameter and randomly returns one of the values. 
"""
x = random.choice([3,5,7,9])
print(x)

"""
    The choice() method also allows us to return an array of values. 
    Add a size parameter to specify the shape of the array. 
"""
x = random.choice([3,5,7,9], size=(3,5))
print(x)
