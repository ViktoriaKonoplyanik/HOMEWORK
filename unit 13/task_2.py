def cyclic_sequence_generator(seq):
    while True:
        for num in seq:
            yield num

sequence = [1, 2, 3]

while True:
    try:
        count = int(input("Введите количество чисел для вывода: "))
        if count <= 0:
            print("Пожалуйста, введите положительное число.")
        else:
            break
    except ValueError:
        print("Пожалуйста, введите целое число.")

gen = cyclic_sequence_generator(sequence)

for _ in range(count):
    print(next(gen))
