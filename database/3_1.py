
"""
Avoid Securitty Issues with Parameterized Statements
    For security reasons, especially when accepting user input, it is important to use parameterized statements.
   This is because parameterized statements are immune to SQL injection attacks.
   And even if we aren't dealing with malicious user, it can happen entirely by accident.
"""

import sqlite3

# Get person data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Execute insert statement for supplied person data
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    line = "INSERT INTO People VALUES(?, ?, ?);"
    cursor.execute(line, (firstName, lastName, age))   

"""
    The following scripty does the same thins as the script above, 
    but uses a parametrized statement to inser the user input into the database: 
"""

import sqlite3

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
data = (firstName, lastName, age)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES(?, ?, ?);", data)

"""
    We can update the content of a row using a parametrized SQL UPDATE statement.
    
    For instance, if we want to change the Age associated with someone already in our table, we could use the following code:
"""
cursor.execute(
    "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",
    (45, "Luigi", "Vercotti"),
)


