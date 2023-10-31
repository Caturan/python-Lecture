import json

    # Python JSON
"""
JSON is a syntax for storing and exchanging data. 
JSON is text, written with JavaScript object notation. 

Python has a built-in package called json, which can be used to work with JSON data. 
"""
"""
    Parse JSON - Convert from JSON to Python
If we have a JSON string, we can parse it by using the json.loads() method. 

The result will be a Python dictionary. 
"""

# some JSON
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x 
y = json.loads(x)

# the result  is a Python dictionary:
print(y["age"])
print(y)

#print(dir(json))


"""
    Convert from Python to JSON
If we have a Python object, we can convert it into a JSON string by using the json.dumps() method. 
"""
x = {
    "name": "John",
    "age": 22,
    "city": "London"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))
"""
We can convert Python objects of the following types, into JSON strings:
* dict
* list
* tuple
* string
* int
* float
* True
* False
* None
"""

print(json.dumps({"name": "Ahmet", "age": 22}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apples", "bananas")))
print(json.dumps("hello"))
print(json.dumps(22))
print(json.dumps(79.4))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


"""
When we convert from Python to JSON, Python objects are converted into the JSON(JavaScript) equivalent:

    Python                              JSON
    dict                                Object
    list                                Array
    tuple                               Array
    str                                 String
    int                                 Number
    float                               Number
    True                                true
    False                               false
    None                                null
"""


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

"""
    Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentitions and line breaks. 
The json.dumps() method has parameters to make it easier to read the result:
"""
print(json.dumps(x, indent=4))


"""
    Order the Result
The json.dumps() method has parameters to order the keys in the result:
"""
print(json.dumps(x, indent=4, sort_keys=True))
