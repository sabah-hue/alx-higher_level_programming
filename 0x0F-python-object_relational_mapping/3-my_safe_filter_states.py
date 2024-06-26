#!/usr/bin/python3
"""script that lists all states with a name entered as argv"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE \
    name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
