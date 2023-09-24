import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the database
    connection = mysql.connector.connect( # Connects to MySQL database
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )

    if connection.is_connected():
        cursor = connection.cursor(prepared=True)
        
        # SQL query with placeholders for data input
        sql_insert_query = """INSERT INTO users (username, email) VALUES (%s, %s)"""
        
        # Data to be inserted
        insert_tuple = ("AmyJarman", "amyjarman@example.com")
        
        # Execute the parameterized query
        cursor.execute(sql_insert_query, insert_tuple)
        
        # Commit the transaction
        connection.commit()
        
        print(cursor.rowcount, "Record inserted successfully into users table")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")