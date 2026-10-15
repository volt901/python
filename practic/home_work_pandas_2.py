import pandas as pd
import numpy as np

df = pd.read_csv('sales_data.csv')

if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

print(df.head())
print(df.shape)

print("1.1. Поставь date индексом, сохрани в переменную df_date. Выведи первые 3 строки.")
df_date = df.set_index('date')
print(df_date.head(3))

print("1.2. Что покажет df_date.index? Какой это тип?")
print(df_date.index)

print("1.3. Отсортируй df_date по индексу (sort_index) и выведи записи за март 2022 (срез '2022-03-01':'2022-03-31').")
print(df_date.sort_index()['2022-03-01':'2022-03-31'])

print("1.4. Верни индекс обратно в столбцы через reset_index(). Убедись, что date снова среди столбцов.")
df_date=df_date.reset_index()
print(df_date.head(3))

print("1.5. Снова поставь date индексом, но теперь сбрось его через reset_index(drop=True). Проверь, что date не стал столбцом.")
df_date=df_date.set_index('date')
print(df_date.head(3))
df_date=df_date.reset_index(drop=True)
print(df_date.head(3))


print("1.6. Сгруппируй df по category, посчитай сумму revenue, сбрось индекс. Убедись, что category — обычный столбец.")
print(df_date.groupby(["category"])["revenue"].sum())


print("1.7. Сгруппируй df по ['category', 'month'], посчитай сумму revenue, сбрось индекс. Сколько строк получилось?")
print(df_date.groupby(["category", 'month'])["revenue"].sum())

print("1.8. Поставь product индексом. Сколько уникальных меток в индексе?")
print(df_date.set_index('product'))


print("1.9. Сделай set_index(['category', 'product']). Выведи первую строку.")
print(df_date.set_index(['category', 'product']).head(1))

print("1.10. Объясни в комментарии: чем sort_index() отличается от sort_values('col')?")
'''
sort_index() - сортировка по индексу
sort_values('col') - сортировка по столбцу 
'''

