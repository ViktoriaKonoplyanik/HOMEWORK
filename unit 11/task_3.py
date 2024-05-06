class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def starting_the_car(self):
       print("Автомобиль заведён")

    def stop_the_car(self):
        print('Автомобиль заглушен')

    def set_year(self, new_year):
        self.year = new_year
        return new_year

    def set_color(self, new_color):
        self.color = new_color
        return new_color

    def set_type(self,new_type):
        self.type = new_type
        return new_type


car = Car('синий', 'bmv', 2022)
car.starting_the_car()
car.stop_the_car()
print(car.type, car.year, car.color)
print(car.set_type('lada'), car.set_year(2022), car.set_color('синий'))






