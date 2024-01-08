import sqlite3

chunk_size = 25000  # Number of characters in each chunk
overlap_size = 2000  # Number of characters to overlap

conn = sqlite3.connect('C:/Users/bruker/Desktop/DBParser/html_files.db')
cursor = conn.cursor()
cursor.execute("SELECT id, category_id, domain, html FROM html_files")
rows = cursor.fetchall()

for row in rows:
    original_id, category_id, domain, html_content = row
    chunk_number = 0

    for i in range(0, len(html_content), chunk_size - overlap_size):
        chunk = html_content[i:i + chunk_size]
        chunk_number += 1
        # Process and insert the chunk into the database as before
        # Insert the chunk into the new table
        print("Inserting chunk number", chunk_number, "for file", original_id)
        cursor.execute('''
            INSERT INTO chunked_html_files (original_id, category_id, domain, chunked_html, chunk_number)
            VALUES (?, ?, ?, ?, ?)
        ''', (original_id, category_id, domain, chunk, chunk_number))
        print("Chunk inserted")
        

conn.commit()
conn.close()
