class Product:
    def __init__(self, name:str, price:int, stok:int, categoria:Category):
        self.name = name
        self.price = price
        self.stok = stok
        self.categoria = categoria
    ...

class Category:
    def __init__(self, name:str, description=""):
        self.name = name
        self.description = description
        self.__product=[]

    def add_product(self, product:Product):
        self.__product.append(product)

food = Category("food")
fish = Product("fish", 10, 100, food)

print(fish.categoria.name)