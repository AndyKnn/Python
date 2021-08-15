# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

text: str = None


def int_func(word: str = None):
    string = input("Введите слово, состоящее из маленьких латинских букв >>> ").lower().capitalize().split(' ')
    word = string[0]
    for id, next_word in enumerate(string):
        if id == 1:
            print(f"Вы набрали более одного слова")
            print(f"Отбрасываем все слова кроме первого\n")
            break
    return word


print(f"Введеное слово, начинающееся с прописной первой буквой >>> {int_func(text)}")
