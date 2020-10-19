# Для определения функции нужно всего лишь написать ключевое слово def перед ее именем,
# а после — поставить двоеточие.
# Следом идет блок инструкций.
# Последняя строка в блоке инструкций может начинаться с return, если нужно вернуть какое-то значение.
# Если инструкции return нет, тогда по умолчанию функция будет возвращать объект None. Как в этом примере:


# def increment(i):
#     while i < 6:
#         print(i)
#     i += 1
# increment(6)

# Функция инкрементирует глобальную переменную i и возвращает None (по умолчанию).

# Еще
# Функцию можно записать в одну строку, если блок инструкций представляет собой простое выражение:
# #
# def sum(a, b): return a + b
# Функции могут быть вложенными:
#
# def func1(a, b):
#
#     def inner_func(x):
#         return x*x*x
#
#     return inner_func(a) + inner_func(b)
# Функции — это объекты, поэтому их можно присваивать переменным.

# Аргументы и параметры
# В функции можно использовать неограниченное количество параметров, но число аргументов должно точно соответствовать параметрам.
# Эти параметры представляют собой позиционные аргументы.
# Также Python предоставляет возможность определять значения по умолчанию, которые можно задавать с помощью аргументов-ключевых слов.
#
# Параметр — это имя в списке параметров в первой строке определения функции.
# Он получает свое значение при вызове.
# Аргумент — это реальное значение или ссылка на него, переданное функции при вызове. В этой функции:

# def sum(x, y):  # x, y — параметри
#     c = x + y
#     print(c)
#
# sum(10, 56)  # 10 і 7 — аргументи


print("-------------------------------------------------------------------")
print("------------ When we have global and local variables with the same name - "
      "global variable is not affected after the that local is initialized-----------------")

name = 'Oleg'


def say_name():
    name = 'Misha'
    print(name)


say_name()  # prints value of local  variable, cauze within called function there is such initialized variable 'name'
print(name)  # print value of global variable, cauze now we are using general function that uses variable 'name'
# not form local scope of function 'say_name', but global one


print("-------------------------------------------------------------------")
print("------------ When we have want global variable to store the same value "
      "as it has similar  local variable - we should use key word \'global\'----------------")

job = 'boxer'


def job_title():
    global job
    job = 'wrestler'
    print(job)


job_title()
print(job)

print("-------------------------------------------------------------------")
print("------------ manipulation with access to variables bu using \'nonlocal\' keyword----------------")


x = 10

def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное x сменилось на', x)


func_outer()
print(x)
