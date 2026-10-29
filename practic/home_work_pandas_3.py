import pandas as pd
import numpy as np

# 1. Основная таблица продаж
df = pd.read_csv('sales_data.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

print(df)
# 2. Справочник товаров
products_info = pd.DataFrame({
    'product':  ['Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Speaker',
                 'T-Shirt', 'Jeans', 'Coat', 'Hoodie', 'Sneakers',
                 'Backpack', 'Watch', 'Smartwatch', 'Wallet'],
    'brand':    ['Samsung', 'Apple', 'Samsung', 'Sony', 'JBL',
                 'Nike', 'Levi\'s', 'Zara', 'Adidas', 'Nike',
                 'Nike', 'Casio', 'Apple', 'Gucci'],
    'supplier': ['Asia', 'USA', 'Asia', 'Japan', 'USA',
                 'Europe', 'Europe', 'Europe', 'Europe', 'Asia',
                 'Asia', 'Japan', 'USA', 'Europe'],
    'warranty': [24, 24, 12, 12, 6,
                 0, 0, 0, 0, 0,
                 0, 12, 12, 0],
})

'''
Часть 1. Метод merge
1.1. Сделай левое слияние (left) таблиц df и products_info по столбцу product. 
Сохрани результат в переменную merged. Выведи первые 3 строки.
'''
merged=df.merge(products_info,on='product',how="left")
print(merged)

'''
1.2. Сколько уникальных брендов (brand) появилось в таблице merged?
'''

print(merged["brand"].value_counts())
print(merged["brand"].nunique())
print(merged.groupby(["brand"]).ngroups)

'''
1.3. Сделай внутреннее слияние (inner) таблиц df и products_info. 
Сколько строк получилось? Сравни это число с len(df). Почему они могут отличаться?
'''
merged = pd.merge(df, products_info, on='product', how='inner')
print(merged)
'''
1.4. Сделай внешнее слияние (outer) с параметром indicator=True. 
Выведи те строки, где _merge равно left_only. Что это за товары и почему они не нашли пару в справочнике?
'''
merged = pd.merge(df, products_info, on='product', how='outer',indicator=True)
print(merged)
left_only = merged[merged['_merge'] == 'left_only']
print(left_only)

'''
1.5. Представь, что в products_info случайно продублировали строку с брендом Apple (товар Laptop). 
Напиши код, который:

Создает такую ошибочную таблицу bad_products.
'''
bad_products = pd.DataFrame({
    'product':  ['Smartphone', 'Laptop', 'Laptop', 'Tablet', 'Headphones', 'Speaker',
                 'T-Shirt', 'Jeans', 'Coat', 'Hoodie', 'Sneakers',
                 'Backpack', 'Watch', 'Smartwatch', 'Wallet'],
    'brand':    ['Samsung', 'Apple','Apple', 'Samsung', 'Sony', 'JBL',
                 'Nike', 'Levi\'s', 'Zara', 'Adidas', 'Nike',
                 'Nike', 'Casio', 'Apple', 'Gucci'],
    'supplier': ['Asia', 'USA', 'USA', 'Asia', 'Japan', 'USA',
                 'Europe', 'Europe', 'Europe', 'Europe', 'Asia',
                 'Asia', 'Japan', 'USA', 'Europe'],
    'warranty': [24, 24, 24, 12, 12, 6,
                 0, 0, 0, 0, 0,
                 0, 12, 12, 0],
})

'''
Делает merge с df.

Проверяет, насколько выросло количество строк (эффект картезианского произведения).
'''

merged=df.merge(bad_products,on='product')
print(merged)

#  не понимаю, не получается эффект картезианского произведения

'''
1.6. Используй метод join() для объединения df и products_info по индексу product.
 (Подсказка: предварительно сделай set_index('product') для обеих таблиц).
'''

df_index = df.set_index('product')
products_index = products_info.set_index('product')

result = df_index.join(products_index, how='outer', rsuffix='_info')
print(result)

'''
Часть 2. Метод concat
2.1. Раздели df на две части: jan (январь, month == 1) и feb (февраль, month == 2).
'''
df_j=df[df["month"]==1]
# прилось поменяь на март, так как df были отсортированы не чего не видно было на упражнении 2.3
df_m=df[df["month"]==3]
print(df_j)
print(df_m)
df_jm= pd.concat([df_j,df_m],ignore_index=True)
print(df_jm)


'''
2.2. Склей их обратно с помощью pd.concat. Обязательно используй ignore_index=True. 
Проверь, что len(combined) == len(jan) + len(feb).
'''
print (len(df_jm) == len(df_j) + len(df_m))
'''
2.3. Что произойдёт с индексами, если не указывать ignore_index=True? Выведи combined.index в обоих случаях 
(с параметром и без), чтобы увидеть разницу.
'''
print(df_jm.index)
df_jm= pd.concat([df_j,df_m])
print(df_jm.index)
'''
2.4. Создай два датафрейма:
Склей их с помощью pd.concat(..., axis=1). Что появилось на месте индекса 'a' в столбце B и почему?
'''
t1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
t2 = pd.DataFrame({'B': [10, 20]}, index=['b', 'c'])
combaint= pd.concat([t1,t2])
print(combaint)
