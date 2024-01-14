#!/usr/bin/python3
"""
script that takes in an argument
and displays all values in the states table
script should take 4 arguments
(no argument validation needed)
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = BINARY\
            '{}' ORDER BY 1".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
