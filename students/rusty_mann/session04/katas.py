#!/usr/bin/env python3

trigram_dict = {}

def get_key(word):
    for akey in trigram_dict:
        if word == akey:
            return akey
    return None

with open('sherlock_small.txt') as f:
    count = 0
    bad_chars = ',.-()'
    text = f.read()
    for c in bad_chars:
        text = text.replace(c, ' ')
    words = text.split()
    for word in range(len(words)-2):
        k = words[word] + " " + words[word+1]
        v = words[count+2]
        akey = get_key(k)
        if akey is None:
            trigram_dict.setdefault(k, [])
        trigram_dict[k].append(v)
        count = count + 1

print(trigram_dict)

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