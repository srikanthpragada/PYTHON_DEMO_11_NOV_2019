# Update minsal for a given job

import sqlite3

# Connect to db
con = sqlite3.connect(r"e:\classroom\python\nov11\hr.db")
cur = con.cursor()

id = input("Enter job id : ")
minsal = input("Enter min salary : ")

cur.execute("update jobs set minsal = ? where id = ?",
            (minsal,id))
if cur.rowcount == 1:
    con.commit()
    print("Job has been updated successfully!")
else:
    print("Sorry! Invalid job id!")

con.close()