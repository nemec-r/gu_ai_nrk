#Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("new_numbers.txt", "w", encoding="UTF-8") as f_obj:
    in_list = input('Введите числа через пробел: ')
    print(in_list, file=f_obj)

with open("new_numbers.txt", "r", encoding="UTF-8") as f_read:
    content = f_read.readlines()
    content = [line.strip().split(' ') for line in content]
    s = 0
    for line in content:
        for number in line:
            s += float(number)
    print(s)