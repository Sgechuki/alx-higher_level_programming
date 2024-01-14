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
    cities = []
    for city in cur.fetchall():
        cities.append(city[0])
    print(", ".join(cities))
    cur.close()
    db.close()
