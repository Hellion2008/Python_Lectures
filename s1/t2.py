"""
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
"""
import math
class1 = int(input("Enter first class: "))
class2 = int(input("Enter second class: "))
class3 = int(input("Enter third class: "))
# table = math.ceil(class1 / 2) + math.ceil(class2 / 2) + math.ceil(class3 / 2)
table = (class1 + 2 - 1) // 2 + (class2 + 2 - 1) // 2 + (class3 + 2 - 1) // 2
print(table)