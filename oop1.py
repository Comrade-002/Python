class Person:
    #Properties/Variables/Attributes/Characteristics
   def __init__(self, name,age,gender):
     self.name = name
     self.age = age
     self.gender = gender
   #Behaviour/Method/Function
   def study(self):
        print("Student is studying")

#Creating an object
student1 = Person("Hussein", 23, "male")
print(student1.name, student1.age, student1.gender)
student1.study()

student2 = Person("Amina", 24, "female")
print(student2.name, student2.age, student2.gender)
student2.study()

student3 = Person("Alex", 25, "male")
print(student3.name, student3.age, student3.gender)
student3.study()