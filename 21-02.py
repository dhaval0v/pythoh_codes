'''
n = int(input())
even,odd,sum,prob=0,0,0,1
rem = 0
while n != 0:
    rem = n%10
    if rem % 2 ==0:
        sum += sum
        even = even * 10 + rem
    else:
        prob *= rem
        odd = odd * 10 + rem
    n= n //10
if sum>prob:
    print(even)
else:
    print(odd)
'''

#WAPT print all the factors of a given number
'''
n = int(input())
fact=[]

i = 1
while i <= n:
    if n%i == 0:
        fact.append(i)
    i += 1
print(fact)
'''

#WAP to check given number is perfect or not
'''
n = int(input())
sum = 0
i = 1
while i <=n//2:
    if n%i == 0:
        sum += i
    i += 1
print(sum)
if sum == n:
    print('perfect')
else:
    print('no')
'''


#WAPT check a given number is Xylem
'''
n = int(input())
ln = n%10
sum = 0
rem = 0
n//=10
while n > 9:
    rem = n%10
    sum += rem
    n//=10
if ln + n == sum:
    print('Xylem')
else:
    print('not xylem')
'''

#dry run
'''
n = int(input())
ln = n%10
sum = 0
rem = 0
n//=10
while n > 9:
    rem = n%10
    sum += rem
    n//=10
    print(f'{n} |  {ln}  |  {sum}')
'''

#WAPT check a given number is armstorng number or not without type casting
'''
it is said to be armstrog when the sum of powers of digit of individual digit of a given
numberis queal to number it self
'''
'''
n = int(input())
digit = n
ln = n
l = 0
sum = 0
rem = 0
while ln > 0:
    l += 1
    ln//=10
    print(f'{ln} |  {l}  |  {sum}')

print('\n')
while n != 0:
    rem = n%10
    sum += ( rem ** l )
    n//=10
    #dry run
    print(f'{rem} |  {n}  |  {sum}')

if sum == digit:
    print('armstorng')
else:
    print('not arm')

'''
