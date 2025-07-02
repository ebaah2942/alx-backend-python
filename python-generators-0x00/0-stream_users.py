import mysql.connector

def stream_users():
    """Generator that yields rows from the user_data table one by one."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc.123",  
        database="ALX_prodev"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row

    cursor.close()
    connection.close()
