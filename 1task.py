# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def rand_list():
    """
    Функция создает массив случайных чисел

    """
    list_numbers=[]
    for i in range(1,6):
        list_numbers.append(randint(1,9))
    print(list_numbers)

    def sum_elem(list_numbers)->int:
        """
        Эта функция ищет сумму элементов списка на нечетной позиции

        """
        sum_elem=0
        for i in range(len(list_numbers)):
            if i % 2 != 0:
                sum_elem+=list_numbers[i]
        print(sum_elem)
    sum_elem(list_numbers)
    

rand_list()   




