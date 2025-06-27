#WAPto extract all the key value pairs from a dict. only if the keys are strings containing
# atlist three char.. in it and the values contain a middl value
'''
d = eval(input())
out={}

for i in d:
    if type(i) == str and len(i) >= 3:
        if type(d[i]) in (str, list, tuple) and len(d[i])%2==1:
            out[i] = d[i]

print(out)
'''

#WAPT exctract all the key values pair from a dict only if
#the keys are immutable and the values are mutable
'''
d = eval(input())
out = {}

for i in d:
    if type(d[i]) in (list,set,dict):
        out[i] = d[i]
print(out)
'''

#WAPT exctract all the words from a string as keys and the number of char. in that word as
# values in the from of dict.

'''
spilt():-
    it is string method which is used to spilt a string into sub strings and the resultan in
    the form of list

    syntax = val.spilt()

    by default it will spilt on space
    we can pass a char. and number of spilts inside spilt function
    exa :   s='python data Analysis Scirnce'
            s.split()
               ['python', 'data', 'Analysis', 'Scirnce']
            s.split('a')
               ['python d', 't', ' An', 'lysis Scirnce']
            s.split('a',1)
               ['python d', 'ta Analysis Scirnce'
    
'''
'''
s = input()
out = {}

l = s.split()

for i in l:
    out[i] = len(i)
print(out)
'''

#ASSIgnment:
#1) WAPT split a string wihout using split() or without slicing

#WAPT find 
'''
s = input()
out={}

l = s.split()

for i in l:
    if len(i)%2==0:
        out[i] = i[0] + i[-1]
    else:
        out[i]=i[0] + i[len(i)//2] + i[-1]
print(out)
'''

