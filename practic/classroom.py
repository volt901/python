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

df = pd.DataFrame({
    "a": ["10","20","30"],
    "b": ["10.0","20.0","30.0"],
})
df["a"] = df["a"].astype(int)
df["b"] = df["b"].astype(float)
print(df.dtypes)