def find_palindrome(text):

    text = text.lower()
    return text == text[::-1]

strings = ['рвалдедлавр', 'лешанаполкеклопанашел', 'abc','аргентинаманитнегра','ишакуказаксенанесказакукаши','python']
palindromes = list(filter(find_palindrome, strings))

print("Исходный список:", strings)
print("Палиндромы :", palindromes)
