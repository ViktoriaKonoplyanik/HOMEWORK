def censor_text(filename):

    try:
        with open("stop_words.txt", "r", encoding='utf-8') as stopwords_file:
            stop_words = set(word.strip().lower() for word in stopwords_file)

        with open(filename, "r", encoding='utf-8') as text_file:
            text = text_file.read().lower()

        censored_text = []
        word_start = 0
        for i, char in enumerate(text):
            if not char.isalnum():  # Конец слова
                word = text[word_start:i]
                if word in stop_words:
                    censored_text.append("*" * len(word))
                else:
                    censored_text.append(word)
                censored_text.append(char)  # Добавить неалфавитный символ
                word_start = i + 1
        # Обработка последнего слова, если оно есть
        if word_start < len(text):
            word = text[word_start:]
            if word in stop_words:
                censored_text.append("*" * len(word))
            else:
                censored_text.append(word)

        censored_text = "".join(censored_text)
        print(censored_text)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' или 'stop_words.txt' не найден.")


filename = "text_to_censor.txt"
censor_text(filename)


