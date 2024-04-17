list_of_numbers = [6, 7, 10, -11, -4, 90]
sum_numbers = 0
max_number = 0
min_number = 0

for i in list_of_numbers:
    sum_numbers += i
    if max_number < i:
        max_number = i

    if min_number > i:
        min_number = i
print(f'Сумма элементов списка равна {sum_numbers}')
print(f'Максимальный элемент списка равен {max_number} ')
print(f'Минимальный элемент списка равен {min_number}')