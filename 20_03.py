def rn(n):
    if n >= 1:
        print(n)
        return rn(n-1)

#n = int(input())
#rn(n)


def ph(n):
    if n >= 1:
        print('Helllooooo')
        return ph(n-1)

# 3 2 1 2 3

def pnp(n,temp1,temp2):
    if temp1 > 1:
        print(temp1,end=' ')
        return pnp(n, temp1-1,temp2)
    if n >= temp2:
        print(temp2, end=' ')
        return pnp(n, temp1,temp2+1)

n = int(input())
temp1=n
temp2=1
pnp(n,temp1,temp2)
