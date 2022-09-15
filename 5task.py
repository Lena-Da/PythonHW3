# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def input_num():
    """
    Функция проверяет ввод числа
    """
    try:
        num=int(input("Введи число: "))
        if num < 0:
            print ("Введи число больше 0")
    except ValueError:
        print("Ввели не число, попробуй еще")

    def fibonachi(num)->list:
        """
        Функция создает положительный список Фибоначчи
        """
        count1=count2=1
        for i in range(num):
            yield count1
            count1, count2 = count2, count1+count2
    result=list(fibonachi(num))
    print(result)
    fibonachi(num)

    def negafibonachi(num)->list:
        """
        Функция создает отрицательный список Фибоначчи
        """
        count3=count4=-1
        for i in range(num):
            yield count3
            count3, count4 = count4, count3+count4
    result=list(negafibonachi(num))
    print(result)
    negafibonachi(num)

input_num()