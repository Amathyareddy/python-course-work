Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming lang'
s
'python programming lang'
type(s)
<class 'str'>
s=''
s
''
a='codegnan'
b='pfs'
a+b
'codegnanpfs'
'codegnan'*5
'codegnancodegnancodegnancodegnancodegnan'
'python '*6
'python python python python python python '
'python code '*5
'python code python code python code python code python code '
names = 'subbu narendra sahith vamsi rishi harish'
names
'subbu narendra sahith vamsi rishi harish'
names[:5]
'subbu'
names[6:14]
'narendra'
names[15:21]
'sahith'
names[22:27]
'vamsi'
>>> names[28:33]
'rishi'
>>> names[34:
...       ]
'harish'
>>> names
'subbu narendra sahith vamsi rishi harish'
>>> names[-6:]
'harish'
>>> names[-12:-7]
'rishi'
>>> names[-6:]
'harish'
>>> names[4::-1]
'ubbus'
>>> names[13:5:-1]
'ardneran'
>>> names[::-1]
'hsirah ihsir ismav htihas ardneran ubbus'
>>> names[26:21:-1]
'ismav'
>>> 'subbu' in names
True
>>> 'dinesh' in names
False
>>> 'akhil' not names
SyntaxError: invalid syntax
>>> 'akhil' not in names
True
>>> names
'subbu narendra sahith vamsi rishi harish'
>>> len(names)
40
>>> names.upper()
'SUBBU NARENDRA SAHITH VAMSI RISHI HARISH'
>>> names.lower()
'subbu narendra sahith vamsi rishi harish'
>>> max(names)
'v'
>>> min(names)
' '
>>> sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'd', 'e', 'h', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'm', 'n', 'n', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 't', 'u', 'u', 'v']
