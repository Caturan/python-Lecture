import matplotlib.pyplot as plt 
import seaborn as sns 

"""
Visualize Distribution With Seaborn:
    Seaborn is a library that used Matplolib underneath to plot graphs. It will be used to visualize random distibutions. 
"""

"""
Displots:
    Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array. 
"""

sns.distplot([0,1,2,3,4,5])
plt.show()

# Plotting a Displot Without the Histogram
sns.distplot([0,1,2,3,4,5], hist=False)
plt.show()

# Note: We will be using: sns.distplot(arr, histFalse) to visualize random distributions in this tutorial. 