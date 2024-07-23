import matplotlib.pyplot as plt 
categories = ['Category']
values = [75]
ranges = [(50, 100)]
markers = [85]
fig, ax = plt.subplots()
ax.barh(categories, values, color='lightblue')
for i, (low, high) in enumerate(ranges):
    ax.plot([low, high], [i]*2, color='black')
    ax.plot([markers[i]], [i], marker='o', markersize=25, color='red')
plt.title('Bullet Chart')
plt.show()