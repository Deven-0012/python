# def myfunc(*args):
#     return sum(args) * 0.05
#
# result = myfunc(100,200,34,345,567,789,789,324)
# print(result)

 
def myfunc(*args,**kwargs):
    print("I would like {} {}".format(args[0],kwargs['food']))

result = myfunc(30,40,60,234,4,56,678,animal = 'dog',food = 'pizza',bike = 'Re')
print(result)

