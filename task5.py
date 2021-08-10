# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print("Введите первоначальный рейтинг. Числа должны быть целыми.")
print("Числа набирать через пробел.")
string_number = input("После набора рейтинга нажмите Enter >>> ")

spisok = ([int(s) for s in string_number.split(' ')])
print("Набранный рейтинг: ", spisok)

spisok.sort(reverse=True)

print("Отсортированный рейтинг: ", spisok)

while True:
    print("Для выхода из набора рейтинга нажмите Ctrl + D")
    try:
        new_rating = int(input("Введите новый рейтинг >>> "))
        spisok.append(new_rating)
        spisok.sort(reverse=True)
        print(f"Пользователь ввел число {new_rating}. Результат: {spisok}.")
    except EOFError:
        break

print(f"\nОкончательный результат: {spisok}")
