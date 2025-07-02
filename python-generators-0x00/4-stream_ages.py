import mysql.connector

def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc.123",
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:  # loop 1
        yield age

    cursor.close()
    connection.close()

def compute_average_age():
    """
    Computes the average age using the stream_user_ages generator.
    Does not load all data into memory.
    """
    total = 0
    count = 0

    for age in stream_user_ages():  # loop 2
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")

# Run it
compute_average_age()
