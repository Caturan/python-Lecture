import matplotlib.pyplot as plt 

x = range(5)
y = [2, 4, 3, 5, 4]
errors = [0.5, 0.3, 0.4, 0.6, 0.2]

plt.errorbar(x, y, yerr=errors, fmt='o', capsize=5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Error Bars')
plt.show()