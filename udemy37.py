# # generator are built in it works like indexing
# for num in range(5,20,3):
#     print(num)

# we can also do indexing counting in python

# letter = "Hello there"
# for num in enumerate(letter):
#     print(num)
# It basically does counting of your enntered string



# mylist1 = [1,2,3]
# mylist2 = ['A','B','C']
# for items in zip(mylist1,mylist2):
#     print(items)


from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

from random import randint

print(randint(0,100))