import re

txt = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Haha

MetaCharecterset (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr.Schafer
Mr smith
Mr. Robinson
Mrs. T
'''

snt="Start a sententence then bring it to the end"

print(r'\tTab')

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(txt)

for match in matches:
    print(match)

print(txt[1:4])