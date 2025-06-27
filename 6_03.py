'''
for i in range(1,6):
    for j in range(1,6):
        print( f'({i} , {j})' , end=' ')
    print()
'''
'''
n = int(input())
for i in range(n,0,-1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(2*i-1):
            print("*", end=" ")
        print()
'''

'''
for i in range(1,6):
    for j in range(1,6):
        if   i <= j:
            print('*',end= ' ')
        else:
            print('_',end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(5,0,-1):
        if   i <= j:
            print('*',end= ' ')
        else:
            print('_',end=' ')
    print()
'''
'''
n = int(input())
for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(1,2*i):
            print("*", end=" ")
        print()

print('\n##\n')
'''
n = int(input())
'''
for i in range(1,n+1):
    for j in range(1,n*2):
        print( f'({i} , {j})' , end=' ')
    print()

print('\n')
'''
'''
for i in range(1, n + 1):
        for j in range(1,n*2):
            if i+j >= n+1 and  j-i <= n-1:
                print('*',end=' ')
            else:
                print(" ", end=' ')
        print()
'''
'''
for i in range(n ,0,-1):
        for j in range(1,n*2):
            if i+j >= n+1 and  j-i <= n-1:
                print('*',end=' ')
            else:
                print(" ", end=' ')
        print()
'''

n = 3  # You can adjust this to make the pattern larger

for i in range(1, n + 1):  # Upper part
    for j in range(1, n + 1):
        if i + j >= n + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(n - 1, 0, -1):  # Lower part
    for j in range(1, n + 1):
        if i + j >= n + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
