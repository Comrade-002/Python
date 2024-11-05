#Built-In Library functions
y = max(34, 76, 23, 90)
print(y)

x = min(34, 76, 23, 90)
print(x)

z = pow(2,3)
print("The result is", z)


#User-Defined functions
def greeting():
    print("Hello there!")

greeting() #calling a function

def add():
    num1 = 7
    num2 = 3
    print(num1 + num2)

add()

#Parameter/-variable and Argument/-value
def multiply(x,y):
    print(x * y)
multiply(5,0)
multiply(3,0)
multiply(7,0)

def doctor(name):
    print(name)
doctor("mkuu")
doctor("Maish")
doctor("jonte")

