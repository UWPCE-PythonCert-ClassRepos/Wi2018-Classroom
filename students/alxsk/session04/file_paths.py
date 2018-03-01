'''
File Paths Exercise
Program prints the full path for all files in the current directory. 
'''
import os


for file in os.listdir(os.curdir):
    print(os.path.abspath(file))