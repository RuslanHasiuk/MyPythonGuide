heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

print('------------   Creating a new list by using \'For\' loop and control flow only: ')
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
