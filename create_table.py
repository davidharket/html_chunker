import sqlite3

# Connect to your database
conn = sqlite3.connect('C:/Users/bruker/Desktop/DBParser/html_files.db')
cursor = conn.cursor()

# Create a new table for the chunked HTML
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chunked_html_files (
        id INTEGER PRIMARY KEY,
        original_id INTEGER,
        category_id INTEGER,
        domain TEXT,
        chunked_html TEXT,
        chunk_number INTEGER,
        FOREIGN KEY (original_id) REFERENCES html_files (id)
    )
''')

conn.commit()
conn.close()
