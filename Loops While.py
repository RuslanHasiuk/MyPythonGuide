# Вивести всі числа непарні числа від 100 до 140 (включно) , після цього ключового слова - [continue] - код ігнорується
# Print all odd numbers from 100 to 140 (inclusive), after this keyword - [continue] - the code is ignored
number = 99
while number < 140:
    number += 1
    if (number % 2) == 0:
        continue
    print("LIne № " + str(number))


# Or another way:
range_from100_to140inc = range(101, 141, 2 )
print(list(range_from100_to140inc))

вивести всі числа від 40 до 50
number = 40
while number >= 40:
    if number > 50:
        break
    print(number)
    number += 1



