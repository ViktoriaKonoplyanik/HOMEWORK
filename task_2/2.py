import time
import threading
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

    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Время выполнения многопоточной программы: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
