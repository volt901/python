import pandas as pd

# df=pd.read_csv("sales_data.csv")
# df_date = df
# df_date['date'] = pd.to_datetime(df_date['date'])
# df_date['month'] = df_date['date'].dt.month_name()
# df_date.groupby(["category", "month"])["revenue"].sum()

# renames=df.rename(columns={
#     "category": "category_new",
#     "price" : "$"
# })
#
# print(renames.columns)
#
# renames=df.rename(index={
#     0: "first",
#     1: "second"
# })
#
# print(renames)
#

# df = pd.DataFrame({
#     "a": ["10","20","30"],
#     "b": ["10.0","20.0","30.0"],
# })
# df["a"] = df["a"].astype(int)
# df["b"] = df["b"].astype(float)
# print(df.dtypes)


df=pd.read_csv("sales_data.csv")
if 'Unnamed: 0' in df.columns:
    df=df.drop(columns=['Unnamed: 0'])


df['date'] = pd.to_datetime(df['date'])
# df['month'] = df['date'].dt.month_name()
# print(df)
# products_info = pd.DataFrame({
#     'product':  ['Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Speaker',
#                  'T-Shirt', 'Jeans', "Coat", 'Hoodie', 'Sneakers',
#                  'Backpack', 'Watch', 'Smartwatch', 'Wallet'],
#     'brand':    ['Samsung', 'Apple', 'Samsung', 'Sony', 'JBL',
#                  'Nike', 'Levis', 'Zara', 'Adidas', 'Nike',
#                  'Nike', 'Casio', 'Apple', 'Gucci'],
#     'supplier': ['Asia', 'USA', 'Asia', 'Japan', 'USA',
#                  'Europe', 'Europe', 'Europe', 'Europe', 'Asia',
#                  'Asia', 'Japan', 'USA', 'Europe'],
#     'warranty': [24, 24, 12, 12, 6,
#                  0, 0, 0, 0, 0,
#                  0, 12, 12, 0],
# })
#
# merged=df.merge(products_info,on='product',how="left")
#
# merged_sum=merged.groupby("brand")["revenue"].sum()
#
# print(merged_sum.sort_values(ascending=False))

df['month'] = df['date'].dt.month
# print(df)
df_1=df[df['month']==1]
df_2=df[df['month']==2]

combaint= pd.concat([df_1,df_2])
print(combaint)

# data = {
#     'product': ['Smartphone', 'Laptop', 'T-Shirt'],
#     'price': [600, 1200, 20]
# }
# df_clean = pd.DataFrame(data)
# print(df_clean)
#
# df_clean.to_csv('dirty_file.csv')
# df_dirty=pd.read_csv('dirty_file.csv')
# print(df_dirty)
#
# if 'Unnamed: 0' in df_dirty.columns:
#     df_dirty=df_dirty.drop(columns=['Unnamed: 0'])
# print(df_dirty)
