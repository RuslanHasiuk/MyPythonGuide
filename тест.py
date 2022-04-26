# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]


# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
#
# two_dim_list = zip(students_period_A, students_period_B)
# print(list(two_dim_list))
#
# combined_list = students_period_B + students_period_A
# print(combined_list)
#
#
#
#
#
# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
#
#
# stud_A = []
# for i in students_period_A:
#     i += 'is'
#     stud_A += i.split()
#
# stud_A = [name + 'is' for name in students_period_A]
# print(stud_A)



# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
#
# students_period_B = students_period_A + students_period_B
# print(students_period_B)

# for student in students_period_A:
#   students_period_B = (students_period_B + student.split())
# print(students_period_B)

# for women in students_period_B:
#     if women == 'Alex' or women == 'Obie':
#         continue
#     print(women)

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
#
# for blocks in items_on_sale:
#     print(blocks)
#     for items in blocks:
#         if items == 'striped socks':
#             continue
#         print(items)




# for one_item in items_on_sale:
#     print(one_item)
#     if one_item == "knit dress":
#         print('Found it')
#         break


big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
#
items_and_number = zip(items_on_sale, big_number_list)

print(list(items_and_number))
# modified_list = [element + 5 for element in big_number_list]
# print(modified_list)
# list_of_positive_items = 0
#
#
# for i in big_number_list:
#     if i <= 0:
#         continue



# sum_of_elements = 0


# print('-------------- Nested Loops ----------------')
# for regions in sales_data:
#     print('Region: ', regions)
#     for elements in regions:
#         print('elements:', elements)
#         sum_of_elements += elements
#     print('Sum of elements for each region:', sum_of_elements)
# print('Total of elements: ', sum_of_elements)


# Output:
# Region:  [12, 17, 22]
# elements: 12
# elements: 17
# elements: 22
# Sum of elements for each region: 51
# Region:  [2, 10, 3]
# elements: 2
# elements: 10
# elements: 3
# Sum of elements for each region: 66
# Region:  [5, 12, 13]
# elements: 5
# elements: 12
# elements: 13
# Sum of elements for each region: 96
# Total of elements:  96
