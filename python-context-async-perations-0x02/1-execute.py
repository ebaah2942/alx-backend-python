import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect("users.db")  # Ensure users.db exists
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# Usage
with DatabaseConnection() as cursor:
    cursor.execute("SELECT * FROM users WHERE age > ?", (25,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)



