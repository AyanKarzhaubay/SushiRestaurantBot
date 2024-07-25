import sqlite3

def add_order(user_id, order_details):
    conn = sqlite3.connect('sushi_bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (user_id, order_details) VALUES (?, ?)', (user_id, order_details))
    conn.commit()
    conn.close()

def get_orders(user_id):
    conn = sqlite3.connect('sushi_bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
    orders = cursor.fetchall()
    conn.close()
    return orders
