import random


def random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]  # Генерируем случайное число от 1 до 100 для каждой ячейки
        matrix.append(row)
    return matrix

# Пример использования функции
r = 5
c = 5

matrix = random_matrix(r, c)


# Вывод матрицы
for row in matrix:
    print(row)
