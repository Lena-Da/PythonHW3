# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

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

    def translation(num):
        """
        Функция переводит число из десятичной в двоичную систему
        """
        result=""
        count=""
        while num>0:
            count=str(num%2)
            result=count+result
            num=int(num/2)
        print(result)
    translation(num)

input_num()