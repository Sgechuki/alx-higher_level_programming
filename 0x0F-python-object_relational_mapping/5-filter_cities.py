#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
should take 4 arguments:username, password, database name
and state name (SQL injection free!)
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT c.name\
            FROM cities c\
            JOIN states s ON c.state_id = s.id\
            WHERE s.name = %s\
            ORDER BY c.id"
    cur.execute(query, [argv[4]])
    rows = cur.fetchall()
    for index, row in enumerate(rows):
        if index < (len(rows) - 1):
            print(row[0], end=", ")
        else:
            print(row[0])
    cur.close()
    db.close()
