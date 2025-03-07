from db import myconn

    # Create a cursor object
try:
    cur = myconn.cursor()
    
    # Correct SQL UPDATE query
    cur.execute("UPDATE employeep SET name = 'wordpress' WHERE name = 'ajay'")
    
    # Commit the changes
    myconn.commit()
    
    # Print the number of rows updated
    print(cur.rowcount, "record(s) updated")
except Exception as e:
    print(f"Error: {e}")


