from db import myconn
  
cur = myconn.cursor()  
try:
    #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
    dbs = cur.execute("create table Employeep(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")  
except:  
    cur.rollback()  
    #print(cur)
cur.close()  