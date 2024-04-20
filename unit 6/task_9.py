import random


def matrix(rows, cols):
    matrix_ = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix_.append(row)
    total_sum = 0
    column_sums = [0] * cols

    for row in matrix_:
        for col_index, num in enumerate(row):
            total_sum += num
            column_sums[col_index] += num

    column_percentages = [(col_sum / total_sum) * 100 for col_sum in column_sums]

    return matrix_, total_sum, column_percentages


rows = 3
cols = 4
matrix_1, total_sum, column_percentages = matrix(rows, cols)

print("Матрица:")
for row in matrix_1:
    print(row)

print("Общая сумма:", total_sum)
print("Процент суммы в каждом столбце:")
for i, p in enumerate(column_percentages):
    print(f"Столбец {i+1}: {p:.2f}%")
