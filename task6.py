# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка
# будет прекращено.

from itertools import count
from itertools import cycle

print("Первый скрипт.")
number_start = int(input("Введите с какого числа начинать генерировать целые числа >>> "))
number_stop = int(input("На каком числе остановиться? >>> "))

print(f"Генерация чисел с шагом 1:")
for element in count(number_start):
    if element > number_stop:
        break
    else:
        print(element, end=' ')

print(f"\nГенерация чисел с шагом 2:")
for element in count(number_start, 2):
    if element > number_stop:
        break
    else:
        print(element, end=' ')

print("\n\nВторой скрипт.")
start_spisok = [2, 4, 6, 8]
print(f"Создаем 10 циклов из заранее определенного списка {start_spisok}")
c = 0
for el in cycle(start_spisok):
    if c > 10:              # условие завершения цикла
        break
    print(el, end=' ')
    c += 1

print("\n\nВторой вариант второго скрипта.")
more_spisok = input("Введите небольшое слово: ")
more_cycle = int(input("Введите количество циклов: "))
print("Результат работы второго скрипта:")
b = 0
for letter in cycle(more_spisok):
    if b > more_cycle:
        break
    print(letter, end=' ')
    b += 1
