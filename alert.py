from db import myconn

cur = myconn.cursor()

try:
    ch = cur.execute("ALTER table Employeep add column slrys varchar(255) AFTER Dept_id")

except:  
    cur.rollback()  
    #print(cur)
    myconn.commit()      
cur.close()  
  
