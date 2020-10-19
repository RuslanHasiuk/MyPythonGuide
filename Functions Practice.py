# def first(a, b):
#     if a > b:
#         print("a is more than b")
#     elif a == b:
#         print("a is equal to b")
#     else:
#         print("b is more than a")
#
# first(5, 6)


# def second(x, y=7):
#     return x + y

# six = second(6, 8)
# print(six)
#
# ten = second(10)
# print(ten)
#
#
#
# d = ef MyFunction(first, secoond, third=5, four=7):
#     print(first + secoond + third + four)
#
# h = MyFunction(3, 5, 8, 9)


# Задача: проганяти всі цифри в заданому діапазоні, і з них виводити тільки парні
# def printEvenNumbers(x, y):
#     for i in range(x, y):
#         if i % 2 != 0:
#             continue
#         else:
#             print(i)
#
#
# printEvenNumbers(20, 31)
# # print("------------------------------------------")


# Задача: проганяти всі цифри в заданому діапазоні, і з них виводити тільки Непарні
# def printOddNumbers(x, y):
#     for i in range(x, y):
#         if i % 2 == 0:
#             continue
#         else:
#             print(i)

# printOddNumbers(20, 31)


# def print_friends_count(friends_count):
#     if friends_count == 1:
#         print('У тебя 1 друг')
#     elif 2 <= friends_count <= 4:
#         print('У тебя ' + str(friends_count) + ' друга')
#     elif friends_count >= 5:
#         print('У тебя ' + str(friends_count) + ' друзей')

# print_friends_count(1)
# print_friends_count(3)
# print_friends_count(19)


# print("-------------------------------------------------------------------")
# print("------------ Write a loop in which print_friends_count ()"
#       " function  is called ONLY with arguments from 1 to 10 --------")
# friends_count = 0
# for i in range(friends_count, 11):
#     print_friends_count(friends_count)
#     friends_count += 1


# print("-------------------------------------------------------------------")
# print("------------ Functions with [arguments by default] -----------------")
# def print_friends_count(friends_count, name=""):
#     if friends_count == 1:
#         text = '1 друг'
#     elif 2 <= friends_count <= 4:
#         text = str(friends_count) + ' друга'
#     elif friends_count >= 5:
#         text = str(friends_count) + ' друзей'
#     if name:
#         print(name + ', у тебя ' + text)
#     else:
#         print('У тебя ' + text)
#
# print_friends_count(3, 'Артём')
# print_friends_count(friends_count=7, name='Марина')
# print_friends_count(6)
# print_friends_count(4, name='Настя')

# print("-------------------------------------------------------------------")
# print("------------ Using 1(One) Function WITHIN another Function -----------------")
# FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
#
#
# def print_friends_count(friends_count):
#     if friends_count == 1:
#         print('У тебя 1 друг')
#     elif 2 <= friends_count <= 4:
#         print('У тебя ' + str(friends_count) + ' друга')
#     elif friends_count >= 5:
#         print('У тебя ' + str(friends_count) + ' друзей')


#
#
# # перенесите в функцию process_query() вот этот код:
# def process_query():
#     print("Привет, я Анфиса!")
#     count = len(FRIENDS)
#     print_friends_count(count)
#
#
# process_query()


# print("-------------------------------------------------------------------")
# print("------------ Using more than 1 Functions WITHIN another Function -----------------")
#
# def process_query(query):
#     print("Привет, я Анфиса!")
#     count = len(FRIENDS)
#     if query == 'Сколько у меня друзей?':
#         print_friends_count(count)
#     else:
#         print('<неизвестный запрос>')
#
#
# process_query('Сколько у меня друзей?')
# process_query('Как меня зовут?')

# print("-------------------------------------------------------------------")
# print("------------ Adding one more condition for listing all friends "
#       "in accordance with the question about this  -----------------")
#
# Friends_string = ', '.join(FRIENDS)
#
# def process_query(query):
#     print("Привет, я Анфиса!")
#     count = len(FRIENDS)
#     if query == 'Сколько у меня друзей?':
#         print_friends_count(count)
#     elif query == 'Кто все мои друзья?':
#         print('Твои друзья: ' + Friends_string)
#     else:
#         print('<неизвестный запрос>')
#
#
# #process_query('Сколько у меня друзей?')
# #process_query('Как меня зовут?')
# process_query('Кто все мои друзья?')

# print("-------------------------------------------------------------------")
# print("------------ Use a counter to retrieve the number of days over "
#       "a specific temperature range in 1 month -----------------")
may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25,
            17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23,
            18, 22, 23, 11]

#
# def comfort_count(temperatures):
#     comfort_days = 0
#     for days in temperatures:
#         if 22 <= days <= 26:
#             comfort_days += 1
#     print('Количество комфортных дней в этом месяце:', comfort_days)
#
#
# comfort_count(may_2017)  # узнаем, что было в мае 2017 г.
# comfort_count(may_2018)  # узнаем, что было в мае 2018 г.


# print("-------------------------------------------------------------------")
# print("------------ Use keyword \'RETURN\' in functions: Example #1 -----------------")


# def comfort_count(temperatures):
#     count = 0
#     for temp in temperatures:
#         if 22 <= temp <= 26:
#             count += 1
#     return 'Количество комфортных дней в этом месяце: ' + str(count)
#
#
# print(comfort_count(may_2017))

#
# print("-------------------------------------------------------------------")
# print("------------ Use keyword \'RETURN\' in functions: Example #2 -----------------")
#
# FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
#
#
# def show_count_friends(count_friends):
#     if count_friends == 1:
#         return 'У тебя 1 друг'
#     elif 2 <= count_friends <= 4:
#         return 'У тебя ' + str(count_friends) + ' друга'
#     elif count_friends >= 5:
#         return 'У тебя ' + str(count_friends) + ' друзей'
#
#
# def process_query(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(FRIENDS)
#         return show_count_friends(count)
#     elif query == 'Кто все мои друзья?':
#         friends_string = ', '.join(FRIENDS)
#         return 'Твои друзья: ' + friends_string
#     else:
#         return '<неизвестный запрос>'
#
#
# # Внимание! Это те самые вызовы, которые не надо трогать
# print(process_query('Сколько у меня друзей?'))
# print(process_query('Кто все мои друзья?'))
# print(process_query('Как меня зовут?'))


print("-------------------------------------------------------------------")
print("------------  ----------------")



