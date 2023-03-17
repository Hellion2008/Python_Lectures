"""
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо, K – положительное число.

Input:   [1, 2, 3, 4, 5] k = 3

Output:  [4, 5, 1, 2, 3]
"""

n, k = [1, 2, 3, 4, 5], int(input("Enter k: "))
k = k % len(n) # отсекание лишних итераций 

# first
# print(n[k:] + n[:k])


# second
# list = [1, 2, 3, 4, 5,6,7,8,9]
# print (list)
# n,k=len(list),5

# while k>0 :
#     list.append(list[0])
#     list.pop(0)
#     k -=1
#     print (list)

for i in range(k-1):
    num = n.pop(-1)
    n.insert(0, num)
print(n)
