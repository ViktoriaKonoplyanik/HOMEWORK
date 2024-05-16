def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


while True:
    try:
        n = int(input("Введите номер числа Фибоначчи: "))
        if n <= 0:
            print('Пожалуйста, введите положительное число!')
        else:
            break
    except ValueError:
        print('Пожалуйста, введите целое число ')

for num in fibonacci_generator(n):
    print(num)