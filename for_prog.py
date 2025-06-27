#WAPTF the product of n natural number
'''
n = int(input())
prod = 1
for i in range(1,n+1):
    prod *= i
print(prod)
'''

#WAPTF the product of all the even natural numbers in the range of 1 to n
# which is not divisiable by 3
'''
prod = 1
n = int(input())

for i in range(1, n+1):
    if i%2==0 and i%3 != 0:
        print(f' | {i} | {prod} |')
        prod *= i
print(prod)
'''

#WAPT print all the upercase character present inside a given string
'''
s = input()
for i in s:
    if i.isupper():
        print(i, end=' ')
'''

#WAPT extract all the upper case character from a string
'''
s = input()
out = ''
for i in s:
    if i.isupper():
        out += i
print(out)
'''

#WAPTf the reverse the string
'''
s = input()
rs = ''
for i in s:
    rs = i + rs
print(rs)
'''

#pali or not
'''
s=input()
rs = ''
for i in s :
    rs = i + rs
if rs == s:
    print('pali')
else:
    print('no')
'''

#factorial number
'''
n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
'''

