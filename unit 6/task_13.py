
import random

def multiplying_columns(rows, cols):
    matrix = []

    print('Начальная матрица:')
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
        print(row)

    def sum_diagonals(matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        sum_main_diagonal = 0
        sum_secondary_diagonal = 0
        for i in range(min(rows, cols)):
            sum_main_diagonal += matrix[i][i]
            sum_secondary_diagonal += matrix[i][cols - 1 - i]
        return sum_main_diagonal, sum_secondary_diagonal


    main_sum, secondary_sum = sum_diagonals(matrix)
    print("Сумма главной диагонали:", main_sum)
    print("Сумма побочной диагонали:", secondary_sum)
    return matrix


rows = 4
cols = 4
matrix = multiplying_columns(rows, cols)


