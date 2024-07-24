import sqlite3

conn = sqlite3.connect('SushiRestaurantDB.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY NOT NULL,
    telegram_id INTEGER NOT NULL,
    name TEXT,
    phone_number TEXT,
    address TEXT,
    registration_date TEXT DEFAULT (datetime('now'))
)
''')

conn.commit()
conn.close()