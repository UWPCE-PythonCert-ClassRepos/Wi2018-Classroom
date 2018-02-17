import os
import random

file_name = '/tester.txt'

book_raw_text = ''

with open(os.getcwd() + file_name, 'r') as f:
	book_raw_text = f.read()

print(repr(book_raw_text))