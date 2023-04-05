"""
Напишите функцию same_by(characteristic, objects), которая проверяет, 
все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, 
функция должна возвращать True. Аргумент characteristic - это функция, 
которая принимает объект и вычисляет его характеристику.
Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)

Вывод:
same
"""
def same_by(func, vals):
    res_val = []
    for i in vals:
        res_val.append(func(i))

    if len(set(res_val)):
        return True
    return False

# return len(set(map(func,vals))) <= 1


values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

# 2 условия во включении 
a = [1, 4, 5, 7 ,6]
list1 = [(item + 10 if item > 4 else item - 10 ) for item in a if not item % 2]
print(list1)


