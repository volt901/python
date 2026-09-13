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

    def sell(self, quantity:int)-> int:
        if quantity <= 0:
            raise ValueError("Ошибка ввода: указать количество проданного товара больше 0")

        if quantity > self.stock:
            raise ValueError(f"Ошибка ввода: недостаточно товара на складе, на складе: {self.stock}, запросили: {quantity}")

        self.stock -= quantity
        takings = self.price * quantity
        return takings

class Category:
    def __init__(self, name:str, description=""):
        self.name = name
        self.description = description
        self.__product=[]

    def add_product(self, product:Product):
        self.__product.append(product)

food = Category("food")
fish = Product("fish", 99, 10, food)
print(fish.stock)
fish.sell(10)
print(fish.stock)

print(fish.stock)
