import os

# Save image to disk and store file path in database
def save_image(user_id, title, image_file):
    user_dir = f"images/user_{user_id}"
    os.makedirs(user_dir, exist_ok=True)
    
    filename = f"{title.replace(' ', '_')}_{image_file.name}"
    file_path = os.path.join(user_dir, filename)
    
    with open(file_path, "wb") as f:
        f.write(image_file.getbuffer())
    
    # Connect to the database and store the file path
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO content (user_id, title, image_path)
        VALUES (?, ?, ?)
    """, (user_id, title, file_path))
    
    conn.commit()
    conn.close()
