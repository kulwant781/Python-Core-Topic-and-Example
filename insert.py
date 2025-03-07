from db import myconn

try:
    cur = myconn.cursor()
    # Use %s for all placeholders
    insert_query = "INSERT INTO employeep (name, id, salary, Dept_id, email) VALUES (%s, %s, %s, %s, %s)"
    # Define the values to be inserted
    insert_values = [
        ('kulwant', 931, 65000, 9393,'kulwant@gmail'), 
        ('abc', 10, 50000, 1, 'abc@gmail'), 
        ('xyz', 33, 3333, 342, 'xyz@gmail')
    ]
    # Execute the query with the values
    cur.executemany(insert_query, insert_values)
    myconn.commit()
    print("Multipel Data inserted successfully in Employee table")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection
    if myconn.is_connected():
        myconn.close()
        print("MySQL connection is closed.")
