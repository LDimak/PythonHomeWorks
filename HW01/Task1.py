# Найдите сумму цифр трехзначного числа

number = str(input('Введите трехзначное число: '))
if len(str(number)) !=3:
    print('Вы ввели не трехзначное число!')
else:
    print(int(number[0])+int(number[1])+int(number[2]))