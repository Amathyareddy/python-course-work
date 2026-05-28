Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
float(b)
10.5
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
complex(c)
(2+3j)
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
d=(1,2,3,4,5)
int(d)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
s='python'
a='4356789'
b='34567.546780'
int(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
4356789
int(b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '34567.546780'
float(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(a)
4356789.0
float(b)
34567.54678
complex(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(a)
(4356789+0j)
complex(b)
(34567.54678+0j)
list(s)
['p', 'y', 't', 'h', 'o', 'n']
list(a)
['4', '3', '5', '6', '7', '8', '9']
list(b)
['3', '4', '5', '6', '7', '.', '5', '4', '6', '7', '8', '0']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
tuple(a)
('4', '3', '5', '6', '7', '8', '9')
tuple(b)
('3', '4', '5', '6', '7', '.', '5', '4', '6', '7', '8', '0')
set(s)
{'p', 'h', 'o', 'y', 'n', 't'}
set(a)
{'5', '6', '8', '3', '9', '4', '7'}
set(b)
{'5', '.', '6', '0', '8', '3', '4', '7'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(a)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(s)
True
>>> bool(a)
True
>>> bool(b)
True
>>> l=[1,2,3,4,5,6,7,8]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
>>> str(l)
'[1, 2, 3, 4, 5, 6, 7, 8]'
>>> list(l)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> tuple(l)
(1, 2, 3, 4, 5, 6, 7, 8)
>>> set(l)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
