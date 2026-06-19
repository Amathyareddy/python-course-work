'''
#Using lambda to dictionary making discount for items

d = {'sugar':40,'salt':20,'cooking oil':80,'chilli':60}

res = dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1 = dict(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))

print(res)
print(res1)

'''

#Using Filter

d = {'sugar':40,'salt':20,'cooking oil':80,'chilli':60}

res = dict(filter(lambda i:i[1]>50,d.items()))
res1 = dict(filter(lambda i:i[1]<50,d.items()))

print(res,res1)
