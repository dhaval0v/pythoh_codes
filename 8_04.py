'''
write a program that dem. multilevel inheritence consider a person classs as
a grant parent class,a student classs as an parent class and graduat student as child class
the person class shuod have attribute name and age
the student class have an additional attribute as student_id
and the gresuat student class should have some additional attrivute as thesis
'''

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        self.display_person_info()
        print(self.student_id)

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis):
        super().__init__(name, age, student_id)
        self.thesis = thesis

    def display_graduate_info(self):
        self.display_student_info()
        print(self.thesis)


grad_student = GraduateStudent("Divyesh", 21, "D00101", "Soa ja bachhe")
grad_student.display_graduate_info()
'''



'''
Multiple level  : it is a phenomena of derived the properties from multiple
parent class to single child class
'''

 
class Father:
    def skills(self):
        print("Gardening , Programming")

class Mother:
    def skills(Self):
        print("Cooking , Art")

class Child(Father , Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

child = Child()
child.skills()



print("*"*79)

class addi:
    def additon(a,b):
        return a + b

class sub:
    def subb(a,b):
        return a-b

class mul:
    def mull(a,b):
        return a*b


class div:
    def divv(a,b):
        return a/b


class calc(addi,sub):
    def inning(self):
        a , b = int(input()),int(input())
        print(addi.additon(a,b))
        print(sub.subb(a,b))
        print(sub.subb(a,b))
        print(div.divv(a,b))


calc1= calc()
calc1.inning()


#note =
'''
we can acess the properties from parent class using child class name
'''
#create a parent class called social media where that attribute will be user name and password.
#create child class facebook,instagram,twiter and inherit the social media class.
