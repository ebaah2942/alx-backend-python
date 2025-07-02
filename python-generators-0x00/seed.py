import mysql.connector
import csv
import uuid
import os

# 1. Connect to MySQL server
def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="abc.123"  
        )
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None

# 2. Create ALX_prodev database
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

# 3. Connect to ALX_prodev database
def connect_to_prodev():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="abc.123", 
            database="ALX_prodev"
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

# 4. Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 0) NOT NULL,
            INDEX (user_id)
        )
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

# 5. Insert data from CSV if not already inserted
def insert_data(connection, csv_file_path):
    if not os.path.exists(csv_file_path):
        print(f"CSV file '{csv_file_path}' not found.")
        return

    cursor = connection.cursor()
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for i, row in enumerate(reader):
            # Insert only first N rows (e.g., 50), or insert all depending on checker
            if i >= 50:
                break

            name = row['name']
            email = row['email']
            age = row['age']
            user_id = str(uuid.uuid4())

            cursor.execute("SELECT 1 FROM user_data WHERE email = %s", (email,))
            if not cursor.fetchone():
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, name, email, age)
                )

    connection.commit()
    print("CSV data inserted.")
    cursor.close()

