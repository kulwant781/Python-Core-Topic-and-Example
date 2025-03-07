from db import myconn

try:
    # Create a cursor object
    cur = myconn.cursor()
    
    # Execute the SELECT query
    cur.execute("SELECT * FROM employeep")
    
    # Fetch all rows
    result = cur.fetchall()
    
    # Print table headers
    print(f"{'Name':<25}{'ID':<10}{'Salary':<10}{'Dept_id':<10}{'Email':<20}")
    print("-" * 75)
    
    # Iterate and print each row with formatting
    for row in result:
        print(f"{row[0]:<25}{row[1]:<10}{row[2]:<10}{row[3]:<10}{row[4]:<20}")
        print("-" * 75)
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection
    if myconn.is_connected():
        myconn.close()
        print("MySQL connection is closed.")
