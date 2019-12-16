# Delete job by the given id

import sqlite3

try:
    # Connect to db
    con = sqlite3.connect(r"e:\classroom\python\nov11\hr.db")
    cur = con.cursor()

    id = input("Enter job id : ")
    try:
        cur.execute("delete from jobs where id = ?", (id,))
        if cur.rowcount == 1:
            con.commit()
            print("Job has been deleted successfully!")
        else:
            print("Sorry! Invalid job id!")
    except Exception as ex:
        print("Sorry! Error -> ", ex)

except:
    print("Sorry! Could not connect to database")
else:
    print("Closing connection!")
    con.close()
