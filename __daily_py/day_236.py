d = {'a':1, 'b': 2, 'c':3}
print(dict.fromkeys(d, 0))

"""
The dict.fromkeys method is used to create a new dictionary from the keys of an existing iterable (in this case, the dictionary d)

In this code, d is used to as the iterable. When d is used as an iterable, it provides its keys ('a','b','c'). 
 The second argument is 0, which means all keys in the new dictionary will have the values 0. 
"""