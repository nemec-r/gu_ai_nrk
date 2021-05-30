#Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

my_list2 = []
n = int(input('Введите количество элементов для заполнения списка: ')) - 1
numbers_list = 0
while numbers_list <= n:
    my_list2.append(numbers_list)
    numbers_list += 1

print(my_list2)
elements_len = len(my_list2)
# решения через обмен значениями
for i in my_list2:
    while i < (elements_len - 1):
        n = i + 1
        my_list2[i], my_list2[n] = my_list2[n], my_list2[i]
        i += 2
    else:
        break
print(my_list2)

#решение через переменную
"""for m in my_list2:
    while m < (elements_len - 1):
        n = m + 1
        a = my_list2[m]
        b = my_list2[n]
        my_list2[m] = b
        my_list2[n] = a
        m += 2
    else:
        break
print(my_list2)"""


