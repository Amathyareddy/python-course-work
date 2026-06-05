Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[[1,2,3,4]]='List'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[[1,2,3,4]]='List'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d
{1: 1, 23: 23.4}
d[3]='fdghjk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fdghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={'ramakanth':89,'prakash':76,'subbu':90,'achyuth':98,'amathya':95}
d['achyuth']
98
d['ramakanth']
89
d['prakash']
76
d['naresh']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d['naresh']
KeyError: 'naresh'
d.get['naresh']
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d.get['naresh']
TypeError: 'builtin_function_or_method' object is not subscriptable
d.get('naresh')
d.get('ramakanth')
89
d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95}
'prakash' in d
True
'ramakanth' in d
True
'sahith' not in d
True
d.keys()
dict_keys(['ramakanth', 'prakash', 'subbu', 'achyuth', 'amathya'])
d.values()
dict_values([89, 76, 90, 98, 95])
d.items()
dict_items([('ramakanth', 89), ('prakash', 76), ('subbu', 90), ('achyuth', 98), ('amathya', 95)])
sorted(d)
['achyuth', 'amathya', 'prakash', 'ramakanth', 'subbu']
max(d)
'subbu'
min(d)
'achyuth'
len(d)
5
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95}
>>> d['rishi']=86
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86}
>>> d.update({'praneeth':92,'naresh':99})
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86, 'praneeth': 92, 'naresh': 99}
>>> d.popitem()
('naresh', 99)
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86, 'praneeth': 92}
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
('praneeth', 92)
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86}
>>> d.pop('prakash')
76
>>> d
{'ramakanth': 89, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86}
>>> del d['amathya']
>>> d
{'ramakanth': 89, 'subbu': 90, 'achyuth': 98, 'rishi': 86}
>>> d.clear()
>>> d
{}
>>> d
{}
>>> d={'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86, 'praneeth': 92, 'naresh': 99}
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86, 'praneeth': 92, 'naresh': 99}
>>> d.setdefault('rishi',0)
86
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86, 'praneeth': 92, 'naresh': 99}
>>> d.setdefault('satish',0)
0
>>> d
{'ramakanth': 89, 'prakash': 76, 'subbu': 90, 'achyuth': 98, 'amathya': 95, 'rishi': 86, 'praneeth': 92, 'naresh': 99, 'satish': 0}
>>> KeyboardInterrupt
