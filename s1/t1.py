"""
За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2
"""
import math
speed = int(input("Enter speed: "))
print("Enter distance: ")
distanse = int(input())
# day = math.ceil(distanse/speed)
day = (distanse + speed - 1) // speed
print(f"Days: {day}")

# булевое значение превращается в число
# print((m := int(input())) // (n := int(input())) + (m % n > 0))