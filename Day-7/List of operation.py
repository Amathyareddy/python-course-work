Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4]
m=[7,5,4,3]
l+m
[1, 2, 3, 4, 7, 5, 4, 3]
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,50]
l[4]
50
l[2]
30
l[0]
10
l[1]
20
l[-1]
50
l[-3]
30
l[-4]
20
l[1:4]
[20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 in l
True
30 in l
True
60 in l
False
80 not in l
True
40 in l
True
l
[10, 20, 30, 40, 50]
l[1]=70
l
[10, 70, 30, 40, 50]
id(l)
2954680738880
l[4]=100
l
[10, 70, 30, 40, 100]
l.append(120)
l
[10, 70, 30, 40, 100, 120]
l.append(400)
l
[10, 70, 30, 40, 100, 120, 400]
l.insert(4,50)
l
[10, 70, 30, 40, 50, 100, 120, 400]
l.extend[80,90,110]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l.extend[80,90,110]
TypeError: 'builtin_function_or_method' object is not subscriptable
l.extend([80,90,110])
l
[10, 70, 30, 40, 50, 100, 120, 400, 80, 90, 110]
l.pop()
110
l
[10, 70, 30, 40, 50, 100, 120, 400, 80, 90]
l.pop(3)
40
l
[10, 70, 30, 50, 100, 120, 400, 80, 90]
l.remove(50)
l
[10, 70, 30, 100, 120, 400, 80, 90]
l.remove(10)
l
[70, 30, 100, 120, 400, 80, 90]
del l[1]
l
[70, 100, 120, 400, 80, 90]
del l[2]
l
[70, 100, 400, 80, 90]
l.clear()
l
[]
id(l)0
SyntaxError: invalid syntax
id(l)
2954680738880
l=[212,300,700,7777,65,77,8,8,99,998,900]
l
[212, 300, 700, 7777, 65, 77, 8, 8, 99, 998, 900]
sorted(l)
[8, 8, 65, 77, 99, 212, 300, 700, 900, 998, 7777]
l.sort()
l
[8, 8, 65, 77, 99, 212, 300, 700, 900, 998, 7777]
min(l)
8
>>> max(l)
7777
>>> l.reverse()
>>> l
[7777, 998, 900, 700, 300, 212, 99, 77, 65, 8, 8]
>>> sorted(l.reverse=True)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> sorted(l.reverse=True)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> sorted(l,reverse=True)
[7777, 998, 900, 700, 300, 212, 99, 77, 65, 8, 8]
>>> l.index(2)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l.index(2)
ValueError: list.index(x): x not in list
>>> l
[7777, 998, 900, 700, 300, 212, 99, 77, 65, 8, 8]
>>> l.index(2)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l.index(2)
ValueError: list.index(x): x not in list
>>> l.index(900)
2
>>> l.index(99)
6
>>> l.count(8)
2
>>> l.count(99)
1
>>> l.count(700)
1
>>> l
[7777, 998, 900, 700, 300, 212, 99, 77, 65, 8, 8]
>>> len(l)
11
>>> sum(l)
11144
>>> # 0 0.0 '' [] {} () set() False
>>> any([1,2,4,5,5,0,0,0,0,0])
True
>>> all([1,2,4,5,5,0,0,0,0,0])
False
