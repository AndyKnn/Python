# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


my_file = open('data_5.1.txt', 'w')
my_string = input("Введите строку данных:") + '\n'
while my_string:
    my_file.writelines(my_string)
    my_string = input("Введите след.строку данных:") + '\n'
    if my_string == "\n":
        print("Ввод текста в файл data_5.1.txt закончен")
        break

my_file.close()
