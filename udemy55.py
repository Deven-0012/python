# def square(num):
#     return (num**2)
#
#
#
# # result = square(46)
# # print(result)
#
# my_num = [2,3,4,5,6,7,8,9]
# for items in map(square,my_num):
#     print(items)




# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'Even'
#     else:
#         return mystring[0]
#
# names = ['Deven','Andy','Jett']
#
# result = list(map(splicer,names))
# print(result)


def check_even(num):
    return num % 2 == 0

my_num = [4,6,66,3,9]

result = list(filter(check_even,my_num))
print(result)


















