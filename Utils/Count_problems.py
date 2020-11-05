ignoreDirs = ['.git','Utils','Contribution.md','LICENSE','README.md']

import os

os.chdir('D:\Python Projects\Python Practice\Technical_Interview_Practice_Problems')
findIn = [i for i in os.listdir() if i not in ignoreDirs]

Count = 0

print('Counting Files...')

for i in findIn:
    os.chdir(i)
    Count+= len(os.listdir())
    os.chdir('..')

print('Opening README.md...')
    
Readme = open('README.md','r')
content = Readme.read()
Readme.close()

index = content.find('Current Problem Count: **') + 25
endindex = content.find('*',index)
content = content[:index] + str(Count) + content[endindex:]

print('Updating README.md...')

Readme = open('README.md','w')
Readme.write(content)
Readme.close()

print('Done!')