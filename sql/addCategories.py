import sqlite3

conn = sqlite3.connect('SushiRestaurantDB.db')
cursor = conn.cursor()

categories = [
    'Сет',
    'Пицца',
    'Ролл',
    'Запеченный ролл',
    'Темпура',
    'Нигири',
    'Сашими',
    'Гункан',
    'Темари',
    'Хосомаки',
    'Крылышки',
    'Напиток',
    'Снэк'
]

# Вставка категорий
cursor.executemany('''
INSERT INTO categories (name)
VALUES (?)
''', [(category,) for category in categories])

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Категории успешно добавлены.")