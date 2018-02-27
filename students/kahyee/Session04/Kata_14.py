import os
import random

file_name = '/sherlock.txt'

book_raw_text = ''

with open(os.getcwd() + file_name, 'r') as f:
	book_raw_text = f.read()

#cleans up text and turns it into a list
bad_characters = ['"', '\n', '--', '(', ')']
for bc in bad_characters:
	book_raw_text = book_raw_text.replace(bc, ' ')
text_list = book_raw_text.split()

trigram_dict = {}

#Turns the list into a trigram dict
for i in range(len(text_list) - 2):
	if text_list[i] + ' ' + text_list[i + 1] in trigram_dict.keys():
		trigram_dict[text_list[i] + ' ' + text_list[i + 1]].append(text_list[i + 2])
	else:
		trigram_dict[text_list[i] + ' ' + text_list[i + 1]] = [text_list[i + 2]]

#Random first two words
text_list = random.choice(list(trigram_dict.keys())).split()

#adjust word count to include first dictionary key
word_count = int(input('how long should the story be?')) - 2

for i in range(word_count):
	next_word_pos = random.randint(0, len(trigram_dict[text_list[-2] + ' ' + text_list[-1]]) - 1)
	text_list.append(trigram_dict[text_list[-2] + ' ' + text_list[-1]][next_word_pos])

print(' '.join(text_list))
