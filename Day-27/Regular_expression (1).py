'''
import re
pattern = r'h.t\b'
text = 'hot hit het hrt hat hate hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)

'''

'''
import re
pattern = r'^h'
text = 'uot hit het hrt hat hate hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)

'''
'''
import re
pattern = r'j$'
text = 'hot hit het hrt hat hate hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)

'''

'''
import re
pattern = r'to?\b'
text = 'too to t toooooooo toooooo'

res = re.findall(pattern,text)
print(res)

'''

'''
import re
pattern = r'(python)'
text = 'pyth pythn python puthoni'

res = re.findall(pattern,text)
print(res)

'''

'''
import re
pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'

text = input("Enter the text:: ")

res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")
'''

'''
import re
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

text = input("Enter the text:: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")

'''

import re
pattern = r'^[a-zA-Z0-9_]{5,15}$'

text = input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")

























