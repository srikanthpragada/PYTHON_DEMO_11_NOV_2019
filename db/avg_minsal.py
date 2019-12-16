
import sqlite3

# Connect to db
con = sqlite3.connect(r"e:\classroom\python\nov11\hr.db")
cur = con.cursor()
cur.execute("select avg(minsal),count(id) from jobs")
avg_minsal,count_jobs = cur.fetchone()

print("No. of jobs        : ", count_jobs)
print("Average min salary : ", avg_minsal)

con.close()