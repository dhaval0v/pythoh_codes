'''
l = eval(input())
out = []

for i in l:
    if i not in out:
        out.append(i)
print(out)
'''

# l = [10,20.9,10+2j,'python',24,'program']
# out = {'python' : 6, 'program':7}
'''
l = [10,20.9,10+2j,'python',24,'program']
out = {}

for i in l:
    if type(i) == str:
        out[i] = len(i)
print(out)

'''

# l = [10,20.9,10+2j,'python',24,'program']
# out = {'python' : 'pn', 'program':'pm'}
'''
l = [10,20.9,10+2j,'python',24,'program']
out = {}

for i in l:
    t = ''
    if type(i) == str:
        t = i[0] + i[-1]
        out[i] = t
print(out)
'''
'''
#l=['python.py','pho.com','google.com']
#out = ['py','html','com']

l=['python.py','pho.html','google.com']
out = []
for i in l:
    if type(i) == str:
        if '.' in i:
            s = i.split('.')
            out.append(s[1])
print(out)
'''
'''

#l=['python.py','pho.com','google.com']
#out = ['py':'python',]
l=['python.py','phol.html','google.com','python2.py']
out = {}
for i in l:
    if type(i) == str:
        if '.' in i:
            s = i.split('.')
            k = s[1]
            v = s[0]
            out[k] = v
print(out)
'''
#
'''
l=['python.py','phol.html','google.com','python2.py']
#out = {'py': ['python','python2'], 'html': 'phol', 'com': 'google'}
out = {}
for i in l:
    if type(i) == str:
        v = []
        if '.' in i:
            s = i.split('.')
            k = s[1]
            v.append(s[0])
            out[k] = v
print(out)
'''
##
'''
l = ['python.py', 'phol.html', 'google.com', 'python2.py']
out = {}

for i in l:
    if '.' in i:
        s = i.split('.')
        k = s[1]
        v = s[0]

        if k in out:  
                out[k] = [out[k], v]
        else:
            out[k] = v

print(out)

'''

## l = [10,13,4,6]
## out = [23,20,29,27]

l = [10,13,4,6]
out = []

for i in l:
    sum = 0
    for j in l:
        if i == j:
            continue
        else:
            sum += j
    out.append(sum)
print(out)
