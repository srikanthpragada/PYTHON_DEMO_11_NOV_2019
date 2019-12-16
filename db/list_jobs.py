
import sqlite3

# Connect to db
con = sqlite3.connect(r"e:\classroom\python\nov11\hr.db")
cur = con.cursor()
cur.execute("select * from jobs order by title")
for job in cur.fetchall():
    print(f"{job[1]:30} {job[3]}")

con.close()