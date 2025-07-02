import mysql.connector

def paginate_users(page_size, offset):
    """
    Helper function that fetches a single page of users from user_data table,
    starting at the given offset.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc.123",  
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def lazy_paginate(page_size):
    """
    Generator that lazily loads paginated data from user_data using offset.
    Only uses one loop.
    """
    offset = 0
    while True:  # Only loop used
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
