'''
# It gets the Error

def display():
    n=10
    print("Inside:",n)

display()
print("Outside:",n)



#Global Accesses


n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)



# write global n it become the outside executes without Error

def display():
    global n
    n=10
    print("Inside:",n)

display()
print("Outside:",n)


#Using the Global Keyword

def display():
    global n
    n += 10
    print("Inside:",n)

n=10
display()
print("Outside:",n)



#Using th nonlocal Keyword

def display():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()

    print("Outer function:",n)

display()



s='python'
print(len(s))

len=5
print(len(s))



#int float complex string list tuple set dict bool --> Data Types
#int float complex srring tuple bool --> Inside and Outside are Not same
#list set dict  --> Inside and Outside are same

#int
def update(n):
    n+=10
    print("Inside:",n)

n=10
update(n)
print("Outside:",n)



#float
def update(n):
    n+=10
    print("Inside:",n)

n=10.4
update(n)
print("Outside:",n)



#complex
def update(n):
    n+=10
    print("Inside:",n)

n=3+4j
update(n)
print("Outside:",n)



#list
def update(n):
    n+=[10]
    print("Inside:",n)

n=[10]
update(n)
print("Outside:",n)


#tuple
def update(n):
    n+=(5,6)
    print("Inside:",n)

n=(1,2,3,4)
update(n)
print("Outside:",n)


#set
def update(n):
    n.add(6)
    print("Inside:",n)

n={1,2,3}
update(n)
print("Outside:",n)


#bool
def update(n):
    n=False
    print("Inside:",n)

n=True
update(n)
print("Outside:",n)


#dict
def update(d):
    d['course']='python'
    print('inside:',d)

d={'name':'achyuth'}
update(d)
print('outside',d)

'''



