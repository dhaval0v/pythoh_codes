#pattern programming
'''
* * * 

* * * 

* * *
'''

'''
for i in range(1,4):
    for j in range(1,4):
        print('*', end=' ')
    print('\n')
'''

#pattern - 2 ( primary  diagonal )
'''
for i in range(1,6):
    for j in range(1,6):
        if   i == j:
            print('*',end= ' ')
        else:
            print('_',end=' ')
    print()
'''
#pattern - 3 (secondry diagonal)

for i in range(1,6):
    for j in range(5,0,-1):
        if   i == j:
            print('*',end= ' ')
        else:
            print('_',end=' ')
    print()

#pattern - 4 ( primary triagonal )
'''
for i in range(1,6):
    for j in range(1,6):
        if   i >= j:
            print('*',end= ' ')
        else:
            print('_',end=' ')
    print()

'''

#pattern - 5 (secondry triagonal)

for i in range(1,6):
    for j in range(5,0,-1):
        if   i >= j:
            print('*',end= ' ')
        else:
            print('_',end=' ')
    print()


# for index
'''
for i in range(1,6):
    for j in range(1,6):
        print( f'({i} , {j})' , end=' ')
    print('\n')
'''

##
