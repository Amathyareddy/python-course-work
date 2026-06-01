Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
Amathya
name
'Amathya'
name = input("Enter your name
             
SyntaxError: unterminated string literal (detected at line 1)
name = input("Enter your name: ")
             
Enter your name: Amathya
name
             
'Amathya'
age = input("Enter your age: ")
             
Enter your age: 23
age
             
'23'
type(age)
             
<class 'str'>
gpa=float(input("Enter your gpa: "))
             
Enter your gpa: 7.8
gpa
             
7.8
type(gpa)
             
<class 'float'>
'Achyuth Amathya Ram Prakesh'
             
'Achyuth Amathya Ram Prakesh'
'Achyuth Amathya Ram Prakesh'.split(' ')
             
['Achyuth', 'Amathya', 'Ram', 'Prakesh']
'java-python-c-c++-javascrit'
             
'java-python-c-c++-javascrit'
'java-python-c-c++-javascrit'.split('-')
             
['java', 'python', 'c', 'c++', 'javascrit']
names = input("Enter the names: ").split()
             
Enter the names: ram sahith prakesh vamsi rishi
names
             
['ram', 'sahith', 'prakesh', 'vamsi', 'rishi']
products = input("Enter the products: ").split()
             
Enter the products: laptop mouse keyboard charger
products
             
['laptop', 'mouse', 'keyboard', 'charger']
topics = tuple(input("Enter the topics: ").split())
             
Enter the topics: token statement variable comments
topics
             
('token', 'statement', 'variable', 'comments')
op = set(input("Enter the oper: ").split())
             
Enter the oper: in not in is is not and or not
op
             
{'and', 'or', 'is', 'not', 'in'}
marks = input("Enter the marks: ").split()
             
Enter the marks: 34 76 89 21 12
marks
             
['34', '76', '89', '21', '12']
map(int,input("Enter the marks: ").split()
    )
             
Enter the marks: 5 6 7 9 0
<map object at 0x00000274F9E33E00>
list(map(int,input("Enter the marks: ").split())
     )
             
Enter the marks: 1 3 5 85 345
[1, 3, 5, 85, 345]
prices = tuple(map(int,input("Enter the prices: ").split()))
             
Enter the prices: 4356 6758 456 8976 45 87
prices
             
(4356, 6758, 456, 8976, 45, 87)
rating = set(map(int,input("Enter the rating: ").split()))
             
Enter the rating: 4 3 4 5 3 3 2
rating
             
{2, 3, 4, 5}
per = list(map(float,input("Enter the per's : ").split()))
             
Enter the per's : 56.3 23.3 78.9.34.5
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    per = list(map(float,input("Enter the per's : ").split()))
ValueError: could not convert string to float: '78.9.34.5'
per = list(map(float,input("Enter the per's : ").split()))
             
Enter the per's : 34.5 78.9 23.4 56.7
per
             
[34.5, 78.9, 23.4, 56.7]
prices = tuple(map(float,input("Enter the prices: ").split()))
             
Enter the prices: 567 898 3435 878 242 
prices
             
(567.0, 898.0, 3435.0, 878.0, 242.0)
prices = set(map(float,input("Enter the prices: ").split()))
             
Enter the prices: 2535 686 69678 23 4546
prices
             
{4546.0, 2535.0, 69678.0, 686.0, 23.0}
a,b = 10,20
             
a
             
10
b
             
20
a,b = (10,20)
             
a
             
10
b
             
20
a,b = [10,20]
             
a
             
10
b
             
20
username,password = input("Enter the username & password: ").split()))
SyntaxError: unmatched ')'
username,password = input("Enter the username & password: ").split()
Enter the username & password: Amathya 1@2424!0
username
'Amathya'
password
'1@2424!0'
a,b,c,d = list(map(int,input("Enter the 4 sides: ").split()))
Enter the 4 sides: 8 5 3 7
a
8
b
5
c
3
d
7
price,discount = list(map(float,input().split()))
345678 89.0
price
345678.0
discount
89.0
a = eval(input())
34567
a
34567
(3,4,6,7,8,9)
(3, 4, 6, 7, 8, 9)
a
34567
a = eval(input())
{1,4,7,8,9}
a
{1, 4, 7, 8, 9}
type(a)
<class 'set'>
a=eval(input())
43743.654747
a
43743.654747
type(a)
<class 'float'>
a=eval(input())
(2,5,6,7,8,9)
a
(2, 5, 6, 7, 8, 9)
>>> type(a)
<class 'tuple'>
>>> a=eval(input()
...        )
('34,54,76,79,34')
>>> a
'34,54,76,79,34'
>>> type(a)
<class 'str'>
>>> a=eval(input())
(32:43,353:54,564:643)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    (32:43,353:54,564:643)
       ^
SyntaxError: invalid syntax
>>> a=eval(input())
32:56,35:65,89:67
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    32:56,35:65,89:67
      ^
SyntaxError: invalid syntax
>>> a=eval(input())
('46:74,47:38,56:90')
>>> a
'46:74,47:38,56:90'
>>> type(a)
<class 'str'>
>>> a=eval(input())
{3:9,4:7,9:6}
>>> a
{3: 9, 4: 7, 9: 6}
>>> type(a)
<class 'dict'>
>>> a=eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
