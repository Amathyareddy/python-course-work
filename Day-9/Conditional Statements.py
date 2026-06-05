
Conditional Statements
-----------------------
Conditional statements are one of the most powerful tools in programming—they let your code make decisions based on certain conditions.
Think of them as the "if this, then that" logic that guides how a program behaves.

🌟 Basics of Conditional Statements:

-> if statement: Executes a block of code if the condition is true.

-> else statement: Executes a block of code if the condition is false.

-> elif (else if): Lets you check multiple conditions in sequence.


     1.Simple if
     2.if -else
     3.if -elif -else
     4.Nested if

"""
1.

s='python programming'

if 'python' in s:
    print('python found')
    
"""

"""
2.

s='python programming'

if s[0]=='p':
    print("string is starting with p")

"""

"""
3.

data = ('abc','1234')

username,password = input("Enter the username and password: ").split()

if data == (username,password):
    print("Login Successful")
else:
    print("Invalid login")
    
"""

"""
4.

n = int(input("Enter the num: "))

if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("Zero")

"""

"""
5.

products ={
    'laptops':0,
    'mouse':10,
    'charger':5,
    'phones':30,
    'keyboard':0,
}

product = input("Enter the product: ")
if product in products:
    if products[product]!=0:
        print(f"you can buy {product}!!")
    else:
        print(f"{product} is out of stock")
        
else:
    print(f"{product} is not available")

"""

    
