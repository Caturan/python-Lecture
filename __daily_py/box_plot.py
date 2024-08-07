import seaborn as sns 
import numpy as np 
import matplotlib.pyplot as plt 

# Generate random data 
data = np.random.randn(100)

# Create a box plot 
sns.boxplot(data=data)
plt.title('Box Plot Example')
plt.show()