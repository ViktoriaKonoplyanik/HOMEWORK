class Soda:
    def __init__(self, taste):
        self.taste = taste

    def print_soda(self):
        if isinstance(self.taste, str):
            return f'Газировка имеет {self.taste} вкус'
        else:
            return 'У вас обычная газировка'


drink1 = Soda('клубничный')
print(drink1.print_soda())

drink2 = Soda(5)
print(drink2.print_soda())

drink3 = Soda('малиновый')
print(drink3.print_soda())

drink4 = Soda(234567890)
print(drink4.print_soda())


