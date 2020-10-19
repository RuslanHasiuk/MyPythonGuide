print("---------Arithmetic operators------------")
a = 5
b = 8
print("Addition")
my_sum = a + b
print(my_sum)
print("Subtraction")
print(a - b)
print("Division - result is a floating point number.")
my_division = b / a
print(my_division)
print(type(my_division))
print("Division without remainder|Деление без остатка (//)")
print(b // a)
print("Multiplication")
print(a * b)
print("Modulo division (remainder of division)|Деление по модулю (остаток от деления) (%)")
my_mod = b % a
print(my_mod)
print(type(my_mod))
print("Exponentiation/Возведение в степень (**)")
print(2 ** 3)
print("------------Comparison Operators----------------")
print("Less(<)")
print(5 < 9)
print("Greater(>)")
print(2 > 3)
print("Greater than or equal (> =)")
print(6 >= 6)
print("Less than or equal (> =)")
print(8 <= 8)
print("Equal (==)")
print(5 == 55)
print(1 == True)
print(0 == False)
print("Not Equal (!=)")
print(1.0 != 1)
print("-----------Assignment operators-----------")
c = 99
print(c)
c += 5
print(c)
c -= 4
print(c)
c *= 2
print(c)
c /= 1.5
print(c)
n = 5
n %= 3
print(n)
n **= 2
print(n)
n //= 3
print(n)
print("-----------Logical operators------------")
print("and | or | not ")
print(5 > 4 and 5 < 3)
print(5 > 4 or 5 < 3)
n = not (0)
print(n)
print("-----------Python Membership Operators Example------------")
# Эти операторы проверяют, является ли значение частью последовательности.
# Последовательность может быть списком, строкой или кортежем.
m = 10
n = 20
list = [1, 2, 3, 4, 5]

if m in list:
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if n not in list:
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

m = 2
if a in list:
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")

pets = ['dog', 'cat', 'ferret']
print('fox' in pets)
print('cat' in pets)
print('tiger' not in pets)
print("--------------Identity Operators-----------")
z = {43, 23, 9}
x = {23, 9, 43}
print(x == z)
# returns True because content in [x] is  same as in [z]
print(x is z)
# returns False because [x] is not the same object as [z], even if they have the same content
v = x
print(v is x)
# returns True because v is the same object as x
print(v is z)
# returns False because v is the Not same object as z
# to demonstrate the difference between "is" and "==": this comparison returns True because v is equal to z
print(v == z)
print(v is not z)
print("--------------Bitwise Operators-----------")
# "Bitwise operator works on bits and performs bit by bit operation. Assume if a = 60; and b = 13; Now in the binary format their values will be 0011 1100 and 0000 1101 respectively. Following table lists out the bitwise operators supported by Python language with an example each in those, we use the above two variables (a and b) as operands")
# a = 0011 1100
# b = 0000 1101
# -----------------
# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a  = 1100 0011
# There are following Bitwise operators supported by Python language"

