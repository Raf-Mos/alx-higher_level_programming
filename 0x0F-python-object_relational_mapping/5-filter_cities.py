#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s ORDER BY cities.id ASC;", (argv[4],))
    query_rows = cur.fetchall()

    print(", ".join([row[1] for row in query_rows]))

    cur.close()
    conn.close()
