#swapping:-
'''
(1) a,b = b,a
(2) temp = a
    a = b
    b = temp
(3) a = a + b
    b = a - b
    a = a - b
(4) a = a * b
    b = a//b
    a = a//b
(5) a = a ^ b
    b = a ^ b
    a = a ^ b
'''

#Bubble sort
#WAP to sort a list without using inbuilt function
# 1
'''
l = eval(input())

for i in range(1,len(l)):
    print('i = ',i,' | len(l)',len(l))
    for j in range(len(l)-i):
        print('j = ',j,' | len(l)-i = ',(len(l)-i))
        if l[j] > l [j + 1]:
            print('l[j] = ',l[j], '>  l[j+1] = ' , l[j+1])
            l[j],l[j+1] = l[j+1],l[j]
    print(l,'\n')
print(l)
'''
#2
'''
l = eval(input())

for i in range(1,len(l)):
    flag = False
    for j in range(len(l)-i):
        if l[j] > l [j + 1]:
            l[j],l[j+1] = l[j+1],l[j]
            flag = True
    if flag == False:
        break
print(l)
'''
###
'''
l=[5,9,1,0,3,-5]
l.sort()
l
[-5, 0, 1, 3, 5, 9]
sorted([5,9,1,0,3,-5])
[-5, 0, 1, 3, 5, 9]
sorted((5,9,1,0,3,-5))
[-5, 0, 1, 3, 5, 9]
sorted({5,9,1,0,3,-5})
[-5, 0, 1, 3, 5, 9]
d = {1:45, 6:23, 0:67}
sorted(d)
[0, 1, 6]
sorted(d.values())
[23, 45, 67]
sorted(d.items())
[(0, 67), (1, 45), (6, 23)]
'''

# pair sum problem OR 2 - sum problem
'''
l = eval(input())
target = int(input())

out = []
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == target:
            out.append((l[i],l[j]))
print(out)
'''
