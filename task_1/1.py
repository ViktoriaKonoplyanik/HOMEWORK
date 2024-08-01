import time

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():

    data = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800]

    #  время начала выполнения программы
    start_time = time.time()

    #факториал для каждого значения в списке
    for n in data:
        result = factorial(n)
        print(f"Факториал({n}) вычислен")

    # время окончания выполнения программы
    end_time = time.time()
    #  время выполнения программы
    print(f"Время выполнения последовательной программы: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
