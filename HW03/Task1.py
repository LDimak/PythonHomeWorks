"""
Задаем длину списка наполненного рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
"""
from random import randint

list_1 = []
n = int(input('Enter qty of elements in the list: '))
for i in range(n):
    list_1.insert(i, randint(1, 100))
print(f'the generated list is : {list_1}')


k = int(input('What number we are looking at in the list?: '))
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count = count + 1
if count > 0:
    print(f'The number: {k} is met in the list: {count} times')
if count == 0:
    closest_number = list_1[0]
    for j in range(len(list_1) - 1):
        if abs(k - list_1[j+1]) < abs(k - closest_number):
            closest_number = list_1[j+1]
    print(f'We found the closest number: {closest_number} ')

