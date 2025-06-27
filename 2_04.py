#create a class caled company having 5 class member and create 5 object with 5 object member

class Company:
    cname = 'qspider'
    cloc = 'ahmd'
    cec = 15
    cphno = 1122334455
    cemail = 'aa@gmail.com'

    def __init__(self,name,sex,age,phno,email):
        self.name = name
        self.sex = sex
        self.age = age
        self.phno = phno
        self.email = email

    def dis(self):
        print(self.name,self.sex,self.age,self.phno,self.email)

    @classmethod
    def display(cls):
        print(cls.cname,cls.cloc,cls.cec,cls.cphno,cls.cemail)


Company.display()
e1 = Company('dhaval','M',21,1020102,'aa@ggg')
e1.dis()

print()
print('*'*10)
print()

#create a class gaving HOME with 5 class member and 4 object with 5 members and change atleast 3 object

class Home:
    hname = 'ah'
    hloc = 'ahmd'
    hfloor = 3
    hrooms = 6
    hstatus = 'permanent'

    def __init__(self,name,sex,age,phno):
        self.name = name
        self.sex = sex
        self.age = age
        self.phno = phno

    def dis(self):
        print(self.name,self.sex,self.age,self.phno)

    def ch_name(self,new):
        self.name = new
        self.dis()

    def ch_sex(self,new):
        self.sex = new
        self.dis()

    def ch_age(self,new):
        self.age = new
        self.dis()

    @classmethod
    def display(cls):
        print(cls.hname,cls.hloc,cls.hfloor,cls.hrooms,cls.hstatus)

    @classmethod
    def ch_hname(cls,new):
        cls.hname = new

    @classmethod
    def ch_hfloor(cls,new):
        cls.hfloor = new


Home.display()
p1 = Home('dhaval','M',21,1020102)
p1.dis()

p1.ch_name('shlok')
p1.ch_sex('F')
p1.ch_age(99)

p1.ch_hname('zzzzzzzz')
p1.ch_hfloor(11)

p1.display()
