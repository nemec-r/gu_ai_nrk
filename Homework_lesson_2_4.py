#Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

my_str = str(input('Введти несколько слов через пробел: '))
my_str_lentgh = len(my_str)
str_list = my_str.split(' ')

for el, str in enumerate(str_list, 1):
    max_str = len(str)
    if max_str > 10:
        print(f'Строка №{el}. Длина слова более {max_str} символов, напечатаем только первые десять символов: {str[:10]}')
    else:
        print(f'Строка №{el}. {str}')
