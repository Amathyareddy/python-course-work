
'''

#checking the 1-11 numbers

def display():
    for i in range(1,11):
        yield i


n = display()
for i in range(10):
    print(next(n))


#write the end to stop

def display():
    for i in range(1,11):
        yield i


n = display()

try:
    while True:
        print(next(n))
        
except StopIteration:
    print("End of the program")



#checking the factors

def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

n = factors(56)

try:
    while True:
        print(next(n))
        
except StopIteration:
    print("End of the program")



#Using the Generatos to factors

def factors(n):
    return [i for i in range(1,n+1) if n%i==0]

def generatos(res):
    for i in res:
        yield i

res = factors(60)
facts = generatos(res)
for i in range(len(res)):
    print(next(facts))



#Using the generatos and creating prime numbers

def primes():
    res = []
    for num in range(2,101):

        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            res.append(num)

    return res

def generatos(res):
    for i in res:
        yield i

res = primes()
g = generatos(res)

for i in range(len(res)):
    print(next(g))

'''
