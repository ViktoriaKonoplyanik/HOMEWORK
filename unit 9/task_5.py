with open('students.txt', 'w') as f:
    while True:
        surname = input('Введите фамилию: ')
        if surname == '':
            break
        name = input('Введите имя: ')
        score = input('Введите оценку: ')
        f.write(f'{surname} {name} {score}\n')

with open('students.txt', 'r') as f:
    for line in f:
        surname, name, score = line.split()
        if float(score) < 3:
            print(f' Ниже 2 :{surname} {name}')
