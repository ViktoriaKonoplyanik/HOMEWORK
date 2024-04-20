def binary_interpretation(decimal):
    if decimal == 0:
        return "0"
    if decimal == 1:
        return "1"
    else:
        return binary_interpretation(decimal // 2) + str(decimal % 2)


dec_num = int(input('Введите десятичное число:'))
print(f'Двоичное число: {binary_interpretation(dec_num)}')


