# В ЯП Python существует (4) четыре типа данных для хранения последовательностей:

             # List (list) - an ordered sequence that can be changed(впорядкована послідовність, яку можна змінити).
             # Duplicate elements are allowed. Can be of different types(Допускаються повторювані елементи. Можуть бути різних видів).
                        
print("output existing list")
mylist = [1, 5, 6, 8, 10, 4, 34, 56, 23, 4, 8]
print(mylist)
length = len(mylist)
print("--------------------")
print("amount of items in the list")
print(length)
print("--------------------")
print("identify which element is located under index \"2\"")
print(mylist[2])
print("--------------------")

print("identify which index has element \"10\"")
print(mylist.index(10))
print("--------------------")

print("how many times element \"8\" is placed is the list")
print(mylist.count(8))
print("--------------------")

print("sort existing list: ascending order(from min to max")
mylist.sort()
print(mylist)

print("--------------")
print("initial list of names")
names = ['Ruslan', 'Anton', 'Stas', 'Alex']
print(names)

print("Sort names in Alphabetical  order")
names.sort()
print(names)
print("--------------------")

print("sort existing list: descending order(from max to min")
mylist.reverse()
names.sort(reverse=True)
print(mylist)
print(names)


print("----iteration of list----")
for i in mylist:
    print(i)

print("----iteration of list with printing indexes of each element----")
for i in range(len(mylist)):
    print(i, mylist[i])

print("----iteration of list with  enumeration of each element----")
for counter, value in enumerate(mylist, 1):
    print(counter, value)
print("--------------------")
print("adding / replacing new elements")
fruits = ['banana', 'apple', 'lemon', 'orange']
print(fruits)
print("--------------------")
print("how to REPLACE some element by another value")
fruits[3] = "nuts"
print(fruits)
print("--------------------")
print(" ADDING One New Element to the END of list")
fruits.append("aubergine")
print(fruits)
print(fruits[4])
print("--------------------")
print(" ADDING More than One New Element to the END of list")
fruits.extend(["kivi", "kokos"])
print(fruits)
print(fruits[5:7])
print("--------------------")
print("ADDING  New Element by defined index ON SPECIFIC PLACE in the list")
fruits.insert(2, "orange")
print(fruits)
print("--------------------")
print("removing new elements")
leads = ['one', 'two', 'three', 'four', 'five']
print(leads)
print("--------------------")
print("delete smth form list by saying exact element")
leads.remove("two")
print(leads)
print("--------------------")
print(" delete smth form list by saying exact index or delets last element (if not say exsct index)")
leads.pop(2)
print(leads)
print("--------------------")
print("delete smth form list by saying exact index")
del leads[0]
print(leads)
print("--------------------")
print("add to the end of the list")
leads.append("seven")
print(leads)
print("--------------------")
print("delete all the elements form list")
leads.clear()
print(leads)
print("--------------------")
print("creating list by using constructor")
rooms = list(("NY", "LA", "Miami", "SF", "WS", 'Boston', 'Texas'))
print(rooms)
print("--------------------")
print("use slice to take some range of list")
print(rooms[1:4])
print("--------------------")
print("use slice to output element beginning from index 4 to the end of list")
print(rooms[4:])
print("--------------------")
print("use slice to output all the elements up to element under some index of list")
print(rooms[:6])

print("--------------------")
print("Adding Lists Togethert")
my_sports_activities = ['boxing', 'running', 'jumping', 'wrestling', 'bodybylding', 'jumping']
my_friend_activities = ["football", "basketball", "tennis"]

our_all_types_of_sport = my_sports_activities + my_friend_activities + [88] # to add some Not List value -> should be casted to list firstly by putting into '[]'
print(our_all_types_of_sport)

print("--------------------")
print("----------------   2D Lists ------------------------")
print(" Create 2D List")
customer_data = [
  ['Ainsley', 'Small', True],
  ['Ben', 'Large', False],
  ['Chani', 'Medium', True],
  ]
print(customer_data)
print(" Add new data to  2D List")
customer_data.append(['Depak', 'Medium', False])
print(customer_data)

print(" Change specific item in  2D List")
customer_data[2][2] = False
print(customer_data)

print(" Remove not needed element from 2D List: 'False' for Ben")
customer_data[1].remove(False)
print(customer_data)

print(" Remove not needed element from 2D List: 'Medium' for Depak")
customer_data[3].remove("Medium")
print(customer_data)


print('test')