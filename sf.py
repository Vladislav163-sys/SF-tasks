import json
from collections import defaultdict
from datetime import datetime

# Считываем данные из файла
with open("orders_july_2023.json", "r+") as my_file:
    orders = json.load(my_file)

# Переменные для хранения нужной информации
max_price = 0
max_order_number = ''
max_quantity = 0
max_quantity_order_number = ''
orders_by_date = defaultdict(int)
orders_by_user = defaultdict(int)
total_price = 0
total_quantity = 0

# Цикл по заказам
for order_num, order_data in orders.items():
    price = order_data['price']
    quantity = order_data['quantity']
    date = order_data['date']
    user_id = order_data['user_id']

    # Находим номер самого дорогого заказа
    if price > max_price:
        max_price = price
        max_order_number = order_num

    # Находим номер заказа с самым большим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order_number = order_num

    # Считаем заказы по дням
    orders_by_date[date] += 1

    # Считаем количество заказов от пользователя
    orders_by_user[user_id] += 1

    # Суммируем общую стоимость и количество товаров
    total_price += price
    total_quantity += quantity

# Найдем день с максимальным числом заказов
max_orders_date = max(orders_by_date, key=orders_by_date.get)
max_orders_count = orders_by_date[max_orders_date]

# Найдем пользователя с самым большим количеством заказов
most_orders_user_id = max(orders_by_user, key=orders_by_user.get)
most_orders_count = orders_by_user[most_orders_user_id]

# Найдем пользователя с самой большой суммарной стоимостью заказов
total_value_by_user = defaultdict(float)

for order_num, order_data in orders.items():
    user_id = order_data['user_id']
    total_value_by_user[user_id] += order_data['price']

richest_user_id = max(total_value_by_user, key=total_value_by_user.get)

# Рассчитаем среднюю стоимость заказа и среднюю стоимость товаров
average_order_price = total_price / len(orders)
average_price_per_item = total_price / total_quantity if total_quantity else 0

# Итог
print(f'Номер самого дорогого заказа: {max_order_number}, стоимость: {max_price}')
print(f'Номер заказа с самым большим количеством товаров: {max_quantity_order_number}, количество: {max_quantity}')
print(f'День с наибольшим количеством заказов: {max_orders_date}, количество: {max_orders_count}')
print(f'Пользователь с самым большим количеством заказов: {most_orders_user_id}, количество заказов: {most_orders_count}')
print(f'Пользователь с самой большой суммарной стоимостью заказов: {richest_user_id}, сумма: {total_value_by_user[richest_user_id]}')
print(f'Средняя стоимость заказа: {average_order_price}')
print(f'Средняя стоимость товара: {average_price_per_item}')