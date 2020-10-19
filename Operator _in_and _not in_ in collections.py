friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}


def is_anyone_in(collection, city):
    if city in collection.values():
        for name in collection:
            if collection[name] == city:
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')


is_anyone_in(friends, 'Челябинск')

# if city  # если есть среди значений словаря collection
#     for name  # переберите все ключи словаря
#         if  # если соответствующее ключу значение равно city
#             print('В городе ' + city + ' живёт ' + name + '.')
