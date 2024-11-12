import sqlite3
from werkzeug.security import generate_password_hash

def signup_user(username, email, password):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Generate hashed password
        password_hash = generate_password_hash(password)
        
        # Insert new user into the users table
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))

        conn.commit()
        conn.close()
        return True

    except sqlite3.IntegrityError:
        # This typically happens if the username or email is already taken
        conn.close()
        return False
