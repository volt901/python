import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Настройка стиля графиков
sns.set_theme(style="whitegrid")

# 1. Загрузка и подготовка данных
df = pd.read_csv('sales_data.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

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
    'warranty': [24, 24, 12, 12, 6, 0, 0, 0, 0, 0, 0, 12, 12, 0],
})

# 3. Объединяем таблицы
merged = df.merge(products_info, on='product', how='left')

print(
"""
Часть 1. Метод crosstab
1.1. Построй перекрестную таблицу (crosstab), где строки — это категории (category), а столбцы — месяцы (month). Внутри 
должно быть количество записей.
Напиши в комментарии, в каком месяце было больше всего продаж товаров из категории Electronics?
"""
)
crosstab_merge=pd.crosstab(merged["category"],merged["month"])
print(crosstab_merge)
print(f"в {crosstab_merge.loc['Electronics'].idxmax()} месяц было больше всего продаж товаров из категории Electronics")

print(
"""
1.2. Построй crosstab для поставщиков (supplier) и брендов (brand). Добавь параметр margins=True, чтобы увидеть 
общее количество товаров по каждому поставщику и бренду внизу и справа.
"""
)
crosstab_supplier=pd.crosstab(merged["supplier"],merged["brand"],margins=True)
print(crosstab_supplier)

print(
"""
1.3. Построй crosstab для бренда (brand) и гарантии (warranty).
Теперь используй normalize='index' и умножь таблицу на 100, чтобы получить проценты. 
Оставь 1 знак после запятой (.round(1)).
Вопрос: Какой процент товаров от Samsung имеет гарантию 24 месяца?
"""
)
crosstab_brand=(pd.crosstab(merged["brand"],merged["warranty"],normalize='index')*100).round(1)
print(crosstab_brand)
crosstab_brand_Samsung=crosstab_brand.loc["Samsung"]
print(crosstab_brand_Samsung)
print(f"{crosstab_brand_Samsung.loc[24]} % товаров от Samsung имеет гарантию 24 месяца")


print(
"""
1.4. Построй crosstab, где строки — категория (category), столбцы — бренд (brand), 
а значения — проценты по столбцам (normalize='columns' умноженное на 100).
Вопрос: Какая категория составляет 100% товаров бренда Gucci?
"""
)
crosstab_category=(pd.crosstab(merged["category"],merged["brand"],normalize='columns')*100).round(1)
print(crosstab_category)
crosstab_category_Gucci=crosstab_category["Gucci"]
print(crosstab_category_Gucci)
print(f"{crosstab_category_Gucci[crosstab_category_Gucci == 100].index.tolist()} - категория составляет 100% товаров бренда Gucci")

print(
"""
Часть 2. Визуализация:
2.1. Построй столбчатую диаграмму (sns.barplot), которая показывает суммарное количество проданных штук 
(quantity) для каждой категории (category).

Используй estimator=sum.

Отключи "усы" погрешности (errorbar=None).

Задай размер картинки (8, 5).

Дай графику заголовок "Продажи в штуках по категориям".
"""
)
# 1. Создаем "холст" (фигуру) и задаем его размер
# plt.figure(figsize=(8, 5))

# 2. Рисуем сам график
# sns.barplot(
#     data=merged,       # Откуда берем данные
#     x='category',         # Что будет на горизонтальной оси (категории)
#     y='quantity',       # Что будет на вертикальной оси (числа)
#     estimator=sum,     # Как считать (сумма)
#     errorbar=None      # Убираем линии погрешности
# )

# 3. Добавляем заголовок
# plt.title("Продажи в штуках по категориям")

# 4. Показываем результат
# plt.show()

print(
"""
2.2. Построй barplot, где:

Ось X — это бренды (brand).

Ось Y — это средняя цена (price).

Не указывай estimator (пусть Seaborn сам посчитает среднее по умолчанию).

Отключи errorbar.

Поверни подписи по оси X на 45 градусов (plt.xticks(rotation=45)), чтобы они не наезжали друг на друга.
"""
)
# plt.figure(figsize=(8, 5))
# sns.barplot(
#     data=merged,       # Откуда берем данные
#     x='brand',         # Что будет на горизонтальной оси (категории)
#     y='price'     # Что будет на вертикальной оси (числа)
# )
#
# plt.xticks(rotation=45)
# # 3. Добавляем заголовок
# plt.title("Средняя цена брендов")
#
# # 4. Показываем результат
# plt.show()

print(
"""
2.3. (Задание с подвохом) Посмотри на код ниже. В нём есть 3 ошибки, из-за которых график не построится 
или будет выглядеть неправильно. Найди и исправь их.

# Найди 3 ошибки в этом коде:
import matplotlib as plt

plt.figure(figsize=(10, 5))
sns.barplot(
    data=merged, 
    x='category', 
    y='revenue'
)
plt.title("Выручка")
"""
)
# нету pyplot — модуль для управления графиками
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(10, 5))
# sns.barplot(
#     data=merged,
#     x='category',
#     y='revenue'
# )
# plt.title("Выручка")
#
# # отсутствовал метод для отображения результата
# plt.show()


print(
"""
Часть 3. Комплексная задача
Представь, что ты делаешь презентацию . Нужно показать, как выручка по категориям меняется в зависимости от месяца.

Сначала построй pivot_table: строки — category, столбцы — month, значения — сумма revenue.

Сохрани этот результат в переменную pivot.
"""
)
pivot=merged.pivot_table(index="category",columns="month", values="revenue",fill_value=0 ).reset_index()
print(pivot)

"""

Теперь построй сгруппированный barplot на основе этого pivot.
"""
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
sns.barplot(
    data=merged,
    x='category',
    y='revenue',
    hue='month',
    estimator=sum,
    errorbar=None
)

plt.title("выручка категорий в течении года (v1)")
plt.show()

"""
Альтернативный (более простой) вариант: построй barplot прямо из merged: x='category', y='revenue',
hue='month', estimator=sum.
"""

plt.figure(figsize=(8, 5))
sns.barplot(
    data=merged,
    x='category',
    y='revenue',
    hue='month',
    estimator=sum,
    errorbar=None
)

plt.title("выручка категорий в течении года (v2)")
plt.show()