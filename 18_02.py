#WAPTF the product f=of n natural number-
'''
prod = 1
n = int(input())
i = 1
while i <= n:
    prod *= i
    i += 1
print(prod)
'''

'''

__ | i | prod
   | 1 | 1
   | 2 | 1
   | 3 | 2
   | 4 | 6
   | 5 | 24
   | 6 |

'''

#WAPTF the product of all the even natural numbers in the range of 1 to n which is not divisable by 3

'''
prod = 1
n = int(input())
i =1
while i <= n:
    if i%2 == 0 and i%3 != 0:
        prod *= i
    i += 1

print(prod)

'''

#wapT print all the uppercase character present inside a given string
'''
ch = input()
i = 0
while i <= (len(ch)-1):# i<len(ch)
    if ch[i].isupper():
        print(ch[i],end='  ')
    i+=1

'''

#WAP to extract all the upper cqse character from a string
'''
s = input()
out = ''
i = 0
while i < len(s):
    if s[i].isupper():
        out = out + s[i]
    i += 1
print(out, end=' ')

'''
#Dry run
'''
i | s(i) | out
0 | 'P'  |  ''
1 | 'y'  |  'p'
.
.
.
7 |  W  |  PW
.
.
.
11 | d  |  PW
12 |    |  PW
'''


#assi:
# WAP to extrct all the alphbets present inside a given string
# WAP to count the number of SC present inside a given string
# WAPT find a product of the odd natural numbers in the range 1 to 50 which are divisiable by 11


#WAP to finr the sum of  all the digital character present inside the given string

'''
total = 0
i = 0
s = input()
while i < len(s):
    if s[i].isdigit():
        total += int(s[i])
    i += 1
print(total)
'''

#WAPTF the reverse of a given string without silcing
'''
s = input()
rs = ''
i = len(s) - 1
while i >= 0:
    rs = rs + s[i]
    i = i - 1

print(rs)
'''
#or
'''

s = input()
rs = ''
i = 0
while i < len(s):
    rs = s[i] + rs
    i += 1
print(rs)
'''
#dry run
'''
i | s[i] | out
0 | 'd'  | ''
1 | 'h'  | 'd' + '' => 'd'
2 | 'a'  | 'h' + 'd'=> 'hd'
3 | 'v'  | 'a' + 'hd' => 'ahd'
4 | 'a'  | 'v' + 'ahd' => 'vahd'
5 | 'l'  | 'a' + 'vahd' => 'avahd'
6 |      | 'l' + 'avahd' => 'lavahd'
'''

#WAPTC wheather a string is palidrome or not
'''

s = input()
rs = ''
i = 0
while i < len(s):
    print(f'{i} | {s[i]} | {rs}')
    rs = s[i] + rs
    i += 1

if rs == s:
    print('yes')
else:
    print('no')

'''

#Waptf the factorial of a number
'''
total = 1
n = int(input())
i = n
while i >= 1:
    total = i * total
    i -= 1

print(total)
'''

#WAP to extract all the even numbers from a given hectoge list
'''
l = eval(input())
out = []
i = 0
while i < len(l):szzzssqs
    if type(l[i]) == int and l[i]%2 == 0:
        out = out + [l[i]]#out.append(l[i])
    i += 1
print(out)
'''

#WAPT extract alll tge palidrome string from a given tuple
'''
t = eval(input())
out = ()
i = 0
while i < len(t):
    if type(t[i]) == str and t[i] == t[i][::-1]:
        out += (t[i],)
    i += 1
print(out)
'''

#WAP to find sum of all int values from the given tuptle
'''
t = eval(input())
out = 0
i = 0
while i < len(t):
    if type(t[i]) == int:
        out += t[i]
    i += 1
print(out)
'''


#WAPTF the sum of all the even intg value present at odd index from a given list
'''
l = eval(input())
out = 0
i = 0
while i < len(l):
    if type(l[i])==int and l[i]%2==0 and i%2 == 1:
        out += l[i]
    i += 1
print(out)
'''

#assi

# WAP to extrct all the alphbets present inside a given string
# WAP to count the number of SC present inside a given string
# WAPT find a product of the odd natural numbers in the range 1 to 50 which are divisiable by 11

#WAPTF the product of all the float values from a given string
#WAPT extract all the string data itmes from a given tuple only if
#   the string contains a middle value and the middle value is not a SC

#1)
'''
s = input()
out = ''
i = 0
while i < len(s):
    if s[i].isalpha():
        out += s[i]
    i += 1
print(out)
'''

#2)
'''
s = input()
sc = '!@#$%^&*()-+?_=,<>/'
count = 0
i = 0
while i <len(s):
    if s[i] in sc:
        count += 1
    i += 1
print(count)
'''


#3
'''
prod = 1
n = int(input())
i =1
if n <= 50:
    while i <= n:
        if i%2:
            prod *= i
        i += 1
    print(prod)
else:
    print('not in range')
'''

#4

#WAPT extract all the string data itmes from a given tuple only if
#   the string contains a middle value and the middle value is not a SC

#5

t = eval(input())
i = 0
while i < len(t):
    if type(t[i]) == str:
        if len(t[i]) % 2:
            mc = t[i][len(t[i]) // 2]
            if mc not in '!@#$%^&*()-+?_=,<>/':
                print(f'in {t[i]} string middle value is {mc}')
            else:
                print(f"In position {i}, in {t[i]} string middle value is a SC is {mc}")
        else:
            print(f"In position {i}, in {t[i]} string no middle value")
    
    i += 1
