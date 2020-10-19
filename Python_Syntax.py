print("---------------------------------------------------------------")
print("How to use quotes within another quotes?! - by using backslash \'(\)\'")
print("This state was named \'Caroline\'")
print("---------------------------------------------------------------")
print("How to jump to the next row? ")
print("There were 3 brothers:\n Dilan,\n Brandon and\n Kevin")
print("---------------------------------------------------------------")
print("How to use backslash as a separate character? - double backslash ")
#Для включения буквального значения обратного слэша, исключите его с помощью еще одного:
print('foo\\bar')
print("---------------------------------------------------------------")
print("horizontal tab character")
print("#1: I\'ve got\t animal")
print("#2 This is\n \t a dog")
print("---------------------------------------------------------------")
print("page break symbol")
#символ разрыва страницы
print("---------------------------------------------------------------")
print("Unicode character named <name>")
# \N{<name>} → Символ из базы Unicode с именем <name>
print("\N{rightwards arrow}")
print("---------------------------------------------------------------")
print("Unicode character with 16-bit hex value")
#\uxxxx	Символ Unicode с 16-битным шестнадцатеричным значением
print('\u2192')
print("---------------------------------------------------------------")
print("Triple quoted strings")
# Строки в тройных кавычках определяют группами из трех одинарных или двойных кавычек.
# Исключенные последовательности в них все еще работают, но одинарные и двойные кавычки,
# а также новые строки могут использоваться без управляющих символов.
# Это удобный способ создавать строки, включающие
print(''''This string contains single (') and double (") quotes. ''')
print("---------------------------------------------------------------")
print("Mixing different rules:")
print(" it is: \n \t \\page1\n \t \\page2 ")
print("--------------------------------------------------------")
print("\t\t\t\t\t\t\t\t\t[Python Casting]")
amount = 5
print(type(amount))
print("int → float")
print(float(amount))
print("-------------------------------------------------")
amount2 = 105.5
print(type(amount2))
print("float → int")
print(int(amount2))
print("---------------------------------------")
am3 = 7
print(type(am3))
print("int → String")
am3st = str(am3)
print(type(am3st))
print("------------------------")
am4 = 7.65
print(type(am4))
print("float → String")
am4fl = (str(am4))
print(type(am4fl))
print("---------------")
somestring = '4565'
print(type(somestring))
print("string→ int")
string_to_int = int(somestring)
print(string_to_int)
print(type(string_to_int))
print("int→ float")
int_to_float = float(string_to_int)
print(int_to_float)
print(type(int_to_float))
