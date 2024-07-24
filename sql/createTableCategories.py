import sqlite3

conn = sqlite3.connect('SushiRestaurantDB.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL
)
''')

conn.commit()
conn.close()