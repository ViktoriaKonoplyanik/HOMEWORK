def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Ввод чисел
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))


result = gcd(num1, num2)
print(f"НОД чисел {num1} и {num2} равен {result}")




