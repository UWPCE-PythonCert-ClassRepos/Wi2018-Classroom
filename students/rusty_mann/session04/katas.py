#!/usr/bin/env python3


import random
import os



def read_in(filename):
    with open(filename, 'r') as f:
        for i in range(61):
            f.readline()
        text = []
        for line in f:
            if line.startswith("End of the Project Gutenberg EBook"):
                break
            text.append(line)
    return " ".join(text)


def build_words(text):
    bad_chars = ",.-(\)/"
    #text = f.read()
    for c in bad_chars:
        text = text.replace(c, ' ')
        text = text.lower()
    words = text.split()
    for n, word in enumerate(words):
        if word == 'i':
            words[n] = "I"
        #little_i = 'i'
        #for i in little_i:
            #word = word.replace(i, 'I')
        #else:
            #word
    #for word in words:
        #if word != "'":
    return words


def make_trigram(words):
    trigram_dict = {}
    #count = 0
    for word in range(len(words)-2):
        k = tuple(words[word:word + 2])
        v = words[word+2]
        #akey = get_key(k, trigram_dict)
        #if akey is None:
        trigram_dict.setdefault(k, [])
        trigram_dict[k].append(v)
        #count = count + 1
    return trigram_dict


def gen_seed(tri_dict):
    ''' '''
    trigram_list = list(tri_dict)
    seed = random.choice(trigram_list)
    return seed


def get_rand_val(tri_dict, new_key):
    val = random.choice(tri_dict[new_key])
    return val


def get_last_two(new_str):
    new_key = tuple(new_str[-2:])
    return new_key


def get_new_word(tri_dict, new_key):
    new_val = get_rand_val(tri_dict, new_key)
    return str(new_val)


def make_new_story(tri_dict):
    new_story = []
    for i in range(20):
        sentence = list(gen_seed(tri_dict))
        for j in range(random.randint(2,15)):
            new_pair = get_last_two(sentence)
            sentence.append(get_new_word(tri_dict, new_pair))
        sentence[0] = sentence[0].capitalize()
        sentence[-1] += '.'
        new_story.extend(sentence)
    new_story = " ".join(new_story)
    return new_story

make_new_story
    #new_word = get_new_word(story_str)
    #if new_word != None:
        #story_str = '{:s} {:s}'.format(story_str, new_word)
        #story_str = story_str + " " + new_word
    #else:
        #if new_word == None:
            #break
    #return story_str
#make_new_story(story_str)

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