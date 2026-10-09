import pandas as pd

df=pd.read_csv("sales_data.csv")

print("\nСоздай копию df под именем work:")
work=df.copy()
print(work)
# print(id(df))
# print(id(work))

print("\nЧерез .loc достань product, category, revenue для строк 0:4:")
print(work.loc[0:4,['product', 'category', 'revenue']])

print("\nЧерез .iloc достань последние 5 строк и первые 4 столбца:")
print(work.iloc[-5:,0:4])

print("\nОтфильтруй записи категории Electronics с price > 300:")
print(work[(work["category"] == "Electronics") & (work["price"] > 300)])

print("\nОтфильтруй записи из Clothing или Shoes через .isin:")
print(work[(work["category"].isin(["Clothing","Shoes"]))])

print("\nНайди товары, содержащие Phone:")
print(work[work["product"].str.contains('phone', na=False)])

print("\nЧерез .query() найди записи с revenue > 5000 и quantity >= 2:")
print(df.query("revenue > 5000 and quantity >= 2"))

print("\nДобавь month из даты и is_expensive = price > 300:")
work['is_expensive'] = work['price'] > 300
work['date'] = pd.to_datetime(work['date'])
work['month_name'] = work['date'].dt.month_name()
print(work)

print("\n Отсортируй по revenue по убыванию, выведи топ-3:")
print(work.sort_values('revenue', ascending=True).head(3))

print("\n Посчитай суммарную выручку по каждой категории :")
print(work.pivot_table(index = "category", values='revenue', aggfunc = "sum"))

print("\n Посчитай суммарную выручку по каждому месяцу:")
print(work.pivot_table(index = "month_name", values='revenue', aggfunc = "sum"))

print("\n По каждому товару: total_revenue (сумма revenue):")
print(work.pivot_table(index = "category", values='revenue', aggfunc = "sum", fill_value = 0,
                       margins = True, margins_name= "total_revenue"
                       ))

print("\n По каждому товару:  orders (кол-во записей), avg_price (средняя price):")
print(work.pivot_table(index = "category" , values='revenue', aggfunc = "count", fill_value = 0,
                       margins = True, margins_name= "orders"
                       ))

print("\n По каждому товару:  avg_price (средняя price):")
print(work.pivot_table(index = "category" , values='revenue', aggfunc = "mean", fill_value = 0,
                       margins = True, margins_name= "avg_price"
                       ))


print("\nСгруппируй по ['category', 'month'], посчитай сумму revenue, сбрось индекс:")
print(work.pivot_table(index = "month_name", columns = "category" , values='revenue', aggfunc = "sum", fill_value = 0,
                       margins = True, margins_name= "total_revenue"
                       ))