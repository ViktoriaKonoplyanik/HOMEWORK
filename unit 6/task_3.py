def check_the_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Введите число: "))
if check_the_number(num):
    print(f"{num} - простое число")
else:
    print(f"{num} - не является простым числом")