# print("------------implement some dialog with messenger bot v 1.0---------")
# for messages_count in reversed(range(1, 11)):
#     print("- Анфиса, есть ли новые письма?")
#     print("- Непрочитанных писем: " + str(messages_count))
#     print("Я прочитал одно, и их осталось:" + str(messages_count - 1))

# print("-------------------------------------------------------------------")
# print("------------implement some dialog with messenger bot v 2.0--------")
# messages_count = 11
# for i in reversed(range(1, messages_count)):
#     print("- Анфиса, есть ли новые письма?")
#     print("- Непрочитанных писем: " + str(i))
#     print("Я прочитал одно, и их осталось:" + str(i - 1))
# print("- Анфиса, есть ли новые письма?\n- Нет")
# print("Я прочитал все письма!")


# print("-------------------------------------------------------------------")
# print("------------ implement some dialog with messenger bot v 3.0--------")
#
# def count_messages():
#     messages_count = 10
#     for i in reversed(range(2, messages_count + 1)):
#         print('- Анфиса, есть ли новые письма?')
#         print("- Непрочитанных писем: " + str(i) + "." )
#         print("Я прочитал одно, и их осталось " + str(i - 1) + ".")
#     print('Я прочитал все. И нет больше писем!')
#
# count_messages()



# print("-------------------------------------------------------------------")
# print("------------ calculate SUM of all the parameters in the list--------")
#
# areas = [
#     5.38, 21.72, 7.78, 26.86, 5.75,
#     29.84, 22.67, 5.50, 16.85, 4.52
# ]
#
# area_start = 0
# for area in areas:
#     area_start += area
#
# print('Sum is ', area_start)


print("-------------------------------------------------------------------")
print("------------ Calculate How many albums the music group"
      " \'Depeche Mode\' has released in the 21st century?! --------")

years = [
    1981, 1982, 1983, 1984, 1986, 1987, 1990,
    1993, 1997, 2001, 2005, 2009, 2013, 2017
]


count = 0
for album in years:
    if album > 2000:
        count += 1
print("Total number of albums in 21st century = ", count)

print("------------ Important! It depends where the variable is initialized : "
      "within Function(locally) OR globally - it impacts final output !!! --------")

for i in years:
    amount_of_albums = 0
    if i > 2000:
        amount_of_albums += 1
print("Total number of albums in 21st century = ", amount_of_albums)


print("-------------------------------------------------------------------")
print("------------ calculate_sum_of_params_of_list --------")


areas = [
    5.38, 21.72, 7.78, 26.86, 5.75,
    29.84, 22.67, 5.50, 16.85, 4.52
]

def calculate_sum_of_params_of_list():
    area_start = 0
    for i in areas:
        area_start = area_start + i
    print("Sum is ", area_start)


calculate_sum_of_params_of_list()
