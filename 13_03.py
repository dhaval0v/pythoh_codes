# two list to dict
'''
def ld(l1,l2):
    out = {}
    i =0
    if len(l1) == len(l2):
        while i < len(l1):
            if type(l1[i]) == str:
                out[l1[i]] = l2[i]
            i +=1
    return out

l1 = eval(input())
l2 = eval(input())

rn = ld(l1,l2)
print(rn)
'''

#WAPTF the initial index  of a char
def ic(s,ch):
    return s.index(ch)
print(ic(input(),input()))
