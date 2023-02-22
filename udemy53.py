# def threechar(text):
#     result = ''
#     for char in text:
#         result += char*3
#     return result
#
# omg = threechar('Hello')
# print(omg)




def spy_game(nums):

    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


result = spy_game([1,2,3,5,6,8,5,0,3,4,6,0,4,7])
print(result)





