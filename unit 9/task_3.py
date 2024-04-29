import random

def generate_text_file(filename, num_lines):

    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi"]
    with open(filename, 'w', encoding='utf-8') as file:
        for _ in range(num_lines):
            line = " ".join(random.choices(words, k=random.randint(3, 10)))
            file.write(line + "\n")

def frequent_words_by_line(input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Преобразование в нижний регистр и удаление знаков препинания
            clean_line = ''.join(c for c in line.lower() if c.isalnum() or c.isspace())
            words = clean_line.split()

            # Подсчет количества вхождений слов
            word_counts = {}
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

            most_frequent_word = max(word_counts, key=word_counts.get)
            count = word_counts[most_frequent_word]

            outfile.write(f"{most_frequent_word} ({count})\n")


input_filename = "random_text.txt"
output_filename = "output.txt"
num_lines = 10

generate_text_file(input_filename, num_lines)
frequent_words_by_line(input_filename, output_filename)


