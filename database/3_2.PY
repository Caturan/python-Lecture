
"""
Retrieving Data
    To fetch data from a database, we can use the .fetchone() and .fetchall() methods of the cursor methods.
    These are similar to the .readline() and .readlines() methods of files.
    The .fetchone() method returns the next row of data, or None if there are no more rows.
    The .fetchall() method returns a list of all remaining rows of data.
"""

import sqlite3

values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );"""
    )
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?);", values)

    cursor.execute("SELECT FirstName, LastName FROM People WHERE Age > 30;")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        print(row)

    cursor.execute("SELECT FirstName, LastName FROM People WHERE Age > 30;")
    for row in cursor.fetchall():
        print(row)

"""
    In the script above, we first drop the People table to destroy changes made in the previous examples in this section.
    Then we create a new People table and insert some data into it.
    We then run two SELECT statements to retrieve data from the table.
    The first uses a while loop to fetch each row of data one at a time.
    The second uses a for loop to fetch all of the remaining rows of data at once.
"""
