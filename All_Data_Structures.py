print("Print the tuple of elements and structure type")
t = ('adsf', 'adf', 'adsff', 'Ruslan')
print(t)
print(type(t))
print('------')
print("Print tuple through loop:")
for i in t:
    print(i)
print('------')
print("Print tuple through loop  + adding text:")
for i in range(len(t)):
    print(i, "This is element " + t[i])

print('------')
print("Print the list of elements and structure type")
l = [345, 'adsf', True, 67.4, 34, 345]
print(l)
print(type(l))
print('------')

print("Print the set of elements and structure type")
s = {34, 76, 2, 89, 'Alex', 77, 21, 76, 2}
print(s)
print(type(s))
print('------')

print("Print the dict of elements and structure type")
d = {4: 'four', 7: 'seven', 11: 'eleven'}
print(d)
print(type(d))
print('------')

# Documentation: https://docs.python.org/3/tutorial/datastructures.html
