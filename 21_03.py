#even number
def en(n,temp=1):
    if n >= temp:
        if temp%2 == 0:
            print(temp)
            return en(n,temp+1)
        else:
            return en(n,temp+1)

#odd number
def on(n,temp=1):
    if n >= temp:
        if temp%2:
            print(temp)
            return on(n,temp+1)
        else:
            return on(n,temp+1)

#decimal to binary
def dtb(n):
    if n == 0:
        return
    #print(f'n = {n} and rem = {n%2}')
    dtb(n//2)
    print(n%2,end=' ')

# fibbonaccii
def f(n,n1=0,n2=1,temp = 1):
    print(n1, end=' ')
    if temp == n:
        return
    f(n,n2,n2 + n1,temp+1)
