#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    for char in word:
        if ord(char) >= 97 <= 122:
            new_string = word.capitalize()
            return new_string


words = input('Ввведите слово состоящие из маленьких латинский букв: ').split()
for i, word in enumerate(words):
    if not word.isalpha() or not word.islower():
        print('ошибка')
    else:
        words[i] = int_func(word)
print(' '.join(words))


