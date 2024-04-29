import re

def replace_names(text):



  pattern = r"\b([А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)?)\s+([А-ЯЁ][а-яё]+)\s+([А-ЯЁ][а-яё]+)\b"
  return re.sub(pattern, "N", text)

# Пример использования
text = "Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании..."
result = replace_names(text)
print(result)