import time
import multiprocessing

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_factorial(n):
    result = factorial(n)
    print(f"Факториал({n}) вычислен")

def main():
    data = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800]
    processes = []

    start_time = time.time()

    for n in data:
        process = multiprocessing.Process(target=calculate_factorial, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Время выполнения многопроцессной программы: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
