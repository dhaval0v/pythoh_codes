#Decorators
'''
-> it is a function which is used to add some additional feature to the
existing functions.
-> it can be used when we have common pre-task and post-task for
duing some opration.
-> there are two types of decorator , inbuilt decorator, user defined decorator

1. inbuilt decorator:
-> it is a decorator whose task are pre defined by the devlopeer
(a) @staticmethod
(b) @classmethod
(c) @abstractmethod

2. userdefine decorators:
-> it is a decorator which is ceated based on the user requirement.
syntax:

def dec_name(func):
    def inner(*args,**kwargs):
        #pre-task
        func(*args,**kwargs)
        #post-task
    return inner
'''
#exa:
def Facebook(func):
    def inner(*args, **kwargs):
        print("pre0task")
        func(*args,**kwargs)
        print("post-task")
    return inner

@Facebook
def A():
    print("updating Facebook")

@Facebook
def B():
    print("Like the post")

A()
print('-'*72)
B()


print('-'*72)

def Positive(func):
    def inner(*args,**kwargs):
        res = func(*args,**kwargs)
        return abs(res)
    return inner

@Positive
def add(a,b,c,d):
    return a+b+c+d

print(add(10,-10,10,-40))

