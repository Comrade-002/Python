#

number = 67 #Integer
second = 45.98 #Float
greeting = "Hello there" #String
IsPythonInteresting = False #Boolean

#Data Structures - multiple values stored in a single variable
cars = ["toyota","nissan","vw"] #List - Ordered and changeable
fruits = ("banana","mango","apple") #Tuple - Ordered but unchangeable
countries = {"Jamaica","Tunisia", "Algeria"} #Set - Unordered and unchangeable
student = {
    "firstname":"Jane",
    "age":25,
    "course":"Web Dev",
    "gender":"Female"
} #Dictionary - Key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["gender"])

print(greeting)
print(IsPythonInteresting)

#Determining a datatype
print(type(countries))
print(type(student))

#Typecasting - converting from one datatype to another
print(float(number))
print(int(second))


