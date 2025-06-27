'''
create  a class called laptop
having 3 class pro.
and create 3 object
with 3 object methods
and 3 class method
and 1 satic method
'''

class Laptop:
    lcompany = 'Dell'
    lprise = '7cr'
    lcolour = 'Black'

    def __init__(self,ram,prc,storage):
        self.ram = ram
        self.prc = prc
        self.storage = storage

    def disp(self):
        print(self.ram,self.prc,self.storage)

    def ch_ram(self,new):
        self.ram = new
        self.get()
        self.disp()

    def ch_prc(self,new):
        self.prc = new
        self.get()
        self.disp()

    def ch_storage(self,new):
        self.storage = new
        self.get()
        self.disp()

    @classmethod
    def display(cls):
        print(cls.lcompany,cls.lprise,cls.lcolour)

    @classmethod
    def ch_company(cls,new):
        cls.lcompany = new
        cls.get()
        cls.display()

    @classmethod
    def ch_prise(cls,new):
        cls.lprise = new
        cls.get()
        cls.display()

    @classmethod
    def ch_colour(cls,new):
        cls.lcolour = new
        cls.get()
        cls.display()

    @staticmethod
    def get():
        print('updated values')

ob1 = Laptop(8,'i3',512)
ob2 = Laptop(16,'i11','1TB')
ob3 = Laptop(4, 'i5', 256)

Laptop.display()

print()

ob1.ch_company('aaple')
ob1.disp()
ob1.ch_ram(16)

print()

ob2.ch_prise('25cr')
ob2.disp()
ob2.ch_prc('i512')

print()

ob3.ch_colour('GOLding')
ob3.disp()
ob3.ch_storage('40cr')
