#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
month_number = int(input('Введите месяц числом и мы подскажем какое это время года: ')) - 1
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
year_time = ['Зима', 'Весна', 'Лето', 'Осень']
elements_len = int(len(month_list))

if month_number >= 0 < 2 or month_number > 10 < (elements_len - 1):
    print(f'Месяц {month_list[month_number]} относится к времени года {year_time[0]}')
elif month_number > 1 < 5:
    print(f'Месяц {month_list[month_number]} относится к времени года {year_time[1]}')
elif month_number > 4 < 8:
    print(f'Месяц {month_list[month_number]} относится к времени года {year_time[2]}')
else: print(f'Месяц {month_list[month_number]} относится к времени года {year_time[3]}')
