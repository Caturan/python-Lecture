 
"""
    A database is a structured system for storing data. It could be made up of several CSV files organized into directories, or something more elaborate. 
    Python comes with a light-weight SQL database called SQLite that is perfect for learning how to work with databases. 
"""

"""
    There are numeraous SQL databases, and some are better suited to particular purposes than others. 
    One of the simplest, most lightweight SQL databases SQLite, which runs directly on our machine and comes bundled with Python automatically. 
"""

import sqlite3 
connection = sqlite3.connect("test_database.db")
"""
    The sqlite3.connect() function is used to connect to, or create, a database. 
    When we execute, Python searches for an existing database called "test_database.db". 
    If no database with that name is found, a new one is created in the current working directory. 
    To create a database in a different directory, we must specify the full path in the argument to .connect(). 
"""

print(type(connection))

cursor = connection.cursor()
print(type(cursor))
"""
    To store and retrieve data, we need a Cursor object, which can be obtained with the Connection.cursor() function. 
    The sqlite3.Cursor object is our gateway to interacting with the database. 
    Using a Cursor, we can create database tables, execute SQL statements, and fetch query results.  
"""

query = "SELECT datetime('now', 'localtime');"
print(cursor.execute(query))
"""
    Note that .execute() returns a Cursor object, but we didn't assign this to a new variable. 
    That's because .execute() alters the state of cursor and also returns the cursor object itself. 
     This might look kind of strange, but it allows us to chain multiple Cursor methods together on a single line. 
"""

"""
    To get the guery results, use the cursor.fetchone() method. .fetchone() returns a tuple containig the first row of results:
"""
print(cursor.fetchone())
"""
    Since .fetchcone() returns a tuple, we need to unpack the tuple elements to get the string containing the date and time information. 
"""
time = cursor.execute(query).fetchone()[0]
print(time)

"""
    Finally, to close the database connection, use the connection.close() method:
"""
connection.close()



#Using with to Manage our Database Connection:
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    time = cursor.execute(query).fetchone()[0]
print(time)

"""
    In this example, the connection variable is assigned to the Connection object returned by sqlite3.connect() in the with statement. 
    The code in the with block gets a new Cursor object using connection.cursor() and then gets the current time with the Cursor object's .execute() and .fetchone() methods. 

    Managing our database connections in a with statement has many advantages. 
    The resulting code is oftn cleaner and shorter than code written without a with statement. 
"""



