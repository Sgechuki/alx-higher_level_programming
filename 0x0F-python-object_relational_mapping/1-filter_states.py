#!/usr/bin/python3
"""
 lists all states with a name starting with N
 script should take 3 arguments: username, password and database name
 (no argument validation needed)
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
            'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
