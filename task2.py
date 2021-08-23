# Создать текстовый файл(не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('data_5.2.txt') as my_file:
    line_count = 0
    for line in my_file.readlines():
        str_spisok = line.split(' ')
        if str_spisok[0] == '\n':  # Проверка на пустые строки в конце файла
            break
        word_count = len(str_spisok)
        print(f"В строке {line_count + 1}: {word_count} слова")
        line_count += 1

print(f"Всего в файле data_5.2.txt: {line_count} строк")
