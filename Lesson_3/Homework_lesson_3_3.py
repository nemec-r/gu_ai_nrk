#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(var_1, var_2, var_3):
    try:
        return sum((var_1, var_2, var_3)) - min(var_1, var_2, var_3)
    except TypeError:
        return 'Use numbers only'

print(my_func(8, 12, 5))