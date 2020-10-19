# print("------------------------------------  Joining Strings "
#       "-------------------------------------")
# print("Create some list and print it")
# some_list = ['one', 'two', 'three', 'four', 'five']
# print(some_list)
# print("-----------------------------------------------------------------------------------------------------")
# print("join some string to existing list --- List automatically converted to string  ")
# added_params = ' AND '
# together = added_params.join(some_list)
# print(together)
# print("----------------------------------------------------------------------------------------------------
# print("join some string to Not String --- will cauze \'TypeError: sequence item 0: "
#       "expected str instance, int found\'  ")
# xxx = [5, 7, 34, 0, 11]
# # mmm = added_params.join(xxx)  # "TypeError: sequence item 0: expected str instance, int found"
# print("----------------------------------------------------------------------------------------------------")
# print("So, by applying string's method \'join\' - any data structures become strings as well - [concatenation]")
# friends = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
# print(friends)
# friends_string = ', '.join(friends)
# print("Твои друзья: " + friends_string)
# print("----------------------------------------------------------------------------------------------------")
# stations = ['Москва', 'Серп и Молот', 'Карачарово', 'Чухлинка', 'Кусково',
#             'Новогиреево', 'Реутово', 'Никольское',
#            ]
# print(stations)
# print("To print items from List collection in a rwa- use \'join\' ")
# stations_schedule = ' - '.join(stations)
# print(stations_schedule)
# print("----------------  Split string for smaller strings  ----------------------")
# name = 'Jean-Claude Van Damme'
# print(name.split('-'))
# l = name.split()
# print(l[1])
# print("---------------- Use method \'strip()\' to remove redundant symbols "
#       "e.g. dots at the end of words  ----------------------")
# blok_string = 'Ночь. Улица.  Фонарь. Аптек'
# splitted_string = blok_string.split()
# print(splitted_string[2])
# print(splitted_string[2].strip('.'))
# print("---------------- Retrieve element from String by calling negative indices ---------------------")
# print(name[-9])
# s = 'spam'
# # s[1] = 'b'  # causes "TypeError: 'str' object does not support item assignment"
# s = s[0] + 'b' + s[2:]
# print(s*4)
# s = s[0] + 'b' + s[2:]


# blok_string = 'Ночь. Улица.  Фонарь. Аптека.'
# # из строки получаем список:
# blok_list = blok_string.split()
# print(blok_string)
# print(len(blok_list))
# print(blok_list[0].strip('.'))


# print("------------------------------------------  task#1 Use methods startswith() for parsing elements of List ----------------------------------------------------------")
# queries = [
#     'Анфиса, сколько у меня друзей?',
#     'Андрей, ну где ты был?',
#     'Андрей, ну обними меня скорей!',
#     'Анфиса, кто все мои друзья?'
# ]
#
#
# def check_query(queries):
#     if queries.startswith('Анфиса'):
#         return 'запрос к Анфисе'
#     else:
#         return 'запрос к кому-то ещё'
#
#
# for q in queries:
#     result = check_query(q)
#     print(q, '-', result)


# print("-------  task#2 Use methods split() and strip() for parsing elements of List  -------------")
# queries = [
#     'Анфиса, сколько у меня друзей?',
#     'Андрей, ну где ты был?',
#     'Андрей, ну обними меня скорей!',
#     'Анфиса, кто все мои друзья?'
# ]
#
#
# def check_query(query):
#     tokens = query.split(',')
#     return tokens[1].strip(' ')
#
#
#
# for q in queries:
#     result = check_query(q)
#     print(q, '-', result)

# print("-------  task#3 Formatting strings in different ways and notice advantages of using \'f-string\'  -------------")
# def show_meteo(temperature, weather):
#     print('Сейчас ' + weather + ', на градуснике ' + str(temperature) + '.')
#     print(f'Сейчас {weather}, на градуснике {temperature}.')
#
# show_meteo(24, 'облачно')

# print("-------  task#4 Using \'f-string\' everywhere  -------------")
#
#
# def format_text(messages_count):
#     remainder = messages_count % 10
#     if messages_count == 0:
#         return 'нет новых сообщений'
#     elif remainder == 0 or remainder >= 5 or (10 <= messages_count <= 19):
#         return f'{messages_count} новых сообщений'
#     elif remainder == 1:
#         return f'{messages_count} новое сообщение'
#     else:
#         return f'{messages_count} новых сообщения'
#
#
# def print_count(messages_count):
#     text = format_text(messages_count)
#     print(f'У вас {text}')
#
#
# print_count(0)
# print_count(1)
# print_count(4)
# print_count(5)
# print_count(12)
# print_count(22)
# print_count(25)


# print("---------------------  task#5  Math calculations in f-strings-------------")
#
# five = 5
# ten = 10
# print(f'{five} + {ten} = {five + ten}')
#
# threehundred = 'threehundred'
# fifteen = 'fifteen'
# print(f'{threehundred} + {fifteen} = {threehundred + fifteen} miles')
#
# print("---------------------   task#6  Accessing the elements of the list-------------")
#
# russian_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
#                     'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
# print(f'{russian_alphabet[1]} - letter "b" in russian alphabet')
#
# print("---------------------   task#7  Referring to the elements of the dictionary by key -------------")
#
# favorite_songs = {
#     'Тополиный пух': 'Иванушки international',
#     'Город золотой': 'Аквариум',
#     'Звезда по имени Солнце': 'Кино'
# }
# song = 'Город золотой'
# song2 = 'Тополиный пух'
# print(f'"{song}" is a song of group "{favorite_songs[song]}"')
#
# print(
#     "---------------------  task#8  Using parameters, defined in declared function, as a variables in \'f-strings\' -------------")
#
#
# def print_time(hour, minute, second):
#     print(f'Now it is {hour}:{minute}:{second} o\'clock')
#     # аргумент должен содержать f-строку
#
#
# print_time('19', '28', '06')
#
# print("---------------------   task#9 Count items from list and print their amount using \'f-string\'  -------------")
#
#
# def calc_stat(listened):
#     N = 0
#     for i in listened:
#         N += 1
#     return f'Вы прослушали {N} песен.'
#
#
# print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))

# # print("---------------------   task#10 Display summary statistics, separately in minutes and seconds  -------------")
# #
# #
# # def calc_stat(listened):
# #     N = len(listened)
# #     T = 0
# #     for i in listened:
# #         T += i
# #     M = int(T / 60)
# #     S = T % 60
# #     return f'Вы прослушали {N} песен, общей продолжительностью {M} минут и {S} секунд.'
#
# print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))

