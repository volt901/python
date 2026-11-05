import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# orders = pd.DataFrame({
#     'order_id': [1, 2],
#     'product':  ['Laptop', 'Laptop'],
#     'price':    [1000, 1000]
# })
#
# bad_products = pd.DataFrame({
#     'product': ['Laptop', 'Laptop'],
#     'brand':   ['Apple', 'Apple']
# })
#
# print(orders)
#
# merged=orders.merge(bad_products,on='product')
# print(merged)
#
# new_products=bad_products.drop_duplicates(subset=['product'])
# print(new_products)
#
# merged=orders.merge(new_products,on='product')
# print(merged)

sns.set_theme(style="whitegrid")

df = pd.read_csv('sales_data.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

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

merged=df.merge(products_info,on='product',how='left')
# print(merged)
#
# print(pd.crosstab(merged["brand"],merged["warranty"],normalize="index").round(2))
#
# print(pd.crosstab(merged["supplier"],merged["brand"],normalize="index").round(2)*100)

plt.figure(figsize=(10,5))
sns.barplot(
    data=merged,
    x = "brand",
    y = "revenue",
    estimator=sum,
    errorbar=None
)
plt.title("суммарная выручка по брендам")
plt.show()