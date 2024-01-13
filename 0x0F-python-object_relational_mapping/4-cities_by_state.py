#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
script should take 3 arguments: username, password and database name
Results must be sorted in ascending order by cities.id
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
            FROM cities c\
            JOIN states s ON c.state_id = s.id\
            ORDER BY c.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
