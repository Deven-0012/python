# try:
#     result = 10 + '10'
#
# except:
#     print("hey it looks like you have made a mistake in adding")
#
# else:
#     print("Addition went all good")
#     print(result)


try:
    f = open('write file.py','w')
    f.write("Write a test file")

except TypeError:
    print('There is a type error occured')
except :
    print('All other random possible error')

finally:
    print('This will run always')