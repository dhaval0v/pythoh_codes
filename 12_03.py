#greatest among three numbers
'''
def gm(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            print('max ',n1)
        else:
            print('max ',n3)
    else:
            if n2 > n3:
                print('max ',n2)
            else:
                print('max ',n3)

n1 = int(input())
n2 = int(input())
n3 = int(input())
gm(n1,n2,n3)
'''

#add to list
def al(l1,l2):
    temp = []
    for i in l1:
        temp.append(i)
    for i in l2:
        temp.append(i)
    print(temp)

l1 = eval(input())
l2 = eval(input())
al(l1,l2)

