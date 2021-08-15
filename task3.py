# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

count = 3
spisok = []

"""Функция возвращает сумму наибольших двух элементов"""
def my_func(fun_spisok):
    fun_spisok.sort(reverse=True)
    return fun_spisok[0] + fun_spisok[1]


"""Формирование списк из 3-х элементов"""
for number in range(count):
    element = int(input(f"Введите число {number + 1} >>> "))
    spisok.append(element)

print(f"Изначальный список: {spisok}")
print(f"Сумма наибольших двух аргументов: {my_func(spisok)}")
