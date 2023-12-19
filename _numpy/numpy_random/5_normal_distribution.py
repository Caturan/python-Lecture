from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns

""" 
Normal (Gaussian) Distribution:
    The Normal Distribution is one of the most important distributions. 
    It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss. 
    It fits the probality distribution of many event, eg. IQ Scores, Heartbeat etc. 

    Use the random.normal() method get a Normal Data Distribution. 
    It has three parameters:
    loc - (Mean) where the peak of the bell exists. 
    scale - (Standard Deviation) how flat the graph distribution should be. 
    size - The shape of the returned array. 
"""

x = random.normal(size=(2,3))
print(x)

print()

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2,3))
print(x)


# Visualization of Normal Distribution
sns.distplot(random.normal(size=100), hist=False)
plt.show()


# Note: The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve. 


