# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract_number_date(cls, day_month_year):
        date = []

        for i in day_month_year.split('-'):
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def date_validator(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


today = Date('06-09-2021')
print(Date.date_validator(11, 11, 2022))
print(today.date_validator(11, 13, 2011))
print(Date.extract_number_date('06-09-2021'))
print(Date.date_validator(6, 9, 2021))
