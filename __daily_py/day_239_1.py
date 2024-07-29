matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
]

sum = 0
for i in range(0, 4):
    for j in range(0, 5):
        if (i + j) % 2 == 0:
            sum += matrix[i][j]
            
print(sum)