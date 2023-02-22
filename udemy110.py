import re

text = "My phone number is 91-9106978750"
phonenum = re.search(r'\d\d-\d\d\d\d\d\d\d\d\d\d',text)
print(phonenum)
print(phonenum.group())
