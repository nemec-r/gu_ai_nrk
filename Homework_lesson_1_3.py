#3.	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number_n = int(input('Для решения задачи по поиску суммы чисел n + nn + nnn, введите число n: '))
#sum_n = n * (1 + (10 + 1) + (100 + 10 +1)))
#через склейку текста
sum_n = print(number_n + int('%d%d' % (number_n, number_n)) + int('%d%d%d' % (number_n, number_n, number_n)))
sum_n2 = print((int(f'{number_n}') + int(f'{number_n}{number_n}') + int(f'{number_n}{number_n}{number_n}')))