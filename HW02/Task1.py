"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import randint
q = int(input('How many coins are there? :'))
coins_list = []
count_zero = 0
count_one = 0

for i in range(1,q+1,1):
    coin_face = randint(0, 1)
    coins_list.append(coin_face)
    if coin_face == 0:
        count_zero = count_zero + 1
    if coin_face == 1:
        count_one = count_one + 1
print(coins_list)
if count_zero > count_one:
    print(f'minimal qty of coins to rotate is {count_one}')
if count_zero < count_one:
    print(f'minimal qty of coins to rotate is {count_zero}')
elif count_one == count_zero:
    print(f'qty of ZEROs = qty of ONEs, so there is no difference what coins are to rotate, minimum qty will be the same : {count_one}')