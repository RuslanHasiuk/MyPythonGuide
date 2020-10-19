import ModuleRandom

print('What\'s your name?')
name = str(input())
if name == 'Alex':
    print('Come in')
else:
    print('Wrong! Get out of here')

print('How old are you?')
age = int(input())
if age < 18:
    print('U are too small, baby')
elif age >= 45:
    print('U may drink, but be careful with dose')
else:
    print('Drink as much as U wanna')

print("How much money You've got?")
amount = 5
total = amount + int(input())
if total < 50:
    print("Your total is " + str(total) + ", you need earn more")
elif total > 55:
    print("Your total is " + str(total) + ", Wow you are reach boy")
else:
    print("Your total is " + str(total) + ", yes, that\'s okay")

print("-------------------------------------------------------------------")
print("------------ Control flow with using User's input --------")

current_hour = int(input())
if 0 <= current_hour < 12:
    print("Good morning")
elif 17 <= current_hour < 22:  # current_hour >= 17 and current_hour < 22:
    print("Good evening")
elif 22 <= current_hour <= 24:
    print("Good night")
elif current_hour > 24:
    print("Oops, no such hour at clock")
else:
    print("This is afternoon, sir!")

print("-------------------------------------------------------------------")
print("------------ Control flow with using Random package --------")

current_hour = ModuleRandom.randint(0, 25)
if 0 <= current_hour < 12:
    print("Good morning")
elif 17 <= current_hour < 22:  # current_hour >= 17 and current_hour < 22:
    print("Good evening")
elif 22 <= current_hour <= 24:
    print("Good night")
elif current_hour > 24:
    print("Oops, no such hour at clock")
else:
    print("This is afternoon, sir!")

print("-------------------------------------------------------------------")
print("------------ Control flow with using Loop For --------")

for current_hour in range(0, 26):
    print("Now is " + str(current_hour) + " o'clock")
    if 6 <= current_hour < 12:
        print("Good morning")
    elif 12 <= current_hour < 17:
        print("Good afternoon")
    elif 17 <= current_hour < 22:  # current_hour >= 17 and current_hour < 22:
        print("Good evening")
    elif current_hour <= 5 or current_hour >= 22:
        print("Good night")
    else:
        print("Oops, there is no such hour at clock")

print("-------------------------------------------------------------------")
print("------------ Control flow with using Loop For --------")
print(11 % 10)
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder == 0 or remainder >= 5 or 11 < messages_count <= 19:
        print('У вас ' + str(messages_count) + ' новых сообщений')
    else:
        print('У вас ' + str(messages_count) + ' новых сообщения')

print("-------------------------------------------------------------------")
print("---------------Compound Boolean Expressions---------------")
milk = True
cereals = False
eggs = not False

if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = '- омлет'
        else:
            breakfast = '- яичница'
    else:
        breakfast = '- хлопья с молоком'
else:
    if milk:
        breakfast = '- стакан молока'
    elif cereals:
        breakfast = 'можно погрызть сухих хлопьев'
    else:
        breakfast = 'ничего не будет: разгрузочный день'
print('Сегодня на завтрак', breakfast)
