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

print("""Часть 2. rename, astype, assign
2.1. Переименуй product → item, revenue → income. Убедись, что исходный df не изменился (проверь df.columns.tolist()).
""")
df_date=df_date.rename(columns={'product': 'item', 'revenue': 'income'})
print(df_date.columns.tolist())
print(df.columns.tolist())



print("2.2. Создай маленький DataFrame:")
print("Переведи a в int, b в float. Выведи типы.")
nums = pd.DataFrame({
    'a': ['10', '20', '30'],
    'b': ['1.5', '2.5', '3.5'],
})
print(nums.dtypes)
nums["a"] = nums["a"].astype(int)
nums["b"] = nums["b"].astype(float)
print(nums.dtypes)

print(
"""
2.3. Через assign добавь к df три столбца:
revenue_check = price * quantity,
is_expensive = price > 300,
product_upper = product.upper().
"""
)
df_new = df.assign(
    revenue_check=lambda d: d["price"] * d["quantity"],
    is_expensive=lambda d: d["price"] > 300,
    product_upper=lambda d: d["product"].str.upper()
)
print(df_new.head(3))


print("2.4. Сделай цепочку assign: сначала добавь revenue_check, потом на его основе is_big = revenue_check > 5000.")
df_new = df_new.assign(
    is_big=lambda d: d["revenue_check"] > 500
)
print(df_new.head(3))
print(df_new.columns.tolist())

print("2.5. Проверь, совпадает ли df['revenue'] с df['price'] * df['quantity'] во всех строках. Подсказка: (df['revenue'] == df['price'] * df['quantity']).all().")
df_new = df_new.assign(
    is_revenue=lambda d: d["revenue"] == d['revenue_check']
)
df_filtr=df_new[df_new["is_revenue"]==False]
print(df_filtr.loc[:,['revenue','revenue_check','is_revenue']])

print("2.6. Переведи price в тип float32. Как изменился размер памяти? Подсказка: df.memory_usage(deep=True).")
print(df_new.memory_usage(deep=True))
print(df_new.dtypes)
df_new["price"] = df_new["price"].astype('float32')
print(df_new.memory_usage(deep=True))
print(df_new.dtypes)

print("2.7. Удали все временные столбцы (revenue_check, is_expensive, product_upper, is_big).")
df_new=df_new.drop(columns=['revenue_check', 'is_expensive', 'product_upper','is_big','is_revenue'])
print(df_new.columns.tolist())