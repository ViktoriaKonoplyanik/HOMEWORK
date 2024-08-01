import time
import multiprocessing
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"Запрос к {url} выполнен с кодом статуса {response.status_code}")

def main():
    urls = [

        "https://www.google.com",
        "https://www.github.com",
        "https://translated.turbopages.org",
        "https://www.python.org",
        "https://habr.com",
        "https://www.wikipedia.org",

    ]

    processes = []
    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Время выполнения мультипроцессорной программы: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
