import random
from random import randint
from random import choice

print(
    "------------------------------------ Use [Random] module for generation pseudo-random numbers --------------------------")
# official documentation - https://docs.python.org/3.6/library/random.html

print("-------------- Randomize float:  0.0 <= x < 1.0 -----------")
print(random.random())

print("-------------- Randomize integer in defined range, e.g. 9 <= x <= 19 -----------")
print(randint(9, 19))  # if we imported the function directly - we can not call library's name then
print(randint(40, 80))

print("-------------- Randomize float in defined range, e.g. 5.0 <= x < 8.5 -----------")
print(random.uniform(5, 8.5))

print("-------------- Shuffle a list -----------")
names = ['nina', 'andrew', 'Bob', 'Ross', 'Rachel']
random.shuffle(names)
print(names)

print("-------------- If U wanna randomize some single character from string,"
      " remember: define range properly! -----------")
string = 'abcde'
random_index = randint(0, len(string) - 1)
char = string[random_index]
print(char)

print("-------------- Single random element from a sequence -----------")
names_list = ['nina', 'andrew', 'Bob', 'Ross', 'Rachel']
name_list2 = ['Phil', 'Arnold', 'Jack', 'Roger']


def choose_name(names):
    return choice(names)


print(choose_name(names_list))
print(choose_name(name_list2))
