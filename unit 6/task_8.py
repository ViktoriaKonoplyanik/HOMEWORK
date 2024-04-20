import random

def matrix(rows, cols):
    matrix_ = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix_.append(row)

    min_value = float('inf')
    max_value = float('-inf')
    for row in matrix_:
        for num in row:
            min_value = min(min_value, num)
            max_value = max(max_value, num)


    return matrix_, min_value, max_value

rows = 5
cols = 5
matrix_1, min_element, max_element = matrix(rows, cols)

for row in matrix_1:
    print(row)

print("Минимальный элемент:", min_element)
print("Максимальный элемент:", max_element)
