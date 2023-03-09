n = 5
print(n)

n = None
print(n)

# n = None
# print(n)

"""
n = 1.89
print(n)

n = 'gjf\'k'
print(n)

print(type(n))
"""
n = 1.89
print(n)

n = 'gjf\'k'
print(n)

print(type(n))

a = 5
b = 5.89
c = 'hello'

print(a,' - ', b,' - ', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a,b,c))

a = input()
print(a)
b = input('Enter number ')

print(a, ' + ', b, ' = ', a + b)

a = int(input())
print(a)
b = int(input('Enter number '))

print(a, ' + ', b, ' = ', a + b)

c = 5.89
print(c)
c = int(c)
print(c)

a = 5.65656
b = 6.56565
print(round(a*b, 3))

username = input('Enter name: ')
if username == 'Masha':
    print('Yes! It\'s Masha' )
elif username == 'Marina':
    print('Hey, hello Marina')
elif username == 'Ilnar':
    print('Hi, my friend Ilnar')
else:
    print('Hello, ', username)

i = 0
while i < 5:
    # if i == 3:
      #  break
    i = i + 1
else:
    print("Enough")
print(i)

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1

r = range(5) # 0 1 2 3 4 
r = range(2, 5) #2 3 4
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20)
for i in r:
    print(i)

a = 'qwerty'

print(a[0]) # q

text = 'СЪЕШЬ ещё этих МяГкИх французких булок'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё', 'ЕЩЁ'))