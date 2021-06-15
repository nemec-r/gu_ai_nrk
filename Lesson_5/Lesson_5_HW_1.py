#Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

def my_func():
    in_list = input('Введите данные или нажмите "Enter" для выхода: ')
    if in_list == '':
        return in_list, True
    return (in_list + '\n'), False

with open("new.txt", "w+", encoding="UTF-8") as f_obj:
    result_list = []
    while True:
        a, b = my_func()
        if b:
            break
        result_list.append(a)
    f_obj.writelines(result_list)