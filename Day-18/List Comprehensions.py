'''
res = []
for i in range(1, 11):
    res.append(i)

print(res)



# Using List Comprehension

res1 = []
for i in range(1, 11):
    res1.append(i)

res2 = [i for i in range(1,11)]

print(res1)
print(res2)

res3 = []
for i in range(3,31,3):
    res3.append(i)

res4 = [i for i in range(3,31,3)]

print(res3)
print(res4)

res5 = []
for i in range(2,51,2):
    res5.append(i)

res6 = [i for i in range(2,51,2)]

print(res5)
print(res6)




a = 'Python Programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

l1 = [i for i in a if i in 'aeiouAEIOU']
print(l1)



a = [1,2,4,5,6,8,9,11,2,32,45,65,67,80]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
        
print(l)

l1 = [i if i%2==0 else 0 for i in a]
print(l1)



l = []
for i in range(10):
    l.append(int(input()))

print(l)



l = [int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)




l = []
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)


l1 = [j for i in range(3) for j in range(1,4)]

print(l1)



#Using the temp into list

l = []
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)



#Using the temp into list in Another Method

l = [[j for j in range(1,4)] for i in range(3)]

print(l)



s = set()
for i in range(1,11):
    s.add(i)
    

s1 = {i for i in range(1,11)}

print(s,s1)


d = {}
for i in range(1,11):
    d[i]=i*i

print(d)


res = {i:i*i for i in range(1,11)}
print(res)



#checking the student names and marks

res = {input("Enter the name: "):int(input("Enter the mark: ")) for i in range(5)}
print(res)

'''


