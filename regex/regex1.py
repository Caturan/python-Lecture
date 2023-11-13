
        # Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. 
"""
Before learn the RegEx we should define the 'What is the pattern?' 
    Pattern 
In computer scince, the term "pattern" generally refers to a repeated structure or a specific form. 
It is used in various contexts, including: 

1. Programming and Software Development:
 * Design Patters: In software development, design patterns represent general solutions to recurring problems. 
    For example, the "Singleton" pattern is used to ensure that a class has only one instance. 

 * Regular Expressions: Regular expressions are used to define and match specific patterns in text. 
    This applied in text mining, data analysis, and text processing.   

2. Data Mining and Customer Analytics:
 * Pattern Recognition: This involves recognizing repeated structures in datasets. 
    For instance, analyzing customer behaviours on an e-commerce site to identify shopping patterns in an example. 

3. Image Processing and Computer Vision: 
 * Image Patterns: This refers to algorithm used to recognize specific objects or structures in images. 
    For example, facial recognition algorithms can identify a person's face based on a specific pattern. 

4. Database Management:
 * Database Patterns: In database design, design patterns are used to address specific problems. 
    The "Repository Pattern", for instance, abstracts database operations for more effective management. 

These examples illustrate the broad application of the term "pattern" in computer science. 
Fundemantally, it is used to decribe and develop solutions for repeated structures,
whether in software design, data analysis,image processing, or database management. 
"""

# RegEx can be used to check if a string contains the specified search pattern. 

# Python has a built-in package called re, which can be used to work with Regular Expressions. 
import re

# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

"""
The re module offers a set of functions that allows us to search a string for a match. 
 findall -> Return a list containing all matches. 
 search  -> Returns a Match object if there is a match anywhere in the string. 
 split   -> Returns a list where the string has been split at each match. 
 sub     -> Replaces one or many matches with a string. 
"""

"""
    Metacharacters 

[] 	A set of characters   ->    "[a-m]" 	
\ 	Signals a special sequence (can also be used to escape special characters) ->  "\d" 	
. 	Any character (except newline character)  ->  "he..o" 	
^ 	Starts with  ->  "^hello" 	
$ 	Ends with   ->  "planet$" 	
* 	Zero or more occurrences ->  "he.*o" 	
+ 	One or more occurrences  ->  "he.+o" 	
? 	Zero or one occurrences  ->  "he.?o" 	
{} 	Exactly the specified number of occurrences -> "he.{2}o" 	
| 	Either or -> "falls|stays" 	
() 	Capture and group
"""

"""
    Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\A 	Returns a match if the specified characters are at the beginning of the string 		

\b 	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")  	

\B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	

\d 	Returns a match where the string contains digits (numbers from 0-9) 	

\D 	Returns a match where the string DOES NOT contain digits 	 	

\s 	Returns a match where the string contains a white space character 		

\S 	Returns a match where the string DOES NOT contain a white space character 	

\w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	

\W 	Returns a match where the string DOES NOT contain any word characters 	

\Z 	Returns a match if the specified characters are at the end of the string 	

"""

"""
    Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

[arn] 	Returns a match where one of the specified characters (a, r, or n) is present 	
[a-n] 	Returns a match for any lower case character, alphabetically between a and n 	
[^arn] 	Returns a match for any character EXCEPT a, r, and n 	
[0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
[0-9] 	Returns a match for any digit between 0 and 9 	
[0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
[a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
[+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string 	s
"""


# The findall() function returns a list containing all matches. 
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"""
The list contains the matches in the order they are found. 
If no matches are found, an empty list is returned. 
"""

x = re.findall("Portugal", txt)
print(x)


"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match. 
If there is more than one match, onyl the first occurance of the Match will be returned: 
"""

# Search dor the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned:
x = re.search("Portugal", txt) 
print(x)


# The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# We can control the number of occurances by specifying the maxsplit parameter:
# Split the string only at the first occurance:
x = re.split("\s", txt, 1)
print(x)


# The sub() function replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# We can countrol the number of replacements by specifying the count parameter:
# Replace the first 2 occurances:
x = re.sub("\s", "9", txt, 2)
print(x)


"""
    Match Object
A Match Object is an object containing information about the search and the result. 
If there is no match, the value None will be returned, instead of the Match Object. 
"""
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)


"""
The Match object has properties and methods used to retrieve information about the search, and the result:
.span() returns a tuple containing the start-, and end positions of the match. 
.string() returns the string passed into the function 
.group() returns the part of the string where there was a match 
"""

"""
Print the position (start- and end- position) of the first matach occurance. 
The regular expression looks for any words that starts with an upper case "S":
""" 
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(txt.index("S"))


# Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w", txt)
print(x.string)


"""
Print the part of the start where there was a match. 
The regular expression looks for any workds that starts with an upper case "S":
"""
txt = "The rain in Spain"
x = re.search(r"\bS\w", txt)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object. 

