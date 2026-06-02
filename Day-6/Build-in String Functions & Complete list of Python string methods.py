Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min('')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    min('')
ValueError: min() iterable argument is empty
min(s)
' '
max(s)
'y'
ord('a')
97
ord('A')
65
ord('0')
48
ord('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
chr(98)
'b'
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
chr(65)
'A'
S='python Programming'
S.upper()
'PYTHON PROGRAMMING'
S.lower()
'python programming'
S.capitalize()
'Python programming'
S.title()
'Python Programming'
S.swapcase()
'PYTHON pROGRAMMING'
"STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
S
'python Programming'
S.center(38,'*')
'**********python Programming**********'
S.center(28,'-')
'-----python Programming-----'
S.ljust(28,'-')
'python Programming----------'
S.rjust(28,'-')
'----------python Programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
s.find('o')
4
s.find('a')
12
s.rfind('m')
14
s.rfind(g)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.rfind(g)
NameError: name 'g' is not defined
s.rfind('g')
17
s
'python programming'
s.count('y')
1
s.count('a')
1
s.count('o')
2
s.count('g')
2
s
'python programming'
s.index('o')
4
s.rindex('o')
9
#String Testing Methods (Boolean Results)
#Replace & Modify Methods
s
'python programming'
s.replace('python','java')
'java programming'
s.translate('python','xxxxxx')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.translate('python','xxxxxx')
TypeError: str.translate() takes exactly one argument (2 given)
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
'123456 1r5grammi6g'
s.translate(s.maketrans('python','678921'))
'678921 6r2grammi1g'
#Splitting & Joining Methods
s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
g='sdfgh'
g='''dsfghjk'''
g='''dfghjk'''
fghjkl;
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    fghjkl;
NameError: name 'fghjkl' is not defined
g='''dfghjk
fghjkl;
gfhjkl
drtyuhj'''
g
'dfghjk\nfghjkl;\ngfhjkl\ndrtyuhj'
g.splitlines
<built-in method splitlines of str object at 0x0000026509733C30>
g
'dfghjk\nfghjkl;\ngfhjkl\ndrtyuhj'
g.splitlines(1)
['dfghjk\n', 'fghjkl;\n', 'gfhjkl\n', 'drtyuhj']
l=['java','python','javascript','c','c++']
''.join(1)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
>>> ''.join(l)
'javapythonjavascriptcc++'
>>> '-'.join(l)
'java-python-javascript-c-c++'
>>> '@'.join(l)
'java@python@javascript@c@c++'
>>> ' '.join(l)
'java python javascript c c++'
>>> ','.join(l)
'java,python,javascript,c,c++'
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> s.partition('-')
('java,python,javascript,c,c++', '', '')
>>> s
'java,python,javascript,c,c++'
>>> s.partition('-')
('java,python,javascript,c,c++', '', '')
>>> #Encoding & Decoding Methods
>>> Encoding -> Converts the string to bytes
SyntaxError: invalid syntax
>>> #Encoding -> Converts the string to bytes
>>> #Decodiing -> Converts bytes back to string
>>> t = "Hello 🙂"
>>> t.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.encode()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    b'Hello \xf0\x9f\x99\x82'.encode()
AttributeError: 'bytes' object has no attribute 'encode'. Did you mean: 'decode'?
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
>>> t = "9381592725"
>>> t.encode()
b'9381592725'
>>> b'9381592725'.decode()
'9381592725'
