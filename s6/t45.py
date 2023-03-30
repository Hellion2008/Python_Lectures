"""
Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз 
(перестановка чисел новую пару не дает).

Ввод:
300

Вывод:
220 284
"""
def find_sum(k):
    sum = 0
    for i in range(1, k):
        if k % i == 0:
            sum += i
    return sum

def find_pairs(k):
    dic_pairs = {}
    for i in range(2, k):
        if i in dic_pairs.values():
            continue
        first = find_sum(i) 
        second = find_sum(first) 
        if second == i and first != second:
            dic_pairs[i] = first
            print(f'{i} ______ {first}')


print(find_pairs(300))

def sum_num(k):
    sum1 = 0
    for i in range(1, (k // 2) + 1):
        if k % i == 0:
            sum1 += i
    return sum1

k = int(input('Введите число: '))
for i in range(1, k):
    j = sum_num(i)
    if i < j <= k and i == sum_num(j):
        print(i, j)