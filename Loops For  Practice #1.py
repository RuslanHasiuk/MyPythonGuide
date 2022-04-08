languages = ["C", "C++", "Perl", "Python"]
print('------')
print('usual loop For')

for i in languages:
    print(i)

print('------')
print('Loops For with showing indexes of elements')

languages_length = len(languages)
for i in range(languages_length):
    print(i, languages[i])

print('------')
print('Skip some item of list if you don\'t need it')

for i in languages:
    if i == "Perl":
        print("No, miss Perl")
        continue
    else:
        print("This is " + i)

print('------')
print('interrupt iteration at all  if U come across item in list if you don\'t need it')

for i in languages:
    if i == "C++":
        print("I hate C++")
        break
    else:
        print("this is " + i)

print('------')
print('Iterate list with showing number of items')

for c, value in enumerate(languages, 1):
    print(c, value)

from typing import Set

print('------')
print("Iteration of set")

row = {5, 7, 23, 45, 98, 4, 23, 56, 4, 11}
#won\'t work because sets are unordered therefore do not support indexing and slicing.
# for i in range(len(row)):
#     print(i, row[i])
# Workaround - Make this set as a list!
my_row = list(row)
for i in range(len(my_row)):
    print(my_row[i])

print('---------------------------------------------------------------------------')
print("---------------- Iteration of list ----------------")

bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']
length = len(bremen_musicians)
for i in bremen_musicians:
    print(i)
print('---------------------------------------------------------------------------')
print("---------------- Iteration of reversed list ----------------")
for i in reversed(bremen_musicians):
    print(i)

print('---------------------------------------------------------------------------')
print("---------------- Iteration of digitals in specific range ----------------")
for i in range(2, 9):
    print(i)
print('---------------------------------------------------------------------------')
print("---------------- Iteration of digitals in specific range (reversed order) ----------------")
for i in reversed(range(2, 9)):
    print(i)
print('-------------- Nested Loops ----------------')

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)

print('---------------------------------------------------------------------------')
print("---------------- ----------------")

