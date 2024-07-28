import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
}

# Database name
database_name = 'alx_book_store'

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create database if it does not exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"Database '{database_name}' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(f"Database '{database_name}' does not exist.")
    else:
        print(err)
finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()