# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_numbers=[2, 3, 4, 5, 6]
new_list=[]

def mult(list_numbers, new_list):
    """
    Фукнция ищет произведение пар чисел

    """
    for i in range(int(len(list_numbers)/2)+1):
        result=list_numbers[i]*list_numbers[len(list_numbers)-1-i]
        new_list.append(result)
    if (len(list_numbers)%2 == 0):
        result=list_numbers[len(list_numbers)-1-(int(len(list_numbers)/2)**2)]
        new_list.append(result)
    print(new_list)

mult(list_numbers, new_list)