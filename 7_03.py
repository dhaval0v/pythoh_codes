'''
n = 3

for i in range(1,n*2):
    for j in range(1,n+1):
        if i + j >= n + 1 and  i - j <= n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('\n###\n')

for i in range(1,n*2):
    for j in range(n,0,-1):
        if i + j >= n + 1 and  i - j <= n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
##
'''
function:
->it is a name given to the memory location where the instructions are
getting stored
->after creating a function the instructions are getting stored in a
memory location and we can access it after calling the function

->memory allocation:
main space | method space
'''
'''
n = 5

for i in range(1,n*2):
    for j in range(1,n*2):
        if i + j > n  and  i + j <n*3   and  i - j < n and  j - i < n:
            print('*', end=' ')
        else:..
            print(' ', end=' ')
    print()

for i in range(1,6):
    for j in range(1,6):
        print( f'({i} , {j})' , end=' ')
    print()
'''

n=5
for i in range(1,n+1):
    for j in  range(1,n+1):
        if  ((i*j) % 4) == 0 and ((i + j) %2) == 0:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
