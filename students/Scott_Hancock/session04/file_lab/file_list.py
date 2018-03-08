import os

wd = os.getcwd()
for fileName in os.listdir():
    print(wd + '/' + fileName)