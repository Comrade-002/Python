try:
    print(number)

except:
    print("An error has occured")

num1 = 39
num2 = 0
try:
    print(num1 / num2)
except:
    print("A ZeroDivisionError has occured")
finally:
    print("Success")