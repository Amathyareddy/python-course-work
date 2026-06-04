Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Tuple
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t
(10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[2]
30
t[-2]
40
t[-3]
30
t[-1]
50
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t
(10, 20, 30, 40, 50)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[::-1]
(50, 40, 30, 20, 10)
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
30 in t
True
60 not in t
True
t
(10, 20, 30, 40, 50)
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(10)
1
t.index(10)
0
t= 1,2,3,4,5,6,7
t
(1, 2, 3, 4, 5, 6, 7)
a,b,c=(1,2,3)
a
1
b
2
c
3
a=(1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
z
4
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[2]
3
t[2]=4
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3]
[4, 5, 6]
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s={1,1,1,1,1,1}
s
{1}
s={987,654,345,56,345,1,2,34,6,56}
s
{1, 2, 34, 6, 654, 56, 345, 987}
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add('kjhy')
s
{56.567, 1, 'kjhy'}
s.add([1,2,3,3])
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.add([1,2,3,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3,4))
s
{56.567, 1, 'kjhy', (1, 2, 3, 4)}
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s
{56.567, 1, 'kjhy', (1, 2, 3, 4)}
1 in s
True
2 is s
False
False not in s
True
a= {1,2,3,5,6,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6}
a & b
{8, 6}
a-b
{1, 2, 3, 5, 10}
a-b
{1, 2, 3, 5, 10}
a^b
{1, 2, 3, 5, 7, 9, 10}
# {1} {2} {3} {5}{1,3} {1,2} {8,10}

a <= {1}
False
a>= {1}
True
a <= {1,2,3,4,5,6,8,10,11,12}
True
a >= {6,10,8}
True
a
{1, 2, 3, 5, 6, 8, 10}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 5, 6, 8, 10}
a.add(14)
a
{1, 2, 3, 5, 6, 8, 10, 14}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14}
a.pop()
1
a.pop()
2
a
{3, 5, 6, 8, 10, 11, 12, 13, 14}
a.remove(6)
a
{3, 5, 8, 10, 11, 12, 13, 14}
a.remove(10)
a
{3, 5, 8, 11, 12, 13, 14}
>>> a.discard(6)
>>> a
{3, 5, 8, 11, 12, 13, 14}
>>> a.discard(3)
>>> a
{5, 8, 11, 12, 13, 14}
>>> a.clear()
>>> a
set()
>>> a
set()
>>> a={1,23,4,57,235}
>>> b={1,2,34,4}
>>> a.intersection(b)
{1, 4}
>>> a
{1, 4, 23, 57, 235}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> d=c.copy()
>>> d.add (10)
>>> d
{1, 2, 34, 4, 10, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
