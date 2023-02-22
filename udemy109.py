text = "The agent phone number is +91-9106978750"
import re
pattern = 'phone'
print(re.search(pattern,text))


text2 = 'The phone number os agent is phone - +91-9134235252'
print(re.search(pattern,text2))
print(re.findall(pattern,text2))