# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class MyDateClass:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def conversion_date(cls, new_date):
        try:
            date_list = new_date.split('-')
            day = int(date_list[0])
            month = int(date_list[1])
            year = int(date_list[2])
            return cls(day, month, year)
        except ValueError:
            print('Ошибка при вводе даты')
        except AttributeError:
            print('Ошибка при вводе даты')
        except IndexError:
            print('Ошибка при вводе даты')

    @staticmethod
    def check_date(obj):
        check_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            if MyDateClass.conversion_date(obj).year % 400 != 0 and MyDateClass.conversion_date(obj).year % 100 == 0:
                if 1 <= MyDateClass.conversion_date(obj).day <= check_days[MyDateClass.conversion_date(obj).month]:
                    print('Correct date')
                    return True
                raise Exception
            elif MyDateClass.conversion_date(obj).year % 400 != 0 and MyDateClass.conversion_date(obj).year % 4 != 0:
                if 1 <= MyDateClass.conversion_date(obj).day <= check_days[MyDateClass.conversion_date(obj).month]:
                    print('Correct date')
                    return True
                raise Exception
            else:
                if MyDateClass.conversion_date(obj).month == 2 and 1 <= MyDateClass.conversion_date(obj).day <= 29:
                    return True
                elif 1 <= MyDateClass.conversion_date(obj).day <= check_days[MyDateClass.conversion_date(obj).month]:
                    return True
                raise Exception
        except KeyError:
            print(f'Некорректная дата! Неверно введен месяц')
            return False
        except TypeError:
            return False
        except Exception:
            print(f'Некорректная дата! Неверно введен день')
            return False


my_date = input('Введите дату в формате DD-MM-YEAR: ')
my_1 = MyDateClass.conversion_date(my_date)
print(my_1.check_date(my_date))
