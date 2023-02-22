# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
#
#
# # Driver function
# List = [23,65]
# pos1, pos2 = 0,1
#
# print(swapPositions(List, pos1, pos2))

# def largestnum(mylist):
#     a = max(mylist)
#     return a
# z = largestnum([1,2,3,4,5,6,7,8,9])
# print(z)


# s = 'Deven is a good boy'
# a = s[::-1]
# print(a)


# def checkob(string):
#     p = set(string)
#     s = {'0','1'}
#     if s==p or p=={'0'} or p=={'1'}:
#         print('YES')
#     else:
#         print('NO')
#
# a = checkob('01011101101')
# print(a)




# list_1 = [2,34,56,78,1,69]
# list_2 = [45,67,89,0,1,69]
# temp = []
# for elements in list_1:
#     if elements not in list_2:
#         temp.append(elements)
#         print(temp)



# tup = (1,2,3,4,5,6,7,1,1)
# for i in tup:
#     if tup.count(i) > 1:
#         print('The element {} is repeated'.format(i))


def Remove(tuples):
    for i in tuples:
        if (len(i) == 0):
            tuples.remove(i)
    return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))



