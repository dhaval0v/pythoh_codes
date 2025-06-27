'''
s = input()
out={}
a = s.split()
for i in a:
    count=''
    #print(f' i = {i} | count = {count}')
    for j in i:
        if j in 'aeiouAEIOU':
            count += j
            #print(f' j = {j} | count = {count}')
        out[i] = count
        #print(f' out = {out}')

print(f'final out = {out}')
'''
#WAPT print all the palideom number in he range of 1 to 150
'''
for i in range(1,151):
    temp = i
    rev=0
    while temp != 0:
        j = temp%10
        rev = (rev*10) + j
        temp = temp//10
    if i == rev:
        print(i)
'''

#WAPT print all the prime number in the range of 2 to 50
'''
for i in range(2,51):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)

'''

#assiii
#l=[123,406,'python',120,40]
#out = [321,604,21,4]


#WAP to extrcart all the palidrom sdstring from a given list withou slicing
# s ='Nested for loops'
# out = {'Nested':'NeStEd','for':'fOr','loops':'lOoPs'}
#OUT = {'Nested':'nEstEd','for':'fOr','loops':'lOOps'}

#WAP to exctract all the perfect numbers in the range of 1 to n in the form of tuple

#l=[123,406,'python',120,40]
#out = [321,604,21,4]

'''
l = [123, 406, 'python', 120, 40]
out = []

for i in l:
    if type(i) == int:
        rev = 0
        temp = i
        while temp > 0:
            j = temp % 10
            rev = (rev * 10) + j
            temp = temp // 10
        out.append(rev)
print(out)
'''

#WAP to extrcart all the palidrom sdstring from a given list withou slicing
'''
l = eval(input())
out=[]

for i in l:
    rs = ''
    if type(i) == str:
        for ch in i:
            rs = ch + rs
        out.append(rs)

print(out)
'''

# s ='Nested for loops'
# out = {'Nested':'NeStEd','for':'fOr','loops':'lOoPs'}

#######################
'''
s = 'Nested for loops'
l = s.split()
out = {}

for i in l:
    temp = ''
    for j in range(len(i)):
        if len(i)%2 == 0:
            if j % 2 == 0:
                temp += i[j].upper()
            else:
                temp += i[j].lower()
        else:
            if j % 2:
                temp += i[j].upper()
            else:
                temp += i[j].lower()
    out[i] = temp

print(out)
'''

# s ='Nested for loops'
#OUT = {'Nested':'nEstEd','for':'fOr','loops':'lOOps'}
'''
s ='Nested for loops'
l = s.split()
out = {}

for i in l:
    temp = ''
    for j in range(len(i)):
        if i[j] in 'aeiouAEIOU':
            temp += i[j].upper()
        else:
            temp += i[j].lower()
    out[i] = temp
print(out)
'''

#WAP to exctract all the perfect numbers in the range of 1 to n in the form of tuple
#n = int(input())
#WRONG
''' 
for i in range(2,51):
    temp = 0
    for j in range(1,i):
        if i % j == 0:
            break
    else:
        temp += i
    if temp == i:
        print('perfect number = ',temp)
'''
#done
'''
n = int(input())
t = ()

for i in range(1,n+1):
    sum= 0
    for j in range(1,i):
        if i % j ==0:
            sum += j
    if sum == i:
        t += (i, )
print(t)
'''
