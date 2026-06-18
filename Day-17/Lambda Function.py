'''

  Lambda Functions:


 => A lambda function is a small, anonymous function often used for short, simple operations without formally defining a named function.
 => It comes from lambda calculus in mathematics and is widely used in programming for concise, inline logic, especially in functional programming contexts


  What is a Lambda Function?
  
 => Anonymous function: A function without a name, defined inline.

 => Origin: Derived from lambda calculus (Alonzo Church, 1930s).

 => Purpose: Useful for short-lived operations, passing functions as arguments, or simplifying code.

 
syntax:
var = lambda agr: exp


add = lambda a,b: a+b

print(add(12,13))
print(add(22,33))



wish = lambda name: f'Welcome the python course {name}'

print(wish('ramakanth'))
print(wish('naresh'))


#checking GST price

gst = lambda price: price + price*0.18

print(gst(1000))
print(gst(800))
print(gst(78000))


#checking greatest number

greatest = lambda a,b: a if a>b else b

print(greatest(18,19))
print(greatest(2000,1900))
print(greatest(10,30))


#checking even or odd number

iseven = lambda a: f"{a}-Even number" if a%2==0 else f"{a}-odd number"

print(iseven(4))
print(iseven(9))
print(iseven(65))


#checking the bill

bill = lambda charge: charge if charge>99 else charge + 30

print(bill(150))
print(bill(45))
print(bill(15))


#checking the login and instock

login = True
instock = False

status = lambda login,instock : ("You can buy product" if instock else "Product is out of stock") if login else "Login to buy a product"

print(status(login,instock))



d = {'suger':40,'salt':20,'milk':50,'cooking oil':90}
for i in d:
    d[i] += d[i]*0.18

print(d)



#checking the numbers cube

l = [1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,l))
print(res)




#changing the names into title

names = ['achyuth','ramakanth','naresh']
t = list(map(lambda i:i.title(),names))
print(t)



#Even number

l = [1,2,3,4,5,6,7]
res = list(filter(lambda i:i%2==0,l))
print(res)



#Greater than 5 number

l = [1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)



#Divible by 3 number

l = [1,2,3,4,5,6,7]
res = list(filter(lambda i:i%3==0,l))
print(res)




#Reduce Function

from functools import reduce

l = [1,2,3,4,5,6,7,8,9,10,11,12]

s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,l)
m = reduce(lambda max,i: max if max>i else i,l)
mi = reduce(lambda max,i: max if max<i else i,l)

print(s,p,m,mi)


'''

d = {'amathya':50,'ramakanth':40,'prakash':60,'naresh':80,'vamcc':70}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse= True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse= True)))
