import sqlite3

conn = sqlite3.connect('SushiRestaurantDB.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS delivery_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    client_id INTEGER NOT NULL,
    delivery_address TEXT NOT NULL,
    order_date TEXT DEFAULT (datetime('now')),
    total_price REAL NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
)
''')

conn.commit()
conn.close()