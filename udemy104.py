from collections import Counter

mylist = [1,2,333,444,5,5,5,4,4,333,444,1,1]
print(Counter(mylist))

mylist1 = [1,2,333,444,5,5,5,4,4,333,444,1,1,'f','g','g','g','w']
print(Counter(mylist1))

print(Counter('ssfefvsvuhacachauvbqkjvbdvhsdvsdvnmsbvahalcxjvbsvnsdnv sheqiandcsdv'))


letter = 'Deven is a very good boy his clg name is vgec and his school name is amrita vidyalayam and his mother name is smita and is father name is jaimin'
c = Counter(letter)
print(c)

print(c.most_common())