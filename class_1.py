class Product:
    def __init__(self, name:str, price:int, stock:int, categoria:Category):
        if price <= 0:
            raise ValueError("Ошибка ввода: указать цену больше 0")
        if stock < 0:
            raise ValueError("Ошибка ввода: значения остатка не может быть меньше 0")

        self.name = name
        self.price = price
        self.stock = stock
        self.categoria = categoria

    #продажа
    def sell(self, quantity:int)-> int:
        if quantity <= 0:
            raise ValueError("Ошибка ввода: указать количество проданного товара больше 0")

        if quantity > self.stock:
            raise ValueError(f"Ошибка ввода: недостаточно товара на складе, на складе: {self.stock}, запросили: {quantity}")

        self.stock -= quantity
        takings = self.price * quantity
        return takings

    #пополнение
    def restock(self, quantity:int):
        if quantity <= 0:
            raise ValueError("Ошибка ввода: указать количество принятого товара на склад больше 0")

        self.stock += quantity

    #скидка
    def apply_discount(self, percent:int)->int:
        if not 0<=percent<=100:
            raise ValueError("Ошибка ввода: указать количество проданного товара больше 0")
        self.price = round(self.price * (100 - percent)/100,2)
        return self.price

    #остаток в денежном эквиваленте
    def total_value(self)->int:
        return self.price * self.stock

class Category:
    def __init__(self, name:str, description=""):
        self.name = name
        self.description = description
        self.product=[]

    def add_product(self, product:Product):
        if product not in self.product:
            self.product.append(product)

food = Category("food")
food2 = Category("food")
food.add_product("product")
food.add_product("product")
print(food.product)

fish = Product("fish", 100, 10, food)
