numbers = [3, 5, 10, 9]
duplicates = {}

is_unique = True

for num in numbers:
    if numbers.count(num) > 1:
        duplicates[num] = numbers.count(num)
        is_unique = False

if is_unique:
    print("Все числа в списке уникальны.")
else:
    print("Не все числа в списке уникальны.")
    print("Дублирующиеся элементы и количество их повторений:")
    for key, value in duplicates.items():
        print(f"Число {key} встречается {value} раз(а).")