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
for regions in sales_data:
    print('Region: ', regions)
    for elements in regions:
        print('elements:', elements)
        sum_of_elements += elements
    print('Sum of elements for each region:', sum_of_elements)
print('Total of elements: ', sum_of_elements)

# Output: 
# Region:  [12, 17, 22]
# elements: 12
# elements: 17
# elements: 22
# Sum of elements for each region: 51
# Region:  [2, 10, 3]
# elements: 2
# elements: 10
# elements: 3
# Sum of elements for each region: 66
# Region:  [5, 12, 13]
# elements: 5
# elements: 12
# elements: 13
# Sum of elements for each region: 96
# Total of elements:  96



print('-----------------------------------------------------------------------------------------')
print("----------------     ----------------")

