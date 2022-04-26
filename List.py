# # В ЯП Python существует (4) четыре типа данных для хранения последовательностей:
#
#              # List (list) - an ordered sequence that can be changed(впорядкована послідовність, яку можна змінити).
#              # Duplicate elements are allowed. Can be of different types(Допускаються повторювані елементи. Можуть бути різних видів).
#
# print("output existing list")
# mylist = [1, 5, 6, 8, 10, 4, 34, 56, 23, 4, 8]
# print(mylist)
# length = len(mylist)
# print("--------------------")
# print("amount of items in the list")
# print(length)
# print("--------------------")
# print("identify which element is located under index \"2\"")
# print(mylist[2])
# print("--------------------")
#
# print("identify which index has element \"10\"")
# print(mylist.index(10))
# print("--------------------")
#
# print("how many times element \"8\" is placed is the list")
# print(mylist.count(8))
# print("--------------------")
#
# print("sort existing list: ascending order(from min to max")
# mylist.sort()
# print(mylist)
#
# print("--------------")
# print("initial list of names")
# names = ['Ruslan', 'Anton', 'Stas', 'Alex']
# print(names)
#
# print("Sort names in Alphabetical  order")
# names.sort()
# print(names)
# print("--------------------")
#
# print("sort existing list: descending order(from max to min")
# mylist.reverse()
# names.sort(reverse=True)
# print(mylist)
# print(names)
#
#
# print("----iteration of list----")
# for i in mylist:
#     print(i)
#
# print("----iteration of list with printing indexes of each element----")
# for i in range(len(mylist)):
#     print(i, mylist[i])
#
# print("----iteration of list with  enumeration of each element----")
# for counter, value in enumerate(mylist, 1):
#     print(counter, value)
# print("--------------------")
# print("adding / replacing new elements")
# fruits = ['banana', 'apple', 'lemon', 'orange']
# print(fruits)
# print("--------------------")
# print("how to REPLACE some element by another value")
# fruits[3] = "nuts"
# print(fruits)
# print("--------------------")
# print(" ADDING One New Element to the END of list")
# fruits.append("aubergine")
# print(fruits)
# print(fruits[4])
# print("--------------------")
# print(" ADDING More than One New Element to the END of list")
# fruits.extend(["kivi", "kokos"])
# print(fruits)
# print(fruits[5:7])
# print("--------------------")
# print("ADDING  New Element by defined index ON SPECIFIC PLACE in the list")
# fruits.insert(2, "orange")
# print(fruits)
# print("--------------------")
# print("removing new elements")
# leads = ['one', 'two', 'three', 'four', 'five']
# print(leads)
# print("--------------------")
# print("delete smth form list by saying exact element")
# leads.remove("two")
# print(leads)
# print("--------------------")
# print(" delete smth form list by saying exact index or delets last element (if not say exsct index)")
# leads.pop(2)
# print(leads)
# print("--------------------")
# print("delete smth form list by saying exact index")
# del leads[0]
# print(leads)
# print("--------------------")
# print("add to the end of the list")
# leads.append("seven")
# print(leads)
# print("--------------------")
# print("delete all the elements form list")
# leads.clear()
# print(leads)
# print("--------------------")
# print("creating list by using constructor")
# rooms = list(("NY", "LA", "Miami", "SF", "WS", 'Boston', 'Texas'))
# print(rooms)
# print("--------------------")
# print("use slice to take some range of list")
# print(rooms[1:4])
# print("--------------------")
# print("use slice to output element beginning from index 4 to the end of list")
# print(rooms[4:])
# print("--------------------")
# print("use slice to output all the elements up to element under some index of list")
# print(rooms[:6])
#
# print("--------------------")
# print("Adding Lists Togethert")
# my_sports_activities = ['boxing', 'running', 'jumping', 'wrestling', 'bodybylding', 'jumping']
# my_friend_activities = ["football", "basketball", "tennis"]
#
# our_all_types_of_sport = my_sports_activities + my_friend_activities + [88] # to add some Not List value -> should be casted to list firstly by putting into '[]'
# print(our_all_types_of_sport)
#
# print("--------------------")
# print("----------------   2D Lists ------------------------")
# print(" Create 2D List")
# customer_data = [
#   ['Ainsley', 'Small', True],
#   ['Ben', 'Large', False],
#   ['Chani', 'Medium', True],
#   ]
#
# print(customer_data[1][0])
# customer_data[1].remove(False)
# customer_data.insert(2, ['Ivan', 'Small', False])
#
# print(customer_data)


# print(customer_data)
# print(" Add new data to  2D List")
# customer_data.append(['Depak', 'Medium', False])
# print(customer_data)
#
# print(" Change specific item in  2D List")
# customer_data[2][2] = False
# print(customer_data)
#
# print(" Remove not needed element from 2D List: 'False' for Ben")
# customer_data[1].remove(False)
# print(customer_data)
#
# print(" Remove not needed element from 2D List: 'Medium' for Depak")
# customer_data[3].remove("Medium")
# print(customer_data)

# print('''The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists.
# It takes two (or more) lists as inputs and returns an object that contains a list of pairs.
# Each pair contains one element from each of the inputs. This is how we would do it for our names and heights lists:
# ''')

# names = ["Jenny", "Alexus", "Sam", "Grace"]
# print('names:', names)
#
# heights = [61, 70, 67, 64]
# print('heights:', heights)
#
# ages = [14, 13, 8, 22, 45, 34,  77]
# print('ages:', ages)
# print(ages[-4:])
# olympic_sports = ["Hockey", "Swimming", "Fencing", "Volleyball", "Breakdancing"]



# olympic_sports.pop(-1)
# print(olympic_sports)
#
# print('--------- Let\'s create  a nested list that paired each name with a height and age: -------------- ')
# students_heights_ages = zip(names, heights, ages)
# # s zip object contains the location of this variable in our computer’s memory.
# # Don’t worry though, it is fairly simple to convert this object into a useable list
# # by using the built-in function list():
# list_of_students_with_heights_and_ages = list(students_heights_ages)
# print(list_of_students_with_heights_and_ages) # -> result is final list that contains tuples: [('Jenny', 61, 14), ('Alexus', 70, 13), ('Sam', 67, 8), ('Grace', 64, 22)]



print('--------- To Convert string to list in Python: -------------- ')
print(''' Syntax:
string.split( delimiter, maxsplit)
Parameters:
Delimiter - Optional. Specifies the desired delimiter to use when splitting the string.
If left empty, whitespaces are considered delimiters. Maxsplit - Optional. Specifies how many splits to do.''')

str_1 = "Hire the top 1% freelance developers"
list_1 = str_1.split()
print(list_1)

#Output:
#['Hire', 'the', 'top', '1%', 'freelance', 'developers']



print('----------------------       List Comprehensions:  -------------------')
  # Let's assume we have a list of integers and wanted to create a list where each element is doubled. 
  # We could accomplish this using a for loop and a new list called doubled:

numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
print(doubled)
# Would output:
#[4, -2, 158, 66, -90]
  
# General Scheme for LIST COMPREHENSIONS: 
# new_list = [<expression> for <element> in <collection>]

# Here is our solution for same task but now written as a list comprehension:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)
  
#In our doubled example, our list comprehension:
# Takes an element in the list numbers
# Assigns that element to a variable called num (our <element>)
# Applies the <expression> on the element stored in num and adds the result to a new list called doubled
# Repeats steps 1-3 for every other element in the numbers list (our <collection>)
# Our result would be the same:
# [4, -2, 158, 66, -90]


print('------------   Creating a new list by using \'For\' loop and control flow only: ')

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []
for item in heights:
    if item > 161:
        can_ride_coaster.append(item)
print(can_ride_coaster)

print(' -------------   Creating a new list by using List Comprehensions only:   ')
can_ride_coaster = [item for item in heights if item > 161]
print(can_ride_coaster)


print('---------------   Syntax for using Conditionals  in  List Comprehensions  ---------------------')

numbers = [2, -1, 79, 33, -45]

# Suppose we wanted to double only our negative numbers from our previous numbers list.
doubled_numbers = [num * 2 for num in numbers if num < 0]
print('Doubled negative number from initial list:', doubled_numbers)

# Now, let’s say we want to double every negative number but triple all positive numbers
doubled_numbers = [num * 2 if num < 0 else num * 3 for num in numbers]
print('Let\'s Double negative number from initial list, and Triple positive ones:', doubled_numbers)


# Inside the loop that iterates through single_digits,
# append the squared value of each element of single_digits to the list squares.

single_digits = []

for i in range(10):
  single_digits.append(i)
print(single_digits)

squares = []

for elem in single_digits:
  print(elem)
  squares.append(elem**2)

print(squares)

# Create the list cubes using a list comprehension on the single_digits list.
# Each element of cubes should be an element of single_digits taken to the third power.

cubes = [item**3 for item in single_digits]

print(cubes)

