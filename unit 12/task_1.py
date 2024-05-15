class Product:
    def __init__(self, name, shop, price):
        self.name = name
        self.shop = shop
        self.price = price


class Warehouse:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def get_by_index(self, index):
        return self.products[index]

    def get_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError("Товар с таким именем не найден")

    def sort_by_names(self):
        self.products.sort(key=lambda product: product.name)

    def sort_by_shops(self):
        self.products.sort(key=lambda product: product.shop)

    def sort_by_prices(self):
        self.products.sort(key=lambda product: product.price)

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

warehouse = Warehouse()
warehouse.add(Product("Товар 1", "Магазин 1", 100))
warehouse.add(Product("Товар 2", "Магазин 2", 200))
warehouse.add(Product("Товар 3", "Магазин 3", 300))

# Печать информации о товаре по индексу
print(f"Товар по индексу 1: {warehouse.get_by_index(1).name}, магазин: {warehouse.get_by_index(1).shop}, цена: {warehouse.get_by_index(1).price}")

# Печать информации о товаре по имени
try:
    product = warehouse.get_by_name("Товар 2")
    print(f"Товар по имени \"Товар 2\": {product.name}, магазин: {product.shop}, цена: {product.price}")
except ValueError as e:
    print(e)

# Сортировка по названиям
warehouse.sort_by_names()
print("Сортировка по названиям:")
for product in warehouse.products:
    print(product.name, end=", ")
print()

# Сортировка по магазинам
warehouse.sort_by_shops()
print("Сортировка по магазинам:")
for product in warehouse.products:
    print(product.shop, end=", ")
print()

# Сортировка по ценам
warehouse.sort_by_prices()
print("Сортировка по ценам:")
for product in warehouse.products:
    print(product.price, end=", ")
print()


