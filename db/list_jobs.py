
import sqlite3

# Connect to db
con = sqlite3.connect(r"e:\classroom\python\nov11\hr.db")
cur = con.cursor()
cur.execute("select * from jobs")

con.close()