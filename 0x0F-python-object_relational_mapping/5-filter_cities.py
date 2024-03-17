#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ run in CMD not in imported """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities\
             left join states ON cities.state_id = states.id\
             WHERE states.name = %s"
    cur.execute(query, [argv[4]])
    query_rows = cur.fetchall()
    arr = []
    for row in query_rows:
        arr.append(row[0])
    print(", ".join(arr))
    cur.close()
    conn.close()
