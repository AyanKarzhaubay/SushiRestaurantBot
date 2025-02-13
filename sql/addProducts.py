import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('SushiRestaurantDB.db')
cursor = conn.cursor()

# Данные товаров
products = [
    ('Роллы', 'Филадельфия', '10 шт', 1890),
    ('Роллы', 'Филадельфия гриль', '10 шт', 1990),
    ('Роллы', 'Филадельфия с угрём', '10 шт', 2490),
    ('Роллы', 'Филадельфия люкс', '10 шт', 2490),
    ('Роллы', 'Филадельфия лайт', '10 шт', 1890),
    ('Роллы', 'Калифорния в кунжуте', '10 шт', 1990),
    ('Роллы', 'Калифорния с лососем', '10 шт', 1990),
    ('Роллы', 'Дайси', '10 шт', 1890),
    ('Роллы', 'Сяке Маки', '10 шт', 1990),
    ('Роллы', 'Сенкай', '10 шт', 2090),
    ('Роллы', 'Аляска', '10 шт', 2090),
    ('Роллы', 'Бонито', '10 шт', 2290),
    ('Роллы', 'Канада', '10 шт', 2290),
    ('Роллы', 'Масаго Кунсей', '10 шт', 2290),
    ('Роллы', 'Токио', '10 шт', 2290),
    ('Роллы', 'Сендвич ролл', '10 шт', 2290),
    ('Роллы', 'Торнадо', '10 шт', 2290),
    ('Роллы', 'Сяке Лосось', '10 шт', 2090),
    ('Роллы', 'Урамаки', '10 шт', 2090),
    ('Роллы', 'Калифорния с угрём', '10 шт', 1990),
    ('Роллы', 'Гавайский', '10 шт', 2090),
    ('Роллы', 'Пряный', '10 шт', 1990),
    ('Роллы', 'Эби темпура', '10 шт', 1990),
    ('Роллы', 'Инь Янь', '10 шт', 1990),
    ('Темпура', 'Кани Темпура', '10 шт', 1990),
    ('Темпура', 'Сяке Темпура', '10 шт', 1990),
    ('Темпура', 'Сяке Кани Темпура', '10 шт', 2090),
    ('Темпура', 'Терияки темпура', '10 шт', 2090),
    ('Темпура', 'Америка', '10 шт', 1990),
    ('Хосомаки', 'Каппа Маки', '10 шт', 990),
    ('Хосомаки', 'Сяке Маки', '10 шт', 1490),
    ('Хосомаки', 'Эби Маки', '10 шт', 1490),
    ('Хосомаки', 'Унаги Маки', '10 шт', 1490),
    ('Хосомаки', 'Филадельфия Маки', '10 шт', 1490),
    ('Хосомаки', 'Планетарный ролл', '10 шт', 1490),
    ('Хосомаки', 'Инь Янь', '10 шт', 1990),
    ('Запечённые роллы', 'Сяке Маки запечённая', '10 шт', 1790),
    ('Запечённые роллы', 'Зэби Маки запечённая', '10 шт', 1790),
    ('Запечённые роллы', 'Сяке Темпура запечённая', '10 шт', 1890),
    ('Запечённые роллы', 'Зэби Темпура запечённая', '10 шт', 1890),
    ('Запечённые роллы', 'Унаги запечённая', '10 шт', 1890),
    ('Запечённые роллы', 'Кани Темпура запечённая', '10 шт', 1790),
    ('Запечённые роллы', 'Цезарь запечённый', '10 шт', 1890),
    ('Запечённые роллы', 'Филадельфия запечённая', '10 шт', 2490),
    ('Запечённые роллы', 'Калифорния с крабом запечённая', '10 шт', 1990),
    ('Запечённые роллы', 'Калифорния с лососем запечённая', '10 шт', 1990),
    ('Гунканы', 'С курицей', '1 шт', 600),
    ('Гунканы', 'С лососем', '1 шт', 600),
    ('Гунканы', 'С крабом', '1 шт', 600),
    ('Гунканы', 'С креветкой', '1 шт', 600),
    ('Нигири', 'С лососем', '1 шт', 600),
    ('Нигири', 'С креветкой', '1 шт', 600)
]

# Вставка данных в таблицу
cursor.executemany('''
    INSERT INTO products (category, name, description, price)
    VALUES (?, ?, ?, ?)
''', products)

conn.commit()
conn.close()