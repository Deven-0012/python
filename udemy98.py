# def cool():
#     def supercool():
#         return 'i am super cool'
#     return supercool()
#
# mynewfunc = cool()
# print(mynewfunc)
#
#
#
# def hello():
#     return 'HI deven'
#
# def other(other_func):
#     print('This is under other function')
#     print(other_func())
#
#
# myfunc = other(hello)
# print(myfunc)






# the first and complicated version for decorated function


def new_decorated_func(original_func):
    def wrap():
        print('Some lines of code before original function')
        original_func()
        print('Some lines of code after original function')

    return wrap()

# def func_need_decoratrion():
#     print('I need to be decorated ')
#
# decorated_func = new_decorated_func(func_need_decoratrion)
# print(decorated_func)



@new_decorated_func
def func_need_decoratrion():
    print('I need to be decorated ')

variable = func_need_decoratrion
print(variable)
