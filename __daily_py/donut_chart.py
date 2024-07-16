import matplotlib.pyplot as plt 

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
circle = plt.Circle((0,0), 0.8, color='white')
plt.gca().add_artist(circle)
plt.title('Donut Chart')
plt.show()