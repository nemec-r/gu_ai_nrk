#Создать (не программно) текстовый файл со следующим содержимым:
# One - 1
# Two - 2
# Three - 3
# Four - 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("eng.dict.txt", "r", encoding="UTF-8") as f_1:
    with open("eng.dict.txt", "w", encoding="UTF-8") as f_2:
        f_2.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in f_1])