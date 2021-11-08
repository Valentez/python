"""
Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен
контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа
элемента и вносить его в список, только если введено число. Класс-исключение
должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""


class OwlException(Exception):
    def __init__(self):
        self.txt = 'Wrong input data. Please, input number'


mylist = []
input_str = input('Please, input number. For exit enter empty string: ')
while input_str:
    try:
        if input_str.isdigit():
            mylist.append(int(input_str))
        else:
            raise OwlException
    except OwlException as e:
        print(e.txt)

    input_str = input('Please, input number. For exit enter empty string: ')

print('Yours list is:\n', mylist)
