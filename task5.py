# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

def summary():
    try:
        print(f"При работе программы числа записываются в файл data_5.5.txt")
        with open('data_5.5.txt', 'w+') as my_file:
            line = input('Введите цифры через пробел: \n')
            my_file.writelines(line)
            my_number = line.split()
            print(sum(map(float, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()