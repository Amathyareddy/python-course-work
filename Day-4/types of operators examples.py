Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a+b
30
a-b
-10
a/b
0.5
a*b
200
a/b
0.5
9/2
4.5
9//2
4
a//b
0
a**2
100
6**3
216
a%b
10
17%4
1
13%3
1
a
10
a=20
b=10
a+b
30
a>b
True
a<=b
False
10<=b
True
a>=b
True
a==b
False
a!=b
True
y = 5
y
5
y=y+5
y
10
y=y+10
y
20
y += 10
y
30
y+=10
y-=10
y
30
y-=10
y
20
y*=4
y
80
y//=10
y
8
y%=2
y
0
y+=10
y
10
y/=2
y
5.0
a=20
b=10
a
20
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False
#str,list,tuple,set,dict
a = 'python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a
False
l=['java','python','mysql','c++','c','html']
'mysql' in l
True
'javascript' in l
False
'c' not in l
False
t=('laptop','mobile','mouse','keyword')
t
('laptop', 'mobile', 'mouse', 'keyword')
'laptop' in t
True
'mouse' in t
True
'charger' in t
False
t = {1,2,4,7,235,78,23,56}
t
{1, 2, 4, 7, 235, 78, 23, 56}
4 in t
True
5 in t
False
50 not in t
True
d={'egg':8,'oil',:120,'suger',:40,'salt',:30}
SyntaxError: ':' expected after dictionary key
d={'egg':8,'oil':120,'suger':40,'salt':30}
d
{'egg': 8, 'oil': 120, 'suger': 40, 'salt': 30}
'oil' in d
True
120 in d
False
'suger' in d
True
'chilli' in d
False
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
id(l)
2344285430912
id(m)
2344285431168
id(n)
2344285431168
8 & 14
8
8 & 9
8
8 & 7
0
>>> 8 | 7
15
>>> 10 | 11
11
>>> 10^11
1
>>> ~12
-13
>>> ~16
-17
>>> ~19
-20
>>> ~70
-71
>>> 8>>2
2
>>> 15>>1
7
>>> 15>>3
1
>>> 15>>2
3
>>> 16<<1
32
>>> 4<<2
16
>>> a=12
>>> b=12.34
>>> c='python'
>>> print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
a=12b=12.34c=python@@@@
>>> print(f'a= {a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a= {a} b={b} c={c}')
...       
a= 12 b=12.34 c=python
>>> print('a %d b=%.2f c=%s'%(a,b,c))
...       
a 12 b=12.34 c=python
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=12 b=12.34 c=python
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...       
a=python b=12 c=12.34
