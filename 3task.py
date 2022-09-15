# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

num_list=[1.1, 1.2, 3.1, 5.17, 10.02]
print(num_list)


def search(num_list):
    """
    Функция ищет дробную часть
    """
    new_list=[]
    for i in num_list:
        new_list.append(round((i-int(i))*100))
    print(new_list)
    return max(new_list), min(new_list)

search(num_list)

def result():
    """
    Функция считает разницу
    """
    max,min=search(num_list)
    result=max-min
    print(result)

result()
