#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.
def my_func():
    s = 0
    in_list = input('Введите числа через пробел или нажмите Q для выхода: ').upper().split()
    for i in in_list:
        if i == 'Q':
            return s, True
        try:
            s += int(i)
        except ValueError:
            pass
    return s, False

result = 0
while True:
    a, b = my_func()
    result += a
    print(result)
    if b:
        break