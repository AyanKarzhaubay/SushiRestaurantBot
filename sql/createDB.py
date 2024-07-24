import sqlite3

# Подключение к базе данных (если база данных не существует, она будет создана)
conn = sqlite3.connect('SushiRestaurantDB.db')