import random


def adding_strings(rows, cols):
    matrix = []
    l = 3

    print('Начальная матрица:')
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
        print(row)

    for i in range(rows):
        for j in range(cols):
            if i != l:
                matrix[i][j] += matrix[l][j]
    return matrix

rows = 5
cols = 4
matrix = adding_strings(rows, cols)

print("Матрица:")
for row in matrix:
  print(row)

