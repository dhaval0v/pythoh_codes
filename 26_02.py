#IMP programm
#WAPT find the smallest factor of a number
'''
n = int(input())

for i in range(2,n+1):
    if n % i == 0:
        print(i)
        break
'''

#WAP to check wether given number prime or not
'''
n = int(input())
for i in range(2,n):
    print(f'{n} | {i} ')
    if n % i == 0:
        print(f'{n} % {i} = {n % i}')
        print('not prime number')
        break
else:
    print('prime nummber')
'''

#WAPT check weather given string contains only upper case character or not
'''
s = input()
#print(s.isupper())

for i in s:
    if s.isupper() == False: # not s.isupper
        print('not only upper')
        break
else:
    print('contain only upper')
'''

#WAPT check weatehr given list is linear or nested
'''
l = eval(input())

for i in l:
    if type(i) in (list,set,dict,str,tuple):
        print('neasted')
        break
else:
    print('linear')
'''

#WAPT CHECK weather a given list is homogemius or hectogenus
'''
l = eval(input())
for i in l:
    if type(l[0]) != type(i):
        print('hecto')
        break
else:
    print('homo')
'''

#WAPT check weather a given dict contains only string keys
'''
d = eval(input())
for i in d:
    if type(i) != str:
        print('not only str')
        break
else:
    print('only str')
'''

#WAPT W the values in dict are only immutable or not
'''
d = eval(input())

for i in d:
    if type(d[i]) in (set,list,dict):
        print('mutable')
        break
else:
    print('im')
'''
