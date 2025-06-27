'''create a class called as animal having 3 class members
and derived the propertied into child class called donkey
and create 3 class member on the child class try to access the pro. pa to chi'''

'''
def line():
    print('-'*79)

class Animal:
    aname = 'Donkey'
    acolour = 'black'
    afood = 'herbivorus'

class donkey(Animal):
    dname = 'shlok'
    dage = 20
    dchild = 2

ob1 = donkey()
print(ob1.aname)
print(ob1.dname)
'''

class Bank:
    bname = 'SBI'
    bloc = 'Ahmedabad'
    bphno = 9876239866
    bmail = 'SBI@gmail.com'

    def __init__(self, name, phno, addr):
        self.name = name
        self.phno = phno
        self.addr = addr

    def disp(self):
        print(self.name, self.phno, self.addr)

    def ch_phno(self, new):
        self.phno = new
        print(f'The new phone number is: {self.phno}')

    def ch_addr(self, new):
        self.addr = new
        print(f'The new address will be: {self.addr}')

    @classmethod
    def display(cls):
        print(cls.bname, cls.bloc, cls.bphno, cls.bmail)


class Bank_updated(Bank):
    def __init__(self, name, phno, addr, email, pan, aadhar):
        super().__init__(name, phno, addr)
        self.email = email
        self.pan = pan
        self.aadhar = aadhar

    def disp(self):
        super().disp()
        print(self.email, self.pan, self.aadhar)

    def ch_addr(self, new):
        super().ch_addr(new)



cus1 = Bank_updated('A', 9987678878, 'down to earth', 'alemail.com', 10001, '111-222-333')


cus1.disp()


cus1.ch_addr('near to god')
###

'''
constructer chainning:
it is the process of calling the constuctor of parrent class in constructor in child class

syntax():
super().__init__(arg)
super(c_class,self).__init__(args)
p.class.__init(self,arg)

method chaining:
1. super().mnane()
2.super(c_class,self/cls).method_name(arg)
3.p_class.method_name(self/cls,arg)

it is a phenomenon of calling the method of parent calss in the method of child class
'''
