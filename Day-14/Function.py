'''
  Function:-

=>In Python, a function is a reusable block of code that performs a specific task.
=>Functions help you organize your program, avoid repetition, and make your code easier to read and maintain.

  Key Points about Functions:-
 
=>Definition: Functions are defined using the def keyword.

=>Parameters: Functions can take inputs (called parameters or arguments).

=>Return Values: Functions can return outputs using the return statement.

=>Reusability: Once defined, a function can be called multiple times.


  Types of Functions:-
  
=>Built-in functions: Already provided by Python (e.g., print(), len(), sum()).

=>User-defined functions: Functions you create yourself.

=>Lambda functions: Small, anonymous functions defined with lambda.


  Advantages of Using Functions in Python:-

=>Reusability: Write once, use many times. You can call the same function multiple times without rewriting code.

=>Modularity: Break large problems into smaller, manageable pieces. Each function handles a specific task.

=>Readability: Code becomes easier to understand and maintain because functions give structure and meaning.

=>Debugging Made Easy: Errors are easier to locate since you can test functions independently.

=>Avoids Repetition (DRY Principle): Functions prevent duplication of code, saving time and reducing mistakes.

=>Scalability: Makes it easier to expand projects by adding new functions without disturbing existing ones.

=>Collaboration: In team projects, different developers can work on different functions without interfering with each other.

=>Abstraction: You don’t need to know the internal details of a function to use it—just call it with the right inputs.


  Types of Functions:-


1.Bulid-in functions:
    

| Function   | Description             | Example                         |
| ---------- | ----------------------- | ------------------------------- |
| `print()`  | Displays output         | `print("Hello")`                |
| `input()`  | Takes user input        | `name = input()`                |
| `len()`    | Returns length          | `len("Python")` → `6`           |
| `type()`   | Returns data type       | `type(10)` → `<class 'int'>`    |
| `int()`    | Converts to integer     | `int("5")` → `5`                |
| `float()`  | Converts to float       | `float("5.5")` → `5.5`          |
| `str()`    | Converts to string      | `str(10)` → `"10"`              |
| `list()`   | Creates a list          | `list("abc")` → `['a','b','c']` |
| `sum()`    | Returns sum of elements | `sum([1,2,3])` → `6`            |
| `max()`    | Returns largest value   | `max(1,5,3)` → `5`              |
| `min()`    | Returns smallest value  | `min(1,5,3)` → `1`              |
| `sorted()` | Sorts elements          | `sorted([3,1,2])` → `[1,2,3]`   |
| `abs()`    | Returns absolute value  | `abs(-10)` → `10`               |
| `round()`  | Rounds a number         | `round(3.75)` → `4`             |


   Types of Arguments:-
   
  1.Positional arguments
  2.Keyword arguments
  3.Defalut arguments
  4.Variable length positional arguments
  5.Variable length keyword arguments


def function_name(arg):
    #stmts
    return


function_name(para)




def wish(name):
    print(f"Welcome to the python course {name}!")

wish('prakash')
wish('ramakanth')
wish('vamcc')
wish('achyuth')


# checking the even or odd numbers

def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - Odd Number"

print(iseven(12))
print(iseven(13))


# checking the numbers factorials

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

num = int(input("Enter the number: "))
print(factorial(num))

    

# checking the Prime Number and Not Prime Number

def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not Prime Number"
    return f"{num} - Prime Number"

num = int(input("Enter the number: "))
print(isprime(num))

#Positional Arguments

#checking name,email and password

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('achyuth','achyuth@gmail.com','achyuth@123')
display('prakash','prakash@gmail.com','prakash@456')
display('vamcc','vamcc@gmail.com','vamcc@900')


def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display(name='achyuth',email='achyuth@gmail.com',pwd='achyuth@123')
display(name='prakash',email='prakash@gmail.com',pwd='prakash@456')
display(name='vamcc',email='vamcc@gmail.com',pwd='vamcc@900')


#Defalut Arguments

def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display(name='achyuth',email='achyuth@gmail.com')


#Variable Arguments

def display(*names):
    print("Names:",names)


display('subbu','naresh','prakash','vamcc','ramakanth')
display('naresh','vamcc','ramakanth')
display('ramakanth')
display('prakash','naresh','vamcc')



#Keyword Arguments

def display(**names):
    print("Names:",names)


display(k1='subbu',k2='naresh',k3='prakash',k4='vamcc',k5='ramakanth')
display(k1='naresh',k2='vamcc',k3='ramakanth')
display(k1='ramakanth')
display(k1='prakash',k2='naresh',k3='vamcc')

'''
