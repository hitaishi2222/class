class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def registration_class(self):
        if self.age <= 10:
            return("your class is 7th std")
        elif self.age <= 12:
            return("your class is 9th std")
        else:
            return("your class is 10th std")
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, class: {self.registration_class()}"

class Science_student(Student):

    def __init__(self, name, age, branch):
        self.branch = branch
        Student.__init__(self, name, age)

class History_student(Student):

    def __init__(self, name, age, branch):
        self.branch = branch
        Student.__init__(self, name, age)



mary = Student("mary", 10)
rob = History_student("rob", 12, "History")
vicky = Science_student("vicky", 13, "PCM")

print(rob.registration_class())