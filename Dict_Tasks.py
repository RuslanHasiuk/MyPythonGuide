friends = {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}
print("Where does \'Серёга\' live ?")
print("Серёга lives in ", str(friends['Серёга']))

print("---------")
friends = {'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Иван': 'Питер',
    'Миша': 'Львов'}

print((list(friends.keys())[list(friends.values()).index('Львов')]))


friends_cities = ', '.join(friends.values())
print("Вот в каких городах живут мои друзья: ", str(friends_cities))
print("---------Iterate names---------------")
friends['Bob'] = "LA"
friends['Bob'] = "SF"

for i in friends:
    print("Names of my friends: " + i)

print("---------Iterate cities---------------")
for i in friends.values():
        i
        print("Cities, where my friends live in: " + i)

print("---------Iterate name AND cities together---------------")
print(friends.items())
for name, city in friends.items():
    print(name, "живёт в городе",  city)


print("---------  Several ways to retrieve amount of values of SOme One Key  ---------------")
favorite_songs = {
    'Серёга': ["Unforgiven", "Holiday", "Highway to hell"],
    'Соня': ["Shake it out", "Don't stop me now", "Наше лето"],
    'Дима': ["Владимирский централ", "Мурка", "Третье сентября"]
}

dima_songs = favorite_songs['Дима']
# by using loop
count = 0
for i in dima_songs:
    count += 1
print(count)
# by using 'length' property
print(len(dima_songs))


print("---------  Print values of some specific key in a raw  ---------------")
sonya_songs_string = ', '.join(favorite_songs['Соня'])
print(sonya_songs_string)

print("---------  Make a dict from 2(two) lists!  ---------------")
friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

for i in range(len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]
print(friends)

print("-------------------------------------------------------------------")
print("Лена живёт в городе " + friends['Лена'])