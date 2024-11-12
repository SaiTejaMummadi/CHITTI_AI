import sqlite3
from werkzeug.security import check_password_hash

def authenticate_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Fetch user by username
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user_record = cursor.fetchone()
    
    conn.close()

    # Verify password
    if user_record and check_password_hash(user_record[0], password):
        return True

    return False
