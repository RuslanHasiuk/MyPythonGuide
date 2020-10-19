# Dict (словарь) — неупорядоченная изменяемая последовательность, состоящая из пар ключ - значение.
# Получить доступ к значениям словаря Python можно с помощью ключей.
# Ключи не дублируются.
# Значения могут быть представлять собой любые типы данных и повторяться, но ключи обязаны быть уникальными.
# словари не упорядочены.

# print("---------")
# print("print dict of elements and its type")
# fishes = {1: 'dolphin', 2: 'shark', 3: 'whale', 4: 'pike', 8: 'crucian', 6: 'pike'}
# print(fishes)
# print(type(fishes))
# #
# print("---------")
# print("print value by specific key")
# print(fishes[3])
# print(fishes[8])
#
# print("---------")
# print("print key by specific value e.g. \'pike'")
# print((list(fishes.keys())[list(fishes.values()).index('pike')]))
# print((list(fishes.keys())[list(fishes.values()).index('shark')]))
#
# print("---------")
# print("Iterate each element of dict")
# for key, value in fishes.items():
#     print(key, value)
#
# print("---------")
# print("Add new element and check updated dict")
# fishes[500] = 'Tiger'
# for key, value in fishes.items():
#     print(key, value)
#
# print("---------")
# print("Update &  Remove some existing elements and check updated dict")
# fishes[3] = 'whAle'
# fishes[8] = 'Trash'
# del (fishes[6])
# for key, value in fishes.items():
#     print(key, value)
#
# print("---------")
# print("Update several pairs at the same time and check updated dict")
# # Update
# # Метод update() пригодится, если нужно обновить несколько пар сразу.
# # Метод принимает другой словарь в качестве аргумента.
# fishes.update({2: 'Big_Shark',
#                4: 'Little_pike'})
#
# for key, value in fishes.items():
#     print(key, value)
#
# print("---------")
# print("Return|Check value by defining specific value from dict ")
# # Метод get() возвращает значение по указанному ключу.
# # Если указанного ключа не существует, метод вернёт None.
# five_hundreds = fishes.get(500)
# print(five_hundreds)
# print("Return \'None\' or any another value instead of \'None\' when there is no needed key in the dict ")
# print(fishes.get(400))
# print(fishes.get(501, 0))
# print(fishes.get(300, 'absent'))
#
# print("---------")
# print("Show key \'3\' form dict \'fishes\' and show result")
# # Pop
# # Метод pop() удаляет ключ и возвращает соответствующее ему значение.
# print(fishes.pop(3))
# for key, value in fishes.items():
#     print(key, value)
#
# #
# print("---------")
# print("Show collection of keys from dict \'fishes\'")
# # Keys
# # Метод keys() возвращает коллекцию ключей в словаре.
# k = fishes.keys()
# print(k)
#
# #
# print("---------")
# print("Show collection of values from dict \'fishes\'")
# # # Values
# # # Метод values() возвращает коллекцию значений в словаре.
# val = fishes.values()
# print(val)
#
# print("---------")




