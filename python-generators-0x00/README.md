📌 Project: seed.py — MySQL Seeding Script
This project automates the setup of a MySQL database named ALX_prodev, creates a user_data table, and populates it with sample data from a provided CSV file (user_data.csv).

It follows a predefined interface with specific function prototypes to support automated checking.

✅ Features
Connects to a MySQL server

Creates a database if it does not exist

Connects to that database

Creates a user_data table with:

user_id (UUID, Primary Key, Indexed)

name (VARCHAR, NOT NULL)

email (VARCHAR, NOT NULL)

age (DECIMAL, NOT NULL)

Loads and inserts data from user_data.csv if not already present

🧪 Sample Execution (0-main.py)

seed = __import__('seed')

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print(f"connection successful")

    connection = seed.connect_to_prodev()

    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')
        cursor = connection.cursor()
        cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
        result = cursor.fetchone()
        if result:
            print(f"Database ALX_prodev is present ")
        cursor.execute(f"SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)
        cursor.close()

def connect_db() -> connection
def create_database(connection) -> None
def connect_to_prodev() -> connection
def create_table(connection) -> None
def insert_data(connection, csv_file_path) -> None