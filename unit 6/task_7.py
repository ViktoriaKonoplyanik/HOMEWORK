import random


def random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]  # Генерируем случайное число от 1 до 100 для каждой ячейки
        matrix.append(row)
    return matrix

# Пример использования функции
row = 5
cols = 5

matrix = random_matrix(row, cols)


# Вывод матрицы
for row in matrix:
    print(row)
