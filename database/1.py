 
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

connection = sqlite3.connect(":memory:")

print(type(connection))

cursor = connection.cursor()
print(type(cursor))

query = "SELECT datetime('now', 'localtime');"
print(cursor.execute(query))


print(cursor.fetchone())