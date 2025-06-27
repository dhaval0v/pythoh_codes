'''
class Hospital:
    
    hospital_name = "Civil Hospital"
    location = "Ahmedabad"
    total_beds = 200
    total_doctors = 50
    total_nurses = 100

    def __init__(self, patient_name, patient_age, patient_disease, patient_room):
       
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_disease = patient_disease
        self.patient_room = patient_room


    def display_info(self):
        print(Hospital.hospital_name, Hospital.location)
        print(Hospital.total_beds, Hospital.total_doctors, Hospital.total_nurses)
        print(self.patient_name, self.patient_age, self.patient_disease, self.patient_room)
        print("-" * 50)




patient1 = Hospital("Dhaval", 21, "Kidney stone", 101)
patient2 = Hospital("Dhruvi", 20, "Fever", 202)
patient3 = Hospital("Shlok", 22, "Flue", 303)


patient1.display_info()
patient2.display_info()
patient3.display_info()


Hospital.hospital_name = "Shlokibenen"
Hospital.location = "Uptown"
Hospital.total_beds = 300
Hospital.total_doctors = 75
Hospital.total_nurses = 150


patient1.patient_name = "Alice Brown"
patient1.patient_age = 31
patient1.patient_disease = "Cold"
patient1.patient_room = 102

patient2.patient_name = "Bob Smith"
patient2.patient_age = 46
patient2.patient_disease = "Sprain"
patient2.patient_room = 203

patient3.patient_name = "Charlie Johnson"
patient3.patient_age = 61
patient3.patient_disease = "Hypertension"
patient3.patient_room = 304


patient1.display_info()
patient2.display_info()
patient3.display_info()
'''

'''
#Program
class Bank:
    bname = 'civil hospital'
    bloc = 'ahmedabad'
    bphno = 1234567890

    def __init__(self,name,loc,age,phno,email):
        self.name = name
        self.loc = loc
        self.age = age
        self.phno = phno
        self.email = email

    def dis(self):
        print(self.name,self.loc,self.age,self.phno,self.email)

    def ch_phno(self,new):
        self.phno = new

    @classmethod
    def display(cls):
        print(cls.bname,cls.bloc,cls.bphno)

    @classmethod
    def ch_bphno(cls,new):
        cls.bphno = new

c1 = Bank('a','ahme',12,10101,'a@gnaukmcon')
c1.display()
c1.dis()
'''

'''
class Bank:
    bname='icici'
    bloc= 'ahmedabad'
    bmail='icici@emai1.com'
    bph_no=998127890
    website='www.icici.com'
    def __init__(self, name, phno, aadhar, panno, mail, bal=500) :

        self. name=name
        self. phno=phno
        self.aadhar=aadhar
        self. panno=panno
        self.mail=mail
        self.bal=bal

    def disp (self) :
        print (self .name, self.phno, self.aadhar, self.panno, self.mail, self.bal)

    def ch_phno (self,new):
        self.phno = new

    def withdraw(self,amt):
        if amt > self.bal:
            print('ins bal')
        else:
            self.bal = self.sub(self.bal,amt)

    def diposit(self,amount):
        self.bal = self.add(self.bal,amt)


    @classmethod
    def display (cls):
        print(cls.bname,cls.bloc,cls.bmail,cls.bph_no,cls.website)

    @classmethod
    def ch_bmail(cls):
        cls.bmail = cls.get_mail()
        #or
        #cls.bmail=input('enter the new mail: ')



    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def get_mail():     
        return input('enter new email: ')

    


c1=Bank('A', 1111,1001,1010, 'A@gmail.com')
c2=Bank('B', 2222,1002,2020, 'B@gmail.com')

c1.display()
c1.disp()

c1.withdraw(200)
c1.disp()

c1.ch_bmail()
c1.display()
'''

'''WAP to create a class called as school and create 5 class
properties or member and create 2 object and 5 object members
where we will be working with respect to finace department
#fee deposit
'''



class School:
    school_name = "Excel Academy"
    school_location = "Ahmedabad"
    school_email = "admin@excelacademy.com"
    school_phone = 9876543210
    school_website = "www.excelacademy.com"

    def __init__(self, student_name, student_grade, fees_paid, total_fees, parent_contact):
        self.student_name = student_name
        self.student_grade = student_grade
        self.fees_paid = fees_paid
        self.total_fees = total_fees
        self.parent_contact = parent_contact

    def display_student_info(self):
        print(self.student_name, self.student_grade, self.fees_paid,self.total_fees,self.parent_contact)

    def pay_fees(self, amount):
        if amount <= 0:
            print("Invalid fee amount!")
        else:
            self.fees_paid += amount
            print(self.fees_paid)
            

    def calculate_outstanding_balance(self):
        return self.total_fees - self.fees_paid

    @classmethod
    def display_school_info(cls):
        print(cls.school_name, cls.school_location, cls.school_email, cls.school_phone, cls.school_website)

    @classmethod
    def update_school_email(cls, new_email):
        cls.school_email = new_email
        print(cls.school_email)


student1 = School("Dhval", "10th", 5000, 8000, "dhaval_parent@example.com")
student2 = School("shlok", "12th", 6000, 10000, "shlok_parent@example.com")

School.display_school_info()

student1.display_student_info()
student2.display_student_info()

student1.pay_fees(2000)

student2.pay_fees(4000)
