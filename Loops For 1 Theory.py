# # print('---------------------------------------------------------------------------')
# # print("---------------- Iteration of floats in specific range----------------")
# # def frange(start, stop, step):
# #      i = start
# #      while i < stop:
# #           yield i
# #           i += step
# #
# # for i in frange(0.5, 1.0, 0.1):
# #     print(i)
# #
# #
# #
#
# for i in range(99, 0, -1):
# 	if i == 1:
# 		print('1 bottle of beer on the wall, 1 bottle of beer!')
# 		print('So take it down, pass it around, no more bottles of beer on the wall!')
# 	elif i == 2:
# 		print('2 more bottles of beer on the wall, 2 more bottles of beer!')
# 		print('So take one down, pass it around, 1 more bottle of beer on the wall!')
# 	else:
# 		print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
# 		print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
#
#
# # for i in range(4, 11, 2):
# #     print(i)
#
# # for i in range(0, -10, -2):
# #     print(i)
#
# homes = ('one', 'two', 'three', 'four', 'five',)
# homes_amount = len(homes)
#
# for i in range(homes_amount):
#     print(i, 'This is home № ' + homes[i])
#
# # dog = ['Freddie', 9, True, 1.1, 2001, ['bone', 'little ball']]
# # dog_l = len(dog)
# #
# # for i in dog:
# #     print(i)
#
# # edibles = ["отбивные", "пельмени", "яйца","орехи"]
# # for food in edibles:
# #     if food == "пельмени":
# #         print("Я не ем пельмени!")
# #         continue
# #     print("Отлично, вкусные " + food)
# # else:
# #     print("Ненавижу пельмени!")
# #
# # print("Ужин окончен.")
# #
#
# # from typing import List
# #
# # bingo = [1, 2, 5, 8, 0] # Якщо треба доступ до індексів
# # for i in range(len(bingo)):
# #      print(i, bingo[i])
#
# # Если вы перебираете список, лучше избегать изменения списка в теле цикла. Чтобы наглядно увидеть, что может случиться, посмотрите на следующий пример:
#
# # colours = ["красный"]
# # for i in colours:
# #     if i == "красный":
# #         colours += ["черный"]
# #     if i == "черный":
# #         colours += ["белый"]
# # print(colours) Результат: ['красный', 'черный', 'белый']
#
#
# # Чтобы избежать этого, лучше всего работать с копией с помощью срезов, как сделано в следующем примере:
#
# # colours = ["красный"]
# # for i in colours[:]:
# #     if i == "красный":
# #         colours += ["черный"]
# #     if i == "черный":
# #         colours += ["белый"]
# # print(colours) # Результат:['красный', 'черный'] Мы изменили список colours, но данное изменение не повлияло на цикл. Элементы, которые должны быть итерированы, остаются неизменными во выполнения цикла.
#
#
# # my_list = ['яблоко', 'банан', 'вишня', 'персик']
# # for c, value in enumerate(my_list, 1):
# #     print(c, value)
#

olympic_sports = ["Hockey", "Swimming", "Fencing", "Volleyball", "Breakdancing"]

print('Classic Loop without \'range\' function -- goes through each item of list')
for kind_of_sport in olympic_sports: # iterator is temparoary assigned to each item of list one after one
    print('this is', kind_of_sport)

print(' -----------------------------   ')
print('Loop with \'range\' function -- goes through each item of list')
for kind_of_sport in range(len(olympic_sports)):
	print(olympic_sports)