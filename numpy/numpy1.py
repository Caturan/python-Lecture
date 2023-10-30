# Iterables - Sequences - Iterators

# Iterable
"""
An iteables is any object that can be looped over. 
It represents a collection of elements that can be accesses one by one. 

An object is considered iterable if:
- It implements the __iter__() method which returns an iterator. 
- It defines the __getitem() method that can fetch items using integer indices starting from zero. 
""" 

# Sequence
"""
A sequence is a subtype of iterables. It's an ordered collection of elements that can be indexed by numbers. 

Ordered: Elements in a sequence have a specific order. 
Indexable: We can get any item using an index: my_sequence[4]
Slicable: Supports slicing to get some of items: my_sequence[2:5]
"""

# Iterator
"""
An iterator is an object that produces items (one at a time) from its associated iterable. 

- Stateful: An iterator remembers its state between calls. Once element is consumed, 
 it can't be accessed again without reinitializing the iterator.
- Lazy Evaluation: Items are not produced from the source iterable until the iterator's __next__() method is called. 
- Iterators raise a StopIteration exception when there are no more items to return. 
- An iterator's __iter__() method returns the iterator object itself. 
- While all iterables must be able to produce an iterator (with __iter__() method),
 not all iterators are directly iterable without using a loop.  
  
"""


