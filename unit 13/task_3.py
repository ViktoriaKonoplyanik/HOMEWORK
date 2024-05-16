class Pizza:
    def __init__(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        pizza_str = f"Pizza Size: {self.size}\n"
        pizza_str += f"Cheese: {self.cheese}\n"
        pizza_str += f"Pepperoni: {self.pepperoni}\n"
        pizza_str += f"Mushrooms: {self.mushrooms}\n"
        pizza_str += f"Onions: {self.onions}\n"
        pizza_str += f"Bacon: {self.bacon}\n"
        return pizza_str


class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_small_pizza(self):
        self.builder.set_size("Small")
        self.builder.add_cheese()
        return self.builder.build()

    def make_large_pizza(self):
        self.builder.set_size("Large")
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.add_onions()
        return self.builder.build()



builder = PizzaBuilder()
director = PizzaDirector(builder)

small_pizza = director.make_small_pizza()
print(small_pizza)

large_pizza = director.make_large_pizza()
print(large_pizza)

custom_pizza = builder.set_size("Medium").add_cheese().add_bacon().build()
print(custom_pizza)

