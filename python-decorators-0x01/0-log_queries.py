


import sqlite3
import functools

#### decorator to lof SQL queries

def log_queries():
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Executing: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Result: {result}")
            return result
        return wrapper
    return decorator

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")