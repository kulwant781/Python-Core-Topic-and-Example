import mysql.connector  as mysql
  
#Create the connection object   
myconn = mysql.connect(host = "localhost", user = "root",passwd = "")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #creating a new database  
    cur.execute("create database pythondb2")  
  
    #getting the list of all the databases which will now include the new database PythonDB  
    dbs = cur.execute("show databases")  
      
except:  
    myconn.rollback()  
  
for x in cur:  
        print(x)  
          
myconn.close()  