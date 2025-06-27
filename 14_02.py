#WAPT create a login page:
'''
un = 'dhaval_123'
pw = 'Dhaval@123'
uni = input('enter useeranme')
pwi = input('enter password')

if un==uni:
    if pwi==pw:
        print('login successfull')
    else:
        print('incoorct pass')
else:
    print('invalid username')


'''
#note:
'''
--nested if is use when ever we have multiple condition and multiple statement
block and the conditions are depended on each other
'''

#WAPTCWG character is a vowel only if it is alphabet
'''
ch = input()

if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print('vowel')
    else:
        print('consonant')
else:
    print('not alphabet')
'''

# WAPTP a middle value present inside give data
'''
d = eval(input())

if type(d) in (str,list,tuple):
    if len(d)%2:
        print(d[len(d)//2], 'is middle value')
    else:
        print('no middle value')
else:
    print('not a valid data for middle value')
'''

#WAPT print the middle character present inside the string only if it's not a special character
'''
d = input()
l = len(d)
if len(d)%2:
    if d[l//2].isalnum():
        print(d[l//2])
    else:
        print('special cha')
else:
    print('middle value not present')
'''

#wap to find greatest among 3 number using nested if
'''
a,b,c = int(input()),int(input()),int(input())

if a > b:
    if a>c:
        print(a, 'greatest')
    else:
        print(c,'is greatest')
else:
    if b > c:
        print(b, 'is greatest')
    else:
        print(c, 'is greatest')
'''

###
#assi
# smallest amlong 3 number


#geastes among four number
'''
a,b,c,d = int(input()),int(input()),int(input()), int(input())

if a>b:
    if a>c:
        if a>d:
            print(a, 'is greatest')
        else:
            print(d, 'is greatest')
    else:
        if c>d:
            print(c,' is greatest')
        else:
            print(d, ' is greatest')
else:
    if b>c:
        if b>d:
            print(b, ' is greatest')
        else:
            print(d, ' i s greatest')
    else:
        if c>d:
            print(c, ' is greatest')
        else:
            print(d, ' is greatest')
'''

#WAP to find 2nd greatest among 3 numbers
'''
a,b,c = int(input()),int(input()),int(input())

if a > b:
    if a>c:
        if b>c:
            print(b, ' is 2nd gn')
        else:
            print(c, '  is 2nd gn')
    else:
        print(a, ' 2nd greatest numner')
else:
    if b>c:
        if a>c:
            print(a, ' is 2nd gn')
        else:
            print(c, ' is 2nd gn')
    else:
        print(b, '  2nd gn')
'''

# OR
'''
if a>b and a>c:
    if b>c:
        print(b)
    else:
        print(c)
elif b>c:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if a>b:
        print(a)
    else:
        print(b)
'''


#WAP to second greastest among four numbers
'''
a,b,c,d = int(input()),int(input()),int(input()),int(input())

if a>b and a>c and a>d:
    if b>c and b>d:
        print(b)
    elif c>d:
        print(c)
    else:
        print(d)
elif b>c and b>d:
    if a>c and a>d:
        print(a)
    elif c>d:
        print(c)
    else:
        print(d)
elif c>d:
    if a>b and a>d:
        print(a)
    elif b>d:
        print(b)
    else:
        print(d)
else:
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)

'''

