
"""
    Create a new database with a table named Roster that has three fields: Name, Species and IQ. 
     The Name and Species columns should be text fields, and the IQ column should be an integer field. 
     Update the Species of Korben Dallas to be Human
     Display the names and IQs of everyone in the table classified as Human
"""

import sqlite3

values = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5),
)


with sqlite3.connect("exercise_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS Roaster;
        CREATE TABLE Roaster(
            Name TEXT,
            Species TEXT,
            IQ INT
        );"""
    )
    cursor.executemany("INSERT INTO Roaster VALUES(?,?,?);",values)

    cursor.execute("SELECT Name, IQ FROM Roaster WHERE Species = 'Human'") 
    for row in cursor.fetchall():
        print(row)

    print()

    cursor.execute(
        "UPDATE Roaster SET Species=? WHERE Name=? AND IQ=?;",
        ("Human", "Korben Dallas", 100),
    )

    cursor.execute("SELECT Name, IQ FROM Roaster WHERE Species = 'Human'") 
    for row in cursor.fetchall():
        print(row)