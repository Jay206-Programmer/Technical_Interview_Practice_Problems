ignoreDirs = ['.git','Utils','Contribution.md','LICENSE','README.md']

import os

findIn = [i for i in os.listdir() if i not in ignoreDirs]

Count = 0

for i in findIn:
    os.chdir(i)
    Count+= len(os.listdir())
    os.chdir('..')
    
Readme = open('README.md','r')
content = Readme.read()
Readme.close()

index = content.find('Current Problem Count: **') + 25
content = content[:index] + str(Count) + content[index:]

Readme = open('README.md','w')
Readme.write(content)
Readme.close()