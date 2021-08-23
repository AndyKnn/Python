# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []


with open("data_5.4_old.txt") as my_file_old:
    print(f"Изначально в файле data_5.4_old.txt записана след. информация:")
    print(my_file_old.read())
    my_file_old.seek(0)         #Возвращаемся в начало файла
    for i in my_file_old:
        name, value = i.split(' - ')
        new_file.append(f"{rus[name]} - {value}")

with open("data_5.4_new.txt", "w") as my_file_new:
    my_file_new.writelines(new_file)

print(f"В новый файл data_5.4_new.txt записана след. информация:")
for x in new_file:
    print(x.replace('\n', ''))
