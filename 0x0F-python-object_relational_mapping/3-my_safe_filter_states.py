#!/usr/bin/python3
"""
This script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    name_pattern = "%" + argv[4].replace("%", "//%").replace("_", "\\_") + "%"
    cur.execute(query, (name_pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)
