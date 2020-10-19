# Set (множество) — неупорядоченная изменяемая последовательность. Одинаковые элементы удаляются.
# Множества примечательны тем, что операция проверки "принадлежит ли объект множеству"
# происходит значительно быстрее аналогичных операций в других структурах данных.

print("--------------------")
print("Just print all the elements  in the set")
set_of_digits = {6, 0.7, 4, 7, 87, 3, 2, 7.1}
print(set_of_digits)
list_from_set = list(set_of_digits)
print(len(list_from_set))
print("--------------------")
print("set data structure is referred as Unordered Collections of "
      "Unique Elements and that doesn't support operations like indexing or slicing etc. "
      "To iterate set = U should cast it to list !!!"
      )
for i in set_of_digits:
    print("this is digital: " + str(i))


print("-----------------------------------------------------")
bands = ['Пикник', 'Ария', 'Блестящие', 'Блестящие']
# получаем сет unique_band_names (с англ. «уникальные названия групп»)
unique_band_names = set(bands)

for band in unique_band_names:
    print('Доктор, я не могу больше слушать группу ' + band)

print("-----------------------------------------------------")
print("---------------  Print  Just Unique titles of cities from existing List-----------------")
cities = ['Вологда', 'Чебоксары', 'Тольятти', 'Вологда']

unique_cities = set(cities)
print(', '.join(unique_cities))



cities = ['Санкт-Петербург', 'Хабаровск', 'Казань', 'Санкт-Петербург', 'Казань']

uniq_cities = set(cities)
for i in uniq_cities:
    print('Один мой друг живёт в городе ' + i)


print("-----------------------------------------------------")
print("---------------  Choose from all the cities that there are in the set "
      "ONLY those not been used yet -----------------")

all_cities = {'Абакан', 'Астрахань', 'Бобруйск', 'Калуга', 'Караганда', 'Кострома', 'Липецк', 'Новосибирск'}
used_cities = set(['Калуга', 'Абакан', 'Новосибирск'])


def print_valid_cities(all, used):
    not_used_cities = all_cities.difference(used_cities)
    print(', '.join(not_used_cities))


print_valid_cities(all_cities, used_cities)

print("-----------------------------------------------------")
print("--------------- It is necessary to make the final recipe from two existing, "
      "without repeating components twice-----------------")


def print_shopping_list(recipe1, recipe2):
    final_recipe = recipe1.union(recipe2)
    print(', '.join(final_recipe))


pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
pizza_recipe_set = set(pizza)
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']
salad_recipe_set = set(salad)

print_shopping_list(pizza_recipe_set, salad_recipe_set)


print("-----------------------------------------------------")
print("---------------  Learn how to develop a function that will print on the screen "
      "what products you need to buy and how many you need -----------------")

pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}


def print_shopping_list(pizza, salad):
    pizza_set = set(pizza)
    salad_set = set(salad)
    components_final_set = pizza_set.union(salad_set)
    for item in components_final_set:
        if item in pizza and item in salad:
            a = pizza[item] + salad[item]
        elif item in pizza:
            a = pizza[item]
        else:
            a = salad[item]
        print(item + ": " + str(a))


print_shopping_list(pizza, salad)
