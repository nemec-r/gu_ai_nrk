#Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
def string_count(string):
    i = 0
    for line in string:
        i += 1
    return f'Данный файл содержит {i} строк(и)'

with open("new.txt", "r", encoding="UTF-8") as f_obj:
    content = f_obj.readlines()

print(string_count(content))

for el, str in enumerate(content,1):
    word_len = len(str.strip().split(" "))
    print(f'Строка №{el} содержит {word_len} слов')


