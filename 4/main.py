def f(x):
    return x**2

a = f #переменная хранит в себе ссылку на функцию
print(f(5))
print(a(5))

def calc1(x):
    return x+x

def calc2(x):
    return x*x

def math(func, x):
    print(func(x))

math(calc1, 5)
math(calc2, 5)

# лямбда-функция
calc3 = lambda a, b: a + b
print(calc3(2,4))
math(lambda a: a ** 3, 5)

list1 = [1, 2, 3, 5, 8]
lst = [(x, x**2) for x in list1 if x % 2 == 0]
print(lst)

# решение с помощью лямбда-функции
def select (f, col):
    return [f(x) for x in col]

def where (f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, data)
print(res)
res = list(select(lambda x: (x, x*x), res))
print(res)

# использование функции map, применить какое то действие для каждого элемента списка
list_1 = [s for s in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

data = '15 20 15 0 4 9 42 41'
data = list(map(int, data.split()))
print(data)

# функция filter

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

# функция zip
users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [122, 4556, 45]
data = list(zip(users, ids, salary))
print(data) # входят элементы по минимальной длине из списков

# функция enumerate
data = list(enumerate(users))
print(data)

# работа с файлами 
colors = ['red', 'yellow', 'blue']
data = open('file.txt', 'a', encoding= 'utf-8')
data.writelines(colors)
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

print("end")

# режим чтения из файла
path = 'file.txt'
data = open(path, "r")
for line in data:
    print(line)
data.close()


