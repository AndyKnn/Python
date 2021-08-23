# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def get_entries(infile):
    with open(infile, 'r') as my_file:
        for line in my_file:
            name, salary = line.split(' ', 1)
            float_salary = float(salary)
            yield name, float_salary


my_dict = dict(get_entries('data_5.3.txt'))     #Получение словаря из файла 'data_5.3.txt'
#print(my_dict)

spisok_surname = []

for x, y in my_dict.items():        #Перебор словаря, и составление списка фамилий, у которых зарплата < 2000
    if y < 20000:
        spisok_surname.append(x)


string_surname = ', '.join(spisok_surname)      #Из списка фамилий делаем строку
print(f"Фамилии сотрудников, имеющих оклад менее 20000:\n {string_surname}")


average_salary = (sum(my_dict.values())) / (len(my_dict))       #Подсчет средней величины дохода сотрудников
print(f"Средняя величина дохода сотрудников: {average_salary}")
