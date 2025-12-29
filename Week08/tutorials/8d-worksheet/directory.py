import os

newdir = 'test'
if newdir not in os.listdir():
    os.mkdir(newdir)

os.chdir(newdir)
newdirs = ['test1', 'test2', 'test3']
for d in newdirs:
    os.mkdir(d)

print(os.listdir())