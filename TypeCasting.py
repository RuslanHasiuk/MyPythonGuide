agE = 30.8
print(type(agE))
print(agE)
print("---------")
print("Typecasting: from float to integer -- it cuts everything after floating point and leaves ONLY what is Before it")
print(int(agE))
print("-------------------------------------------------")
print("Casting [string - float - int - string]")
temperature_exact = '39.3'  # (жара)
temperature_approx = int(float(temperature_exact))  # преобразуйте значение в целое и прибавьте 1
print("За окном " + temperature_exact + " градусов Цельсия. Это почти " + str(temperature_approx))

