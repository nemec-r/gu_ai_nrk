#Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
# Сидоров 21038.22
# Васечкин 33003.12
# Ложкин 27575.45
# Вилкин 18375.85
# Ножкин 29364.74
# Потемкин 75638.47
# Молчунов 13035.76
# Почемучкин 9564.99

with open("salary.txt", "r", encoding="UTF-8") as f_1:
    content = f_1.readlines()

content = [line.rstrip() for line in content]

new_list = [line.split(' ') for line in content]

max_salary = 20000

all_money = 0
count = 0
for new_line in new_list:
    count += 1
    for name, money in zip(new_line,new_line[1:]):
        all_money += float(money)
        if float(money) < max_salary:
            print(f'{name} имеет оклад менее {max_salary} рублей')

print(f'Средний доход сотрудников по компании {(all_money / count):.2f} рублей')
