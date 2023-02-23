"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
n = {int(input(f'{i}: ')) for i in range(int(input('Enter qty of the first list of numbers: ')))}
m = {int(input(f'{j}: ')) for j in range(int(input('Enter qty of the second list of numbers: ')))}
print(f'here is the first set: {n}')
print(f'here is the second set: {m}')

i = n.intersection(m)
i = list(i)
i.sort()
print(i)
