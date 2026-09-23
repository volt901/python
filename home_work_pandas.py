import pandas as pd

data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'date': [
        '2024-01-05', '2024-01-07', '2024-01-08', '2024-01-12',
        '2024-01-15', '2024-02-01', '2024-02-03', '2024-02-10',
        '2024-03-01', '2024-03-05', '2024-03-07', '2024-03-15',
    ],
    'customer': ['Аня', 'Борис', 'Аня', 'Вика', 'Борис', 'Аня',
                 'Вика', 'Глеб', 'Борис', 'Аня', 'Глеб', 'Вика'],
    'city':     ['Москва', 'СПб', 'Москва', 'Казань', 'СПб', 'Москва',
                 'Казань', 'Москва', 'СПб', 'Москва', 'Москва', 'Казань'],
    'product':  ['Ноутбук', 'Мышь', 'Клавиатура', 'Ноутбук', 'Монитор',
                 'Мышь', 'Ноутбук', 'Клавиатура', 'Монитор', 'Мышь',
                 'Монитор', 'Ноутбук'],
    'quantity': [1, 2, 1, 1, 1, 3, 1, 2, 1, 4, 2, 1],
    'price':    [70000, 1500, 3000, 65000, 20000, 1500,
                 72000, 3000, 21000, 1500, 21000, 70000],
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['total'] = df['quantity'] * df['price']
df['month'] = df['date'].dt.month

print("1.1. Сколько строк и столбцов в df?")
print(f"строк: {df.shape[0]}, колонок: {df.shape[1]}")

print("1.2. Какие типы у столбцов date, total, customer?")
print(f"типы date: {df.dtypes["date"]}, total: {df.dtypes["total"]}, customer: {df.dtypes["customer"]}")

print("1.3. Сколько уникальных товаров в датасете?")
value_counts_df = df["product"].value_counts()
flag = False
for value,counts in value_counts_df.items():
    if counts == 1:
        print(value)
        flag = True

if not flag:
    print("Уникального товара нет")

print("1.4. Какая максимальная цена среди всех заказов?")
print(f"максимальная цена - {df['price'].max()}")

print("1.5. Сколько всего денег было заработано (total по всем заказам)?")
print(f"сумма - {df['total'].sum()}")

print("1.6. Выведи первые 3 строки датасета")
print(df.head(3))

print("1.7. Выведи последние 2 строки датасета.")
print(df.tail(2))

print("2.1. Выведи только столбец customer.")
print(df["customer"])

print("2.2. Выведи таблицу из столбцов order_id, customer, total.")
print(df[["order_id","customer","total"]])

print("2.3. Сколько всего денег во всём датасете?")
print(f"сумма - {df['total'].sum()}")

print("2.4. Какая максимальная цена (price) в датасете?")
print(df["price"].max())

print("2.5. Какая средняя quantity в датасете?")
print(df["quantity"].mean())