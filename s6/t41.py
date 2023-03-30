"""
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел.

Ввод: Ввод:
5
1 5 1 5 1

Вывод: Вывод:
2
"""
def create_lst(input_int):
    arr = []
    for i in range(input_int):
        arr.append(int(input(f'Enter number {i + 1}: ')))
    return arr

def num_dif(lst):
    count = 0
    for index in range(1, len(lst) - 1):
      # if lst[index] > lst[index - 1] and lst[index] > lst[index + 1]:
      if lst[index-1] < lst[index] > lst[index+1]:
        count += 1
    return count

n = int(input('Enter length of list: '))
arr  = create_lst(n)
print(num_dif(arr))