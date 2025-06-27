'''
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__balance = 0

    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount

    def deduct_balance(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

class Customer(User):
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address

    def make_purchase(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            self.deduct_balance(amount)
            print(f"{self.username} made a purchase of {amount}")
            return amount
        else:
            print(f"{self.username} has insufficient balance for this purchase.")
            return 0

class Seller(User):
    def __init__(self, username, email, store_name):
        super().__init__(username, email)
        self.store_name = store_name

    def receive_payment(self, amount):
        if amount > 0:
            self.add_balance(amount)
            print(f"{self.username} received a payment of {amount}")

customer1 = Customer("Shlok", "shlok@gmail.com", "Ahmedabad")
seller1 = Seller("Dhaval", "dhaval@gmail.com", "Vala's Bhajiya House")

customer1.add_balance(500)
purchase_amount = customer1.make_purchase(300)
if purchase_amount > 0:
    seller1.receive_payment(purchase_amount)

print(f"{customer1.username}'s final balance: {customer1.get_balance()}")
print(f"{seller1.username}'s final balance: {seller1.get_balance()}")
'''

#polymorphism
'''
- it is an phenomeanan of using same method name or same operator to work on
two or more diff operation
- polymorphism can be explain in two ways
 1. method overloading
 2. operator oeverloading

 1. method overloading
 - it is an phenomeanan of using same method name to perform two or more
 diff. opration.
 - in another programming lan. it is posible to perform method overloading but when
 it come to python , here method will override the another method.

 -- method overriding:
 -> it is an phenomeanan of using same function name to perform multiple task
 or diff operation.

 exa:
 def add(a,d):
     print(a+b)
 def add(a,b,c):
     print(a+b+c)
 def add(a,b,c=0,d=0):
     print(a+b+c+d)
 add(10,10,10)


    main      |       method sapce
----------------------------------------
                 |
                 |        0x11
                 |       ---------------
                 |       | print(a+b) |
                 |       ---------------

     add       |
    -------    |
    |0x11|   |
    -------    |
                |



def add(a,d):
     print(a+b)
temp1 = add
def add(a,b,c):
     print(a+b+c)
temp2=add
def add(a,b,c=0,d=0):
     print(a+b+c+d)
temp3 = add
temp1(10,10)
temp2(10,10,10)
temp3(10,10,10,10)

- to perform method overrding wwe will use 2 ways
1. by providing default arg.
2. by storing the funcationality in a container.


(2) operator overloading
- it is an phn. of meking a operator to work on objects or user def. class or user
def. datatype by invoking magical methods

exa.

'''
class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a + other.a

ob1 = A('hello  ')
ob2 = A('shlok gathedi che')
print(ob1+ob2) # __add__()


#WORD FILE
class Arithematic:
    def __init__(self, a) :
        self.a=a
    def __add__(self, other) :
        return self.a + other.a
    def __sub__(self, other) :
        return self.a-other.a
    def __mul__(self, other) :
        return self.a*other.a
    def __truediv__(self, other):
        return self.a/other.a
    def __floordiv__(self, other):
        return self.a//other.a
    def __mod__(self,other):
        return self.a%other.a
    def __pow__(self,other):
        return self.a ** other.a

ob1 = Arithematic(10)
ob2 = Arithematic(20)

print("Addition:", ob1 + ob2)
print("Subtraction:", ob1 - ob2)
print("Multiplication:", ob1 * ob2)
print("True Division:", ob1 / ob2)
print("Floor Division:", ob1 // ob2)
print("Modulus:", ob1 % ob2)
print("Power:", ob1 ** ob2)


print("-"*79)

class Bitwise:
    def __init__(self,a):
        self.a = a
    def __and__(self,other):
        return self.a&other.a
    def __or__(self,other):
        return self.a|other.a
    def __invert__(self):
        return ~self.a
    def __xor__(self,other):
        return self.a^other.a
    def __lshift__(self,other):
        return self.a<<other.a
    def __rshift__(self,other):
        return self.a>>other.a

ob1 = Bitwise(10)
ob2 = Bitwise(20)
print(ob1^ob2)


print("-"*79)
class Relational:
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return self.a == other.a

    def __ne__(self, other):
        return self.a != other.a

    def __gt__(self, other):
        return self.a > other.a

    def __lt__(self, other):
        return self.a < other.a

    def __ge__(self, other):
        return self.a >= other.a

    def __le__(self, other):
        return self.a <= other.a



ob1 = Relational(10)
ob2 = Relational(20)

print("Equal:", ob1 == ob2)         
print("Not Equal:", ob1 !=ob2)     
print("Greater Than:", ob1 >ob2)  
print("Less Than:", ob1 < ob2)   
print("Greater or Equal:", ob1 >= ob2) 
print("Less or Equal:", ob1 <= ob2)    


