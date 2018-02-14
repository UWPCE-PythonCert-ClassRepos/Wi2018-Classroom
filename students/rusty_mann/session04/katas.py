#!/usr/bin/env python3
import random


trigram_dict = {}

def get_key(word):
    for akey in trigram_dict:
        if word == akey:
            return akey
    return None

with open('file_to_move.txt') as f:
    count = 0
    bad_chars = ',.-()'
    text = f.read()
    for c in bad_chars:
        text = text.replace(c, ' ')
    words = text.split()
    for word in range(len(words)-2):
        k = words[word] + " " + words[word+1]
        v = words[word+2]
        akey = get_key(k)
        if akey is None:
            trigram_dict.setdefault(k, [])
        trigram_dict[k].append(v)
        count = count + 1

#print(trigram_dict)

trigram_list = list(trigram_dict)
#print(trigram_list)

def gen_seed():
    seed = random.choice(trigram_list)
    return seed

def get_rand_val(new_key):
    for akey in trigram_dict:
        if new_key == akey:
            val = random.choice(trigram_dict[akey])
            return val

def get_last_two(new_str):
    word_list = new_str.split()
    new_key = word_list[-2] + " " + word_list[-1]
    return new_key

def get_new_word():
    new_key = get_last_two(story_str)
    if new_key is None:
        new_key = gen_seed()
    new_val = get_rand_val(new_key)
    return str(new_val)

story_str = " "
print(story_str)
seed_str = gen_seed()
print(seed_str)
story_str = story_str+seed_str
print(story_str)
#def make_new_story():
    #story_str = story_str + get_new_word()
    #return story_str

#while True:
new_word = get_new_word()
story_str = story_str + " " + new_word
print(story_str)
#else:
    #False
    #make_new_story()

    #new_str = new_str + get_rand_val(get_last_two(new_str))




#with open('new_text', 'w') as f:
    #f.write()

"""
for key in dict:
    choose random key as seed
    write to new file 
    and append a random word from value list 
read in new file:
    select last two words from string 
    and search trigram dict keys for match
    if match:
        append random word from value list 
repeat
"""