# str list tuple set dict range()

'''
for var in seq:
    print(var)


s = 'python programming'
for ch in s:
    print(ch)


l = ['sugar','salt','oil','eggs']
for item in l:
    print(item)



t = ('1.intro','2.Tokens','3.Data types')
for i in t:
    print(i)



s = {'laptop','mouse','keyboard','phone','charger'}
for i in s:
    print(i)



d = {'name':'Ramakanth','Batch':'55,'course':'PFS','skills':['python','mysql','java']}
if i in d:
    print(i,d[i])



#range (start,stop+1,step) => (0,n,1)

for i in range(1, 11):
    print(i)



for i in range(2,51,2):
    print(i)



for i in range(20,0,-1):
    print(i)


for i in range(30,2,-3):
    print(i)


for i in range(5,101,5):
    print(i)



for i in range(6):
    print(i)



for i in range(1,50,2):
    print(i)




s = 'looping statements'

for i in range(len(s)):
    print(i,s[i])



l = [7,2,4,8,3,1,5]
for i in range(len(l)):
    print(i,l[i])


#Using the enumerate

s = 'looping'
for i in enumerate(s):
    print(i[0],i[1])



l = [7,2,4,8,3,1,5]
for i in enumerate(l):
    print(i[0],i[1])



s = 'looping statements'

for i in enumerate(s):
    print(i[0],i[1])



t = (7,2,4,8,3,1,5)
for i in enumerate(t):
    print(i[0],i[1])
    
    

k = {7,2,4,8,3,1,5}
for i in enumerate(k):
    print(i[0],i[1])



for i in range(10):
    pass



for i in range(10):
    if i==5:
        break
    print(i)



for i in range(10):
    if i==5:
        continue
    print(i)



s = 'looping statements'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)


l = [56,76,32,3,34,2,3,5,97,45,13,23,45,23,98,76,32]
for i in l:
    if i%2==0:
        print(i)



d = {'laptop':0,'chargers':2,'keyboard':10,'phone':15,'tab':0,'mouse':5}

for i in d:
    if d[i]:
        print(i)



t = (9,2,13,4,5,6)
#0 2 26 12 20 30
for i in range(len(t)):
    print(i*t[i])

'''

names = {'achyuth','amathya','prakash','ramakanth','naresh'}
for i in names:
    print(i.upper())
