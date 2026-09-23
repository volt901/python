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
    def sell(self, quantity:int)->int:
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
    def apply_discount(self, percent:int)->float:
        if not 0<=percent<=100:
            raise ValueError("Ошибка ввода: скидка должна быть в диапозоне от 0 до 100%")
        self.price = round(self.price * (100 - percent)/100,2)
        return self.price

    #остаток в денежном эквиваленте
    def total_value(self)->float:
        return self.price * self.stock

class Category:
    def __init__(self, name:str, description=""):
        self.name = name
        self.description = description
        self.product=[]

    def add_product(self, product:Product):
        if product not in self.product:
            self.product.append(product)

    def remove_product(self, product:Product):
        if product in self.product:
            self.product.remove(product)

    def total_value(self)->float:
        total = 0.0
        for n in self.product:
            total += n.total_value()
        return total

food = Category("food")

fish = Product("fish", 100, 10, food)
dog = Product("dog", 10, 10, food)

food.add_product(fish)
food.add_product(dog)

print(food.total_value())


