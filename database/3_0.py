
"""
Executing Multiple SQL Statements
    If we want to run more than one SQL statement at a time we can use the Cursor.executescript() method.
    This method takes a string containing one or more SQL statements separated by semicolons and executes them all at once.
"""
import sqlite3

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
        CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );
        INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            42
        );"""
    )

"""
    We can also use the Cursor.executemany() method to insert multiple rows of data into a table at once.
    This method takes two arguments: the SQL statement to execute and a list of tuples containing the data to insert.
"""
people_values = (
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
    ("Ron", "Obvious", 42),
)

# We can then insert all of these people at once in a single line of code:
cursor.executemany("INSERT INTO People VALUES(?, ?, ?);", people_values)

"""
    Here, the question marks in the SQL statement are placeholders for the data in the people_values tuple.
    This is called parameter substitution and is a way to protect against SQL injection attacks.
    We may notice some similarities between this and the string formatting. 
"""



