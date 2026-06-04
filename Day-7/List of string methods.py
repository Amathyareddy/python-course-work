Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='    hello     world  '
s
'    hello     world  '
s.strip()
'hello     world'
s.lstrip()
'hello     world  '
s.rstrip()
'    hello     world'
s='    Achuyth    Amathya    '
s
'    Achuyth    Amathya    '
s.strip()
'Achuyth    Amathya'
s.lstrip()
'Achuyth    Amathya    '
s.rstrip()
'    Achuyth    Amathya'
#String Testing Methods (Boolean Results
)
SyntaxError: unmatched ')'
>>> #String Testing Methods (Boolean Results)
>>> s='strings.py'
>>> s
'strings.py'
>>> s.startswith('str')
True
>>> s.startswith('ghf')
False
>>> s.endswith('py')
True
>>> s.endswith('er')
False
>>> 'DSHFKDHBFVIUEGFEWI'.isalpha()
True
>>> 'ramakanth@135516'.isalpha()
False
>>> '2345678'.isalnum()
True
>>> 'sdfugjkggnljh'.isalnum()
True
>>> 'awufjiesfi'.isalnum()
True
>>> 'prakash'.islower()
True
>>> 'achyuth@1324'.islower()
True
>>> 'RAMAKANTH@454678^%&*^'.isupper()
True
>>> ' '.isspace()
True
>>> 'hello    '.isspace()
False
>>> 'Python Java C++'.istitle()
True
>>> 'Python java c c++'istitle()
SyntaxError: invalid syntax
>>> 'Python java c c++'.istitle()
False
>>> 'python_name'.isidentifier()
True
>>> 'py@1431'.isidentifier()
False
>>> '232379.4749'.isdecimal()
False
>>> '123'.isdecimal()
True
