import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Загрузка
df = pd.read_csv('sales_data.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

# Справочник (без колонки category, чтобы избежать дубля _x и _y)
products_info = pd.DataFrame({
    'product':  ['Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Speaker',
                 'T-Shirt', 'Jeans', 'Coat', 'Hoodie', 'Sneakers',
                 'Backpack', 'Watch', 'Smartwatch', 'Wallet'],
    'brand':    ['Samsung', 'Apple', 'Samsung', 'Sony', 'JBL',
                 'Nike', 'Levi\'s', 'Zara', 'Adidas', 'Nike',
                 'Nike', 'Casio', 'Apple', 'Gucci'],
})

# Объединяем
merged = df.merge(products_info, on='product', how='left')

'''
Задание 1.
Оставь в таблице merged только товары бренда Apple и Samsung (используй .isin).
Сгруппируй данные по месяцу (month), чтобы узнать суммарную выручку (revenue).
Построй линейный график (lineplot), где по оси X — месяц, по оси Y — выручка.
Сделай маркеры в виде квадратов, цвет линии — темно-синий (darkblue).
'''
merged = merged[merged['brand'].isin(['Apple','Samsung'])]
print(merged)

merged_revenue=merged.groupby("month")["revenue"].sum().reset_index()
print(merged_revenue)

plt.figure(figsize=(10, 5))

# sns.lineplot(
#     data=merged_revenue,
#     x='month',
#     y='revenue',
#     marker = "s",
#     linewidth = 3,
#     color = "darkblue"
# )
#
# plt.title("линейный график")
# plt.xticks(range(1,13))
# plt.xlabel("месяц",fontsize = 14)
#
# plt.ylabel("выручка",fontsize = 14)
#
# plt.show()

"""
Задание 2.
Создай копию таблицы work = merged.copy().
Представь, что произошел сбой и 15% (примерно 55 строк) цен (price) стали NaN. Сделай это с помощью np.random.choice.
Заполни пропуски медианой (.median()).
Построй гистограмму (histplot) для очищенной колонки price. Используй 20 корзин (bins=20) и 
включи линию распределения (kde=True).
"""
work = merged.copy()

work_nan = np.random.choice(work.index, size=55, replace=False)
work.loc[work_nan, 'price'] = np.nan
print(work['price'].loc[work_nan])
work['price'] = work['price'].fillna(work['price'].median())

# sns.histplot(
#     data=merged,
#     x ='price',
#     bins = 20,
#     kde=True,
#     color = "red",
#     edgecolor = "black"
# )
#
# plt.title("Гистограмма")
#
# plt.show()

"""
Задание 3.
Построй boxplot, который покажет разброс цен (price) для каждой категории (category)
Но перед построением оставь только те категории, где средняя цена (mean) больше 100.
Сделай подписи оси X повернутыми на 45 градусов.
"""

# df_price_mean = df[df['price'] > 100]
# sns.boxplot(
#     data=df_price_mean,
#     x ='category',
#     y = 'price',
#     palette = 'Set3'
# )
#
# plt.xlabel("категория",fontsize = 14)
# plt.ylabel("цена",fontsize = 14)
# plt.title("график")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

"""
Задание 4.
С помощью crosstab узнай, сколько раз каждый бренд (brand) продавался в каждый месяц (month).
"""
merged = df.merge(products_info, on='product', how='left')
merged_crosstab=pd.crosstab(merged ["brand"], merged ["month"],margins=True, margins_name="Total")

"""
Оставь в таблице merged только те бренды, у которых общее количество продаж за год больше 20 (используй value_counts).
"""
brand_counts = merged["brand"].value_counts()
brands_fillter = brand_counts[brand_counts > 20].index.tolist()
"""
Сгруппируй отфильтрованные данные по двум столбцам: month и brand, чтобы посчитать суммарную выручку (revenue). 
Не забудь сбросить индекс (reset_index), чтобы Seaborn смог прочитать данные.
"""
merged_total = merged[merged["brand"].isin(brands_fillter)].reset_index()

"""
Построй линейный график (lineplot), где по оси X — месяц (month), по оси Y — выручка (revenue).
"""

sns.lineplot(
    data=merged_total,
    x='month',
    y='revenue',
    marker = "s",
    linewidth = 3,
    color = "red"
)

plt.title("линейный график")
plt.xticks(range(1,13))
plt.xlabel("месяц",fontsize = 14)

plt.ylabel("выручка",fontsize = 14)

plt.show()








"""
Раскрась линии по брендам с помощью параметра hue='brand'. Добавь маркеры в виде кружочков (marker='o').

Добавь заголовок, поверни подписи X (на 45 градусов) и вынеси легенду за пределы графика, 
чтобы она не перекрывала линии (используй plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')).
"""

