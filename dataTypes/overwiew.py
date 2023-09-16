
# Python supports several built-in data types, each of which has specific characteristics and uses. 

"""

Numeric Types:

int: Represents integer values, e.g., 42 or -10.
float: Represents floating-point (decimal) numbers, e.g., 3.14 or -0.5.
complex: Represents complex numbers with a real and imaginary part, e.g., 2+3j.


Text Type:

str: Represents a sequence of characters, e.g., 'Hello, Python!'.


Boolean Type:

bool: Represents a Boolean value, which can be either True or False. Used for logical operations and control flow.


Sequence Types:

list: Represents an ordered, mutable (changeable) collection of items. Lists are created using square brackets, e.g., [1, 2, 3].
tuple: Represents an ordered, immutable (unchangeable) collection of items. Tuples are created using parentheses, e.g., (1, 2, 3).
range: Represents an immutable sequence of numbers. Commonly used for looping.


Mapping Type:

dict: Represents a collection of key-value pairs. Dictionaries are created using curly braces with key-value pairs separated by colons, e.g., {'name': 'Alice', 'age': 30}.


Set Types:

set: Represents an unordered, mutable collection of unique elements. Sets are created using curly braces or the set() constructor, e.g., {1, 2, 3}.
frozenset: Represents an unordered, immutable collection of unique elements. Frozensets are created using the frozenset() constructor.


Sequence Types (Binary):

bytes: Represents a sequence of bytes, which is immutable. Often used in binary data handling, e.g., b'hello'.
bytearray: Represents a mutable sequence of bytes, e.g., bytearray(b'hello').
memoryview: Represents a memory view object of a sequence of bytes.


None Type:

None: Represents a special value indicating the absence of a value or a null value.


Custom Types:

We can also create your own custom data types using classes.

"""

# Python is a dynamically typed language, meaning we don't need to declare the data type of a variable explicitly; it's determined at runtime. For example:

x = 42                  # x is an integer
y = 3.14                # y is a float
name = 'Ceyda'          # name is a string
is_valid = True         # is_valid is a boolean
my_list = [1, 2, 3]     # my_list is a list


# We can get the data type of any object by using the type() function. 

