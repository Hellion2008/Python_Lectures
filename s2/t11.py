# num = int(input('Enter your number: '))
# first, second = 0, 1
# res = 0
# count = 2
# while res < num:
#     res = first + second
#     # print(f'{res}, {first}, {second}')
#     first = second
#     second = res
#     count += 1
#     # print(count)
# if res == num:
#     print(count)
# else:
#     print(-1)


number = int(input())
f1 = f2 = 1
n = 3
while number > f2:
  f1, f2 = f2, f1 + f2
  n += 1
print(n if number == f2 else '-1')
