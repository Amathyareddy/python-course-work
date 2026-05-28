Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
t= 999.99
type(t)
<class 'float'>
c = 12+8j
type(c)
<class 'complex'>
s='python'
type(s)
<class 'str'>
s='''sdfghjkl:'''
type(s)
<class 'str'>
s="dfghjkl"
type(s)
<class 'str'>
l=[1,2,3,4]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> id(l)
2044524291648
>>> l.append(50)
>>> l.append(60)
>>> type(l)
<class 'list'>
>>> id(l)
2044524291648

>>> l=['post1.png','reel1.mp4']
>>> l
['post1.png', 'reel1.mp4']
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,2,34,5,6,67)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,6}
>>> type(s)
<class 'set'>
>>> s={45678,546,3456,13423}
>>> s
{3456, 546, 45678, 13423}
>>> d={'name':'abc','age':100,'course':'PFS'}
>>> d
{'name': 'abc', 'age': 100, 'course': 'PFS'}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> a=none
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> a=None
>>> type(a)
<class 'NoneType'>
