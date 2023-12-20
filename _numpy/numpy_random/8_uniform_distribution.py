
"""
Uniform Distibution:
    Used to describe probality where every event has equal chances of occuring. 
    E.g. Generating of random numbers.
    
    It has three parameter:
    a - lower bound - default 0.0
    b - upper bound - default 1.0 
    size - The shape of returned array
"""

# Create a 2x3 uniform distribution sample:
from numpy import random

x = random.uniform(size=(2,3))
print(x)

x =random.uniform(1,10, size=10)
print(x)


# Visualization of Uniform Distribution
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(x ,hist=False)
plt.show()

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()