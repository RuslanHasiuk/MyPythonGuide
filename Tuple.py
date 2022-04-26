# Tuple (кортеж) — последовательность, которая упорядочена, но не изменяемая. Допускаются одинаковые элементы.
# Вы не можете добавлять в них новые элементы. У этого типа нет методов append() или extend()
# Удалять элементы тоже нельзя, также из-за неизменяемости. Методов remove() и pop() здесь нет
# Искать элементы в кортеже можно, потому что этот процесс его не меняет
# Разрешено использовать оператор in для проверки наличия элемента в кортеже
print("--------------------")
print("amount of items in the tuple")
mytuple = (3, 6, 1, 5, 6, 1, 76, 1)
print(mytuple)
print("--------------------")
print("Count amount of element \"1\" in the tuple")
amount = mytuple.count(1)
print(amount)
print("--------------------")
print("index of element \"6\" in the tuple")
place = mytuple.index(6)
print(place)
print("--------------------")
print("index of element \"6\" in the specific range of tuple")
print(mytuple.index(6, 2, 5))
print("--------------------")
print("Check maximum/minimum of tuple")
tuple_max = max(mytuple)
print((tuple_max))
print(min(mytuple))
print("--------------------")
print("Slices(Срезы) : output elements of tuple in some specific range e.g. from 1 to 5(!Not including \"5\")")
print(mytuple[1:5])
print("--------------------")
print("Using Frequency(Частота) - solution for printing some elements e.g. each second/third element of tuple..")
print(mytuple[::3])
print("--------------------")
print("Combine tuples - adds two tuples to one line")
x = (1, 40, 50, 4)
y = (5, 6, 7, 8)
c = x+y
print(c)
h = (5, 6, 34, 32, 8)
k = 34, 34, 45
print(h + k)
# print(z)
print("--------------------")
print("Multiple tuples - then some tuple repeats needed amount of times")
h = x * 3
print(h)
print("--------------------")
print("Check length of tuple \'h\'")
print(len(h))
print("--------------------")
print("Find out whether element of tuple may be iterable by using function \'any()\'")
y = (5,)
print(any(y))
print("This function can be useful to know if the tuple is called and you need to make sure that it is not empty.")
r = ()
print(any(r))
print("--------------------")
print("The tuple () function is used to convert data to a tuple, e.g. from [list] to tuple etc.")
some_list = [45, 65, 342, 56]
conv_list_to_tuple = tuple(some_list)
print(type(conv_list_to_tuple))
print("--------------------")
print("Calculate sum of elements in tuple")
print(sum(x))
print("--------------------")
print("If you wanna sort your tuple - make by using \'sorted()\' function")
a = (6, 7, 4, 2, 1, 5, 3)
print(a)
sorted_tuple = sorted(a)
print(sorted_tuple)
print("--------------------")
print("Multiple Tuple Assignment(Присваивание несколько кортежей)")
a = (1, 2, 3)
(one, two, three) = a
print(three)
print(one)
print(two)

print(" ---------- Unpacking: number of values to unpack Must be the same as number of elements in tuple------------")
family_members = ('Ruslan', 'Carolina', 'Olya', 'Demian')
print('Family consists of:', family_members)

print('                          So who is who ?!     ')
daddy, daugther, mommy, son = family_members
print('Daddy -', daddy)
print('Son -', son)
print('Daughter - ', daugther)
print('Mommy -', mommy)

print(" ---------------- Packing is accordingly a reverse operation to Unpacking--------------e")

teammate_1 = 'Andrew'
teammate_2 = 'Billy'
teammate_3 = 'Sam'
my_team = teammate_1, teammate_2, teammate_3
print('My team:', my_team)  # My team: ('Andrew', 'Billy', 'Sam')





# Некоторые кортежи (которые содержат только неизменяемые объекты: строки и так далее) — неизменяемые,
# а другие (содержащие изменяемые типы, например, списки) изменяемы
# Кортеж 'n_tuple' со списком в качестве одного из его элементов.
# n_tuple = (1, 1, [3,4])
# Добавить элемент в кортеж нельзя, поэтому появляется последняя ошибка AttributeError.
# Вот почему эта структура данных неизменна. Но всегда можно сделать вот так:
# n_tuple[2].append(5)
# n_tuple
# (1, 1, [3, 4, 5])

