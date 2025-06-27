#WAPT merge two sorted list into a single list such that the resultant list is also sorted
'''
l1 = eval(input())
l2 = eval(input())

l = []
i = 0
j = 0

# if we use or then it returns error 'out of range error'

while i < len(l1) and j< len(l2):
    if l1[i] < l2[j]:
        l.append(l1[i])
        i += 1
        print('from list one and i is',i)
        print(f' | {l} ')
    else:
        l.append(l2[j])
        j += 1
        print('from list two and j is',j)
        print(f' | {l} ')

if len(l1) > len(l2):
    print('remining items of first list')
else:
    print('remining items of second list')

while i < len(l1):
    l.append(l1[i])
    i += 1
    print(f' | {l} ')

while j < len(l2):
    l.append(l2[j])
    j += 1
    print(f' | {l} ')


print('\n\nAnswer is :- \n',l)
'''

#WAP to print nth fibonacci number
'''
n = int(input())
a=0
b=1
i=1

if n == 1 or n == 2: # or # if n in (1,2):
    print(n-1)
else:
    while i <= n-2:
        c = a + b
        a = b
        b = c
        i += 1
    print(c)
'''
#or
'''
n = int(input())
a=0
b=1
i=1

if n == 1 or n == 2: # or # if n in (1,2):
    print(n-1)
else:
    while n-2>0:
        c = a + b
        a = b
        b = c
        n -= 1
    print(c)
'''
# or
'''
n = int(input())
a=0
b=1
i=1

if n == 1 or n == 2: # or # if n in (1,2):
    print(n-1)
else:
    while n-2>0:
        c = a + b
        a,b = b,c
        n -= 1
    print(c)
'''

#or

'''
n = int(input())
a=0
b=1
i=1

if n == 1 or n == 2: # or # if n in (1,2):
    print(n-1)
else:
    print(a,b,end=' ')
    while n-2>0:
        c = a + b
        a,b = b,c
        n -= 1
        print(c,end=' ')

'''

#WAPT check a weather given number is spy number or not
'''
a number is said to be spy number if the sum of digits of a number if equal to the product
of the digit
'''
''' 
n = int(input())

sum = 0
mul = 1

while n != 0:
    rem = n % 10
    sum += rem
    mul *= rem
    n //= 10
if sum == mul :
    print('spy')
else:
    print('no spy')

'''

#WAPT check wether given number is neon number or not
'''
it is number where the sum of digit of its square equals the orinal number
'''

'''
n = int(input())

sq = n*n
sum = 0

while sq != 0:
    rem = sq % 10
    sum += rem
    sq //=10
if sum == n:
    print('neon')
else:
    print('no neon')
'''

#WAP to check given number is automorfic or not
'''
it is number whose square ends in the same digit as the number itself
'''
'''
n = int(input())

sq = n**2

rem = sq % 100

print(rem,sq)
if n == rem:
    print('automorfic')
else:
    print('not automorfic')

'''

'''
n = int(input())

sq = n**2

rem = sq % 100 # 

print(rem,sq)
if n == rem:
    print('automorfic')
else:
    print('not automorfic')

'''


#assi
#WAP to check given number is ugly number or not
# wap to check given number is happy nuber or not

'''
n = int(input())
if n >10:
    if n%2==0 and n %3==0 and n%5==0:
        print('ugly nummber')
    else:
        print('not ugly')
elif n<0:
    print('neg number not acceptable')
else:
    print('ugly')
'''
'''
n = int(input())
temp = n
while temp > 0:
    sum=0
    print('rem | mul | sum | temp')
    while temp > 0:
        rem = temp%10
        mul = rem*rem
        sum += mul
        temp //=10
        print(f'{rem} | {mul} | {sum} | {temp}')
    if sum == 1:
        print('happy')
    else:
        temp = sum
        print(f'temp = {temp} | sum = {sum}\n')

'''
