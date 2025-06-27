#function programming
#lambda:
'''
-> it is an anonymous function which dose not have any name
used to display the output.

-> lambda is an keyword which is use to perform small operation in
python.

syntax:
var = lambda arg: expression
^
it is fun. name

exa:
result = lambda n:n%2==0
'''
sqr = lambda n: n**2

'''
-> lambda fun. do not have any proper stucture to display the output.
it will store the address of lambda function.
so, to overcome this one we make use of container to display the o/p.
'''

#syntax:

gl = lambda a,b: print("Easy") if a>b else print("Hard")

#even or odd
eo = lambda n: "Even" if n%2==0 else "Odd"

#wrap to print sq. of an int number if the given value is even
#else print the qub. of an int number
sq = lambda n: n**2 if n%2==0 else n**3

#to print a value in reverse odder if the given value is coll.
#which supports indexing else print the value
ro = lambda n: n[::-1] if type(n) in [str,list,tuple] else n

#WAP to find the sum of minimum 3 numbers and max. 5 number
mm = lambda a,b,c,d=0,e=0: a+b+c+d+e

#WAP to return true if both the input str is equle
ee = lambda a,b: True if a==b else False
#or
ee = lambda a,b: a==b

##########

#map():-
'''
-> it is an inbuilt function which is used to perform some set of
operations for each and every value present in a given collection.

syntax:
var = map(fun_name, coll)
print(list(var))


-> map() will return the o/p in format of address so to get values
typecasting is required.

__________________
| 1 | 2 | 3 | 4 |  ----
------------------     |
                    fun
                |-----------|
                | n**2     |
                |-----------|
                    |
                gives the add
                    |
                convert to list
                    |
__________________  |
| 1 | 2 | 3 | 4 |---
------------------
'''

#wapto find the sq. of all the values presrnt between the range of
# 1 to 10

sqr = lambda n: n**2
val = map(sqr,range(1,11))
print(list(val))

#or

print(list(map(lambda n: n**2,range(1,11))))

#WAPT find the length of each and every word present inside the
#given string

l = 'hello world'
print(list(map(lambda l: len(l), l.split(' '))))

