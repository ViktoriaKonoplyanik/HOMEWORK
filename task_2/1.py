import time
import requests

def fetch_url(url):
    response = requests.get(url)
    return response.status_code

def main():
    urls = [

        "https://www.google.com",
        "https://www.github.com",
        "https://translated.turbopages.org",
        "https://www.python.org",
        "https://habr.com",
        "https://www.wikipedia.org",

    ]

    start_time = time.time()

    for url in urls:
        status_code = fetch_url(url)
        print(f"Запрос к {url} выполнен с кодом статуса {status_code}")

    end_time = time.time()
    print(f"Время выполнения последовательной программы: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
