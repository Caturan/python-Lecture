# Python Iterators
"""
An iterator is an object that contains a countable number of values. 
An iterator is an object that can be iterated upon, meaning that we can travere through all the values. 
Technically, in Python, an iterator is an object which implements the iterator protocal, which consist of the methods __iter__() and __next__(). 
"""

"""
Lists, tuples, dictionaries, and sets are all iterable objects. Thet are iterable containers 
which we can get an iterator from. 
All these objects have a iter() method which is used to get an iterator:
"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# We can also use a for loop to iterate through an iterable object:
for x in mytuple:
    print(x)

for x in mystr:
    print(x)

# The for loop actaully creates an iterator ıbject and executes the next() method for each loop. 


"""
Create an Iterator
To create an object/class as an iterator we have to implement the methods __iter__()
 and __next__() to our object.
As we have learned, all classes have a function called __init__(), 
 which allows we to do some inializing when the object is being created. 
The __iter__() method acts similar, we can do operations, but must always return the iterator object itself. 
The __next__() method also allows we to do operations, and must return the next item in the sequence. 
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1 
        return x 

myclass = MyNumbers()
myiter = iter(myclass)

print(iter(myiter))

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 


"""
StopIteration
The example above would continue forever if we had enough next() statements, or if it was used in a for loop. 
To prevent the iteration from going on forever, we can use the StopIteration statement. 
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x 
        else :
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)



# Another example code:
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        raise StopIteration

# Creating an iterable object
my_iterable = MyIterator(2, 8)

# Using the iterator
for item in my_iterable:
    print(item)

