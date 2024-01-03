import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()

# Cursor = In SQLite and many other database systems, a cursor is a mechanism for traversing and processing the results of a query. 

cursor.execute(
    """CREATE TABLE People(
        FirstName TEXT,
        LastName TEXT,
        Age INT
    );"""
)

cursor.execute(
    """INSERT INTO People VALUES(
        'Ron',
        'Obvious',
        42
    );"""
)

connection.commit()
connection.close()


"""
    First, we get a Connection object with sqlite3.connect() and as sign it to the connection variable. 
    A Cursor object is created with connection.cursor() and used to execute the two SQL statements for creating the People table and inserting some data. 

    The SQL statement in both .execute() methods have been written using triple quote strings so that we can format the SQL nicely. 
    SQL ignores whitespace, so we can get away with this here and improve the readability of the Python code. 

    Finally, connection.commit() is used to save the data to the database. Commit is database jargon for saving data. 
    If we do not run connection.commit(), no People table is created.  
"""

cursor.execute("DROP TABLE People;")
connection.commit()
connection.close()


