from random import randint

a = []
for i in range(10):
    a.append(randint(1,50))
a.sort()
print(a)

value = int(input('Введите позицию искомого элемента:  '))

low = 0
high = len(a) - 1
mid = (low + high) // 2

while value != a[mid] and low < high:
    if value > a[mid]:
        low = mid + 1
    else:
         high = mid - 1
    mid = (low + high) // 2

if value == a[mid]:
    print('ID:', mid)
else:
    print('No value')
    print('Программа завершена')
