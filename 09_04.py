class SocialMedia:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_credentials(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

class Facebook(SocialMedia):
    def post_status(self):
        print(f"{self.username} Facebook.")

class Instagram(SocialMedia):
    def post_story(self):
        print(f"{self.username}  Instagram.")

class Twitter(SocialMedia):
    def tweet(self):
        print(f"{self.username}  Twitter.")

fb_user = Facebook("dhaval", "dhaval123")
insta_user = Instagram("shlok__00_0", "S$M")
twitter_user = Twitter("dha_v", "twpass456")

fb_user.display_credentials()
fb_user.post_status()

print()

insta_user.display_credentials()
insta_user.post_story()

print()

twitter_user.display_credentials()
twitter_user.tweet()


print("*"*79)


#hybrid:
'''
- if we combine more than 1 type of inheritance than we can say it as hybrid inheritence.
- hybrid ineritence is done based upone user requirement so because of this we do not have
proper flow diagram of hybrid inheritence .

    ----
    | A |
    ----
      |
    ----                ----
    | B |                | C |
    ----                ----
      |                      |
      |          ----      |
      |___     | D |____|
                ----
'''

#a - school name
#b - teacher name
#c - parent name
#d - student name

class School():
    def show(self,sn):
        self.sn = sn
        print(self.sn)

class Teacher(School):
    def show_T(self,tn):
        self.tn = tn
        print(self.tn)

class Parent():
    def show_P(self,pn):
        self.pn = pn
        print(self.pn)

class Student(Teacher, Parent):
    def __init__(self,ssn):
        self.ssn = ssn
        print(self.ssn)

ob1 = Student("Dhaval")
ob1.show("Qspdier")
ob1.show_P("(* _ *)")
ob1.show_T("Karan")

print("*"*79)

#hybrid
class A:
    def show (self):
        print ("This ia claso A")
class B (A) :
    def show_b (self) :
        print ("This la class B")
class C(A) :
    def show_c (self) :
        print ("This is class C")
class D(B, C): 
    def show_d (self) :
        print ("This is class D")

obj = D()
obj.show()
obj.show_b()
obj.show_c()
obj.show_d()

print("-"*79)

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")

class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color

    def display_mammal_info(self):
        self.display_info()
        print(f"Fur Color: {self.fur_color}")

class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span

    def display_bird_info(self):
        self.display_info()
        print(f"Wing Span: {self.wing_span} meters")

class Bat(Mammal, Bird):
    def __init__(self, name, species, age, fur_color, wing_span, is_night_flying):
        Animal.__init__(self,name,species,age)
        self.fur_color = fur_color
        self.wing_span = wing_span
        self.is_night_flying = is_night_flying

    def display_bat_info(self):
        self.display_info()
        print(f"Fur Color: {self.fur_color}")
        print(f"Wing Span: {self.wing_span} meters")
        print(f"Night Flying: {'Yes' if self.is_night_flying else 'No'}")

bat = Bat("shlok", "Bat", 21, "black_white", 1.5, False)
bat.display_bat_info()

print("-"*79)


class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, team_size):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_developer_info(self):
        self.display_employee_info()
        print(f"Programming Language: {self.programming_language}")


class Intern(Employee):
    def __init__(self, name, employee_id, salary, duration):
        super().__init__(name, employee_id, salary)
        self.duration = duration  

    def display_intern_info(self):
        self.display_employee_info()
        print(f"Internship Duration: {self.duration} months")


print()
mgr = Manager("Dhaval", "Q103", 95000.0, "IT", 10)
mgr.display_manager_info()

print()
dev = Developer("shloki", "Q101", 75000.0, "Python")
dev.display_developer_info()

print()
intern = Intern("Shlok", "I501", 15000.0, 6)
intern.display_intern_info()
