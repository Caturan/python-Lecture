import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
print(cursor.execute("SELECT * FROM People;"))
print(cursor.fetchone())

"""
    Same script in 2_0.py but written using a with statement to manage the database connection. 

    Notice that not only is there no connection.close(), we also don't have to type connection.commit(). 
    That's because any changes made to the database are automatically committed when the with block is done exxecuting. 
    This is another advantage to using a with statement to manage our database connection. 
"""

