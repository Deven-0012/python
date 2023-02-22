import os

f = open('gg.txt','w+')
f.write('This is a gg string')
f.close()
print(os.listdir('C:\\Users'))

print(os.getcwd())

import send2trash
send2trash.send2trash('gg')