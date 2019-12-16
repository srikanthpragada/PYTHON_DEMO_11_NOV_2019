
import sqlite3

# Connect to db
con = sqlite3.connect(r"e:\classroom\python\nov11\hr.db")
cur = con.cursor()

title = input("Enter job title : ")
location = input("Enter location : ")
minsal = input("Enter min salary : ")

cur.execute("insert into jobs(title,location,minsal) values(?,?,?)",
            (title,location,minsal))
con.commit()
print("Job has been added successfully!")
con.close()