# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print("Ведите элемены списка через пробел.")
string = input("Для окончания ввода списка нажмите Enter: ")
spisok = string.split(' ')

print(f"Изначально список выглядит так: {spisok}")

j = 0
for i in range(int(len(spisok) / 2)):
    spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
    j += 2

print(f"После обмена соседними элементами список выглядит так: {spisok}")

