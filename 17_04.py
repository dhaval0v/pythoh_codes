''' for functions:-
syntax:
func. declaration:
    func. defination
calling func.
'''

#abstraction
'''
-> it is an phn. of hiding the implementation and showing the
funcationality from the user.

-> to work with abstraction we should know about three things:
1. abstract method :- only fun. declaration
2. abstract class :- including the abstract methods is known as ..
3. concreate class :- not including abstract method and class

1. abstract method:
-> if a class consist of function declaration but not function defination
is called as abstract method.
exa:-
def demo():
    pass

####

2. abstract class
-> if a class consist of any one abstract method then that class
will be consider as abstract class.
exa:
class Ex:
    def demo():
        pass
#####


3. concrete class:
-> if a class dosen't contain neither abstract method nor abxtract class
that is called as concrete class
'''

'''
To make use of abstract methof we have to import
abstract base class
:- from abc import ABC,abstractmethod

->if we want to create any objects in abstract class then it is not possible
->to create any object we will inherite the abstract class to diff class
and then we will create object
'''


from abc import ABC,abstractmethod

class Demo(ABC):
    @abstractmethod
    def example():
        pass

class inheri(Demo):
    def example(self):
        print('Noooo')

ob1 = inheri()
ob1.example()

'''
1. Create an abstract class PaymentPethod with:
• An abstract method pay(ount) that each subclass must implement.
2. Create three subclasses of Pay eithethod:
* ﻿﻿Creditcard: implements pay() by printing a message simulating a credit card payment.
* ﻿﻿Paypal: implements pay() with a message simulating PayPal.
* ﻿﻿UPI: implements pay() with a message simulating UPI.
1. ﻿﻿﻿Write a function process_payment (payment sethod, anount) that takes an object of type PaymentMethod and calls its payC, method.
2. ﻿﻿﻿Demonstrate abstraction by creating objects of each subclass and passing them to process payment) to simulate different types of payments.
'''

from abc import ABC, abstractmethod

# Abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete subclasses
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Processing credit card payment of ₹{amount}")
        print('Payment successful using credit card')

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")
        print('Payment successful using Paypal')

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")
        print('Payment successful using UPI')

# Function to process a payment
def process_payment(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)

# Test the system with different payment methods
credit_card_payment = CreditCard()
paypal_payment = PayPal()
upi_payment = UPI()

process_payment(credit_card_payment, 500)
print()
process_payment(paypal_payment, 300)
print()
process_payment(upi_payment, 150)

'''
-> To call an object inside the function we are making use of
'Type Hinting'  exa.: 'payment_method: PaymentMethod'
 
'''

print('-'*79)

from abc import ABC,abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def employee_info(self):
        print("Employee Type: ")


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary + 700000000000

    def employee_info(self):
        print(f"Employee Type: Full-Time, Name: {self.name}")


class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate * 1000

    def employee_info(self):
        print(f"Employee Type: Part-Time, Name: {self.name}")


full_time_emp = FullTimeEmployee("Dhaval", 50000)
part_time_emp = PartTimeEmployee("Shlok", 80, 300)

full_time_emp.employee_info()
print("Salary:", full_time_emp.calculate_salary())

print()

part_time_emp.employee_info()
print("Salary:", part_time_emp.calculate_salary())
