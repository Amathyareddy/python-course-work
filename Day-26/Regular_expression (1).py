'''

import re
pattern = '[abc]'
text = 'codegnan'
res = re.match(pattern,text)
print(res.group() if res else "No Match Found")

'''

'''
import re

pattern = '[abc]'
text = 'python version 3.11'

res = re.search(pattern,text)
print(res.group() if res else "No Match Found")
'''

'''
import re

pattern = '[0-9]'
text = 'python version 3.11'

res = re.findall(pattern,text)
print(res)

'''

'''
import re

pattern = '[0-9]'
text = 'python version 3.11'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

'''

'''
import re

pattern = '[a-z]{9}'
text = 'abcdefghi'

res = re.fullmatch(pattern,text)
print(res.group() if res else "No Match Found")

'''

import re

pattern = r'[,a+yn]'
text = 'python:34 mysql : 78 java : 55 html: 45'

res = re.sub(pattern,'**',text)
print(res)



























