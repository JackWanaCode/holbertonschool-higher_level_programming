#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

i = 0
for el in sys.argv:
    if i == 1:
        u = el
    if i == 2:
        pd = el
    if i == 3:
        d = el
    i += 1
db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=pd, db=d)
cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print("{}".format(row))
