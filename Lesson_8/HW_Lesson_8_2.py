# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


print('Привествую Вас в программе осуществляющей деление двух чисел')
inp_param_1 = int(input('Введите делимое число: '))
inp_param_2 = int(input('Введите делитель: '))

try:
    if inp_param_2 == 0:
        raise OwnError('Вы ввели 0 в качестве делителя')
    division_param = float(inp_param_1 / inp_param_2)
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {division_param:.2f}")
