courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#Accessing an element in an array
print(courses[1])

#Looping through an element
for y in courses:
    print("Course is",y)

#Adding a new element
courses.append("web development")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)
