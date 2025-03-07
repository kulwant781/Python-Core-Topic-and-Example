from db import myconn

cur = myconn.cursor()

cur.execute("DELETE FROM employeep WHERE id = 1")

print(cur.rowcount, "record(s) deleted")
myconn.commit()
