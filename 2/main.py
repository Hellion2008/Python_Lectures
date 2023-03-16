# создание пустого листа
list_1 = [] 
list_2 = list()
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1)
print(*list_1)

for i in list_1:
    print(i)

print(len(list_1))

list_1.append(888)
print(list_1)

a = list_1.pop()
print(list_1)
print(a)
list_1.pop(1)
print(list_1)
list_1.insert(1, 9)
print(list_1)


# кортеж (тот же список только неизменяемый)
t = ()
print(type(t))

t = (1)
print(type(t))

t = (1, 5, 3)
print(type(t))

v = [1, 5, 8]
print(v)
print(type(v))
v = tuple(v)
print(v)
print(type(v))

# распаковка кортежа
a,b,c = v
print(a, b, c)

# словари (тот же список, но доступ по ключу (слово, число))
d = {}
d = dict()
d['q'] = 'qwerty'
print(d)
d['w'] = 'werty'
print(d)
print(d['q'])
d['s'] = 'ssssss'
print(d)
del d['s']
print(d)
for i in d:
    print(f'{i}: {d[i]}')
for (k, v) in d.items():
    print(f'{k}: {v}')

# множества (содержит уникальные неповторяющиеся значения)
q = set() #пустое множество 
colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')
print(colors)
colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
# удаляет элемент, если он есть
colors.discard('red')
print(colors)
colors.clear()


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
u = a.union(b)
i = a.intersection(b)
dl = a.difference(b)
dr = b. difference(a)

# замороженное множество
f = frozenset(a)

# генератор списка
list_3 = [i for i in range(1,101)] #1 2 3 ... 100
list_4 = [i for i in range(1, 101) if i % 2 == 0] #2 4 6 ... 100





