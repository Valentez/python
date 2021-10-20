"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

grammarFunc = lambda word: word.capitalize()
int_func = lambda word1: word1.title()

inString = input("Please, input string:\n")
print(grammarFunc(inString))
print(int_func(inString))
# resultStringList = []
# inWords = inString.split()
# for i in inWords:
#     resultStringList.append(grammarFunc(i))
# print(" ".join(resultStringList))

#
