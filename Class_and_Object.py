class AnimalsParams:
    home = 'wood'
    maxAge = 20

    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height


lion = AnimalsParams(5, 'LionSimba', 1.45)
#create attribute specifically for some object
lion.father = 'King'
print("height is " + str(lion.height))
print("age is " + str(lion.age))
print(lion.name)
print("home is " + str(lion.home))
print("father is " + str(lion.father))
print(dir(lion))
print(lion.__dict__)

print("------------")

elefant = AnimalsParams(10, 'ElefantStar', 2.88)
print("height is " + str(elefant.height))
print("age is " + str(elefant.age))
print(elefant.name)
print("home is " + str(elefant.home))
print("It is impossible to use attribure \'father\' for object \'elefant\' because it was created only for object \'lion\'")
# AttributeError will be displayed in attempt to use attribure \'father\' for object \'elefant\'
# print(elefant.father)

print("------------")

print(dir(elefant))