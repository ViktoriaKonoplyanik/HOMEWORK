import random


def multiplying_columns(rows, cols):
    matrix = []
    k = 3

    print('Начальная матрица:')
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
        print(row)

    for i in range(rows):
        for j in range(cols):
            if j != k:
                matrix[i][j] *= matrix[i][k]
    return matrix

rows = 3
cols = 4
matrix = multiplying_columns(rows, cols)

print("Матрица:")
for row in matrix:
  print(row)

