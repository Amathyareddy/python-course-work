Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='python programming'
>>> len(s)
18
>>> sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
>>> min('')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    min('')
ValueError: min() iterable argument is empty
>>> min(s)
' '
>>> max(s)
'y'
>>> ord('a')
97
>>> ord('A')
65
