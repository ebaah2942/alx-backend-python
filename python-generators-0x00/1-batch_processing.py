import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that fetches users from the database in batches.
    Yields one batch (list of rows) at a time.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc.123",
        database="ALX_prodev"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """
    Generator that filters and yields users over age 25 from each batch.
    """
    for batch in stream_users_in_batches(batch_size):  # 1st loop
        filtered = [user for user in batch if user[3] > 25]  # 2nd loop (list comprehension)
        for user in filtered:  # 3rd loop
            yield user
