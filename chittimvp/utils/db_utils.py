import sqlite3
from werkzeug.security import generate_password_hash

# Initialize the database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            text_content TEXT,
            image_path TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    conn.commit()
    conn.close()

# Add user
def add_user(username, email, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    password_hash = generate_password_hash(password)
    
    cursor.execute("""
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?)
    """, (username, email, password_hash))
    
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id

# Add text content
def add_text_content(user_id, title, text_content):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO content (user_id, title, text_content)
        VALUES (?, ?, ?)
    """, (user_id, title, text_content))
    
    conn.commit()
    conn.close()
