import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect('movies.db')

# Create table
conn.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_title TEXT NOT NULL,
    reviewer_name TEXT NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT
);
''')

conn.close()
print("Database initialized.")
