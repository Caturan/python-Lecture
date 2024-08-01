def sum(num):
    if num == 1:
        return 1 
    
    return num + sum(num - 1)

print(sum(4), sum(3), sum(2))
