#Ebcapsulation
'''
it is an phenomean of providing security to the data members present inside the class

it is also called as access specifier

Access specifiers is used to give the permission to the user weather they can access the properties or functionaties
outside the class is called as access specifiers.

there are 3 types of access specifier are prsent in python:
1. public access specifier
2. protected
3. private

1. public access specifier :-
- it is an access specifier which will allow the user to access the members outside the class
- what ever we are going to store inside the class , by default all the data members all methods will act as public access specifier

#syntax

class cname:
    var = values
    def mname(arg):
        |-----|
        | SB |
        |-----|

    @classmethods
    def mname(args):
        |-----|
        | SB |
        |-----|

    @staticmethod
    def mname(arg):
        |-----|
        | SB |
        |-----|


2. protected Access specifier:
- it is an access specifier which should provide security to the data members present inside the class
- the name it self represents as it will provide security to the data members but it will not provide any security
to the data members

syntax::

class _cname:
    _var = values
    def _mname(arg):
        |-----|
        | SB |
        |-----|

    @classmethods
    def _mname(args):
        |-----|
        | SB |
        |-----|

    @staticmethod
    def _mname(arg):
        |-----|
        | SB |
        |-----|


3. private access specifier
- it is an private access specifier which is used to proivde the security to the data members
present inside the class by using "__"

syntac::

class __cname:
    __var = values
    def __mname(arg):
        |-----|
        | SB |
        |-----|

    @classmethods
    def __mname(args):
        |-----|
        | SB |
        |-----|

    @staticmethod
    def __mname(arg):
        |-----|
        | SB |
        |-----|

# to access single property  ---> __cname._cname__pn
# to access class/object method ----> cname/ob._cname__mname()
'''

#WAP to create a class company having class members as cname, cloc,website and profit
#and profit as private access specifier and create six object menbers as ename,eid,esal,ephno,
#edes,eemail create an object access the class property and object members with class members

class Company:
    cname = 'qspider'
    cloc = 'ahmd'
    website = 'qspider@gmail.com'
    __profit = '7cr'

    def __emp(self, emp_name, emp_id, salary, phno, designation, email):
        self.emp_name = emp_name
        self.id = emp_id
        self.salary = salary
        self.phno = phno
        self.designation = designation
        self.email = email

    def __ch_emp_name(self,emp_name):
        self.emp_name = emp_ename
        self._Company__dis()

    def __ch_emp_id(self,emp_id):
        self.emp_id = emp_id
        self._Company__dis()

    def __ch_salary(self,salary):
        self.salary = salary
        self._Company__dis()

    @classmethod
    def get_profit(cls):
        return cls.__profit

    @classmethod
    def ch_cname(cls,cname):
        cls.cname = cname

    @classmethod
    def ch_cid(cls,cid):
        cls.cid = cid

    @classmethod
    def ch_website(cls,website):
        cls.website = website


    def display(self):
        print(Company.cname, Company.cloc, Company.website, Company.get_profit())

    def __dis(self):
        print(self.emp_name, self.id, self.salary, self.phno, self.designation, self.email)

ob1 = Company()
ob1.display()

ob1.ch_cname('Jspider')
ob1.display()

ob1._Company__emp('Dhaval', 101, 50000, '1234567890', 'DA', 'DDA@example.com')
ob1._Company__dis()

ob1._Company__ch_salary('40cr')
