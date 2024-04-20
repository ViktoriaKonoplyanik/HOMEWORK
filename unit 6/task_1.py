from random import randint


def binary_search_recursive(a, left, right, n):
    mid = (left+right) // 2
    if a[mid] == n:
        return mid
    elif a[mid] > n:
        return binary_search_recursive(a, 0, mid - 1, n)
    else:
        return binary_search_recursive(a, 0, mid + 1, n)


a = []
for i in range(10):
    a.append((randint(1, 50)))
    a.sort()
print(a)
n = int(input('Введите искомое: '))
print(f' ID :{binary_search_recursive(a, 0, len(a) - 1, n)} ')















