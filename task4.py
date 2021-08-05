# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число >>> "))
max = 0
value = 0

while number >= 10:
    value = number % 10
    number = number // 10
    if value >= max:
        max = value
else:
    if number > max:
        max = number

print(f'Самая большая цифра в введенном числе >>> {max}')
