'''
def func(num):
    if basecondi:
        return
    func()



def func(num):
    if num == 0:
        return
    print(num,end=' ')   # reverse ex=> 5 4 3 2 1
    func(num-1)
    #print(num,end=' ') 

func(5)
    


def func(num):
    if num == 0:
        return
    #print(num,end=' ') 
    func(num-1)
    print(num,end=' ')  # ex=> 1 2 3 4 5

func(5)


def func(num):
    if num == 0:
        return
    print(num,end=' ')  
    func(num-1)
    print(num,end=' ')    # ex=> 5 4 3 2 1 1 2 3 4 5 

func(5)
    


# Sum of digits

def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)

print(sumofdigits(5))



# Product of digits

def productofdigits(n):
    if n==0:
        return 1
    return n*productofdigits(n-1)

print(productofdigits(5))



#Power Calculation

def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)

print(power(2,4))
print(power(3,3))

'''

#Reverse a string
def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)

l="Python Programming"
print(reverseofstr(l,len(l)-1))
