#4.	Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input('Введите целое положительное число больше 10: '))
number_max = 0
while  number != 0:
    if number_max < number % 10:
        number_max = number % 10
    number = number // 10
print(f'Самая большая цифра :{number_max}')