"""
Даны два массива чисел. 
Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, 
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод: 
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод:
3 3 2 12
"""

def create_lst(input_int):
    arr = []
    for i in range(input_int):
        arr.append(int(input(f'Enter number {i + 1}: ')))
    return arr

def dif_el (lst1, lst2):
    for el in lst1:
        if el not in lst2:
            print(el, end = ' ')


n = int(input('Enter length of first list: '))
m = int(input('Enter length of second list: '))
ar1 = create_lst(n)
ar2 = create_lst(m)
dif_el(ar1, ar2)

# def remove_el(lst1, set2):
#   for i in set2:
#     while i in lst1:
#       lst1.remove(i)
#   return(lst1)

# l1 = [int(input(f"Введите элемент массива {i + 1}: ")) for i in range(int(input("Введите длину массива: ")))]
# l2 = set([int(input(f"Введите элемент массива {i + 1}: ")) for i in range(int(input("Введите длину массива: ")))])

# print(l1)
# print(l2)
# print(*remove_el(l1, l2))