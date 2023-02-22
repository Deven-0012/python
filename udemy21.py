my_list = ['deven',100,234.344]
print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[0:2])

mylist = ['one', 'Two','Three']

print(my_list + mylist)

newlist = mylist + my_list

newlist[0] = 'Hello'
print(newlist)

newlist.append('Hey')
print(newlist)

newlist.pop()
print(newlist)

newlist.pop(2)
print(newlist)


numlist = [4,2,8,1,5]
alphalist = ['g','f','a','t']

print(numlist)
numlist.sort()
print(numlist)
alphalist.sort()
print(alphalist)