#!/usr/bin/env python3

import random
import os


def read_in(filename):
    '''
    read the contents of a text document from a Project Gutenberg EBook
    param: name of text file
    return: one long string containing entire text of book except table of contents
    '''
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
    '''
    replace punctuation and make list of strings from read_in
    param: string of text
    return: list of strings
    '''
    bad_chars = ",.-\/"
    for c in bad_chars:
        text = text.replace(c, ' ')
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.lower()
    words = text.split()
    for n, word in enumerate(words):
        if word == 'i':
            words[n] = "I"
    return words


def make_trigram(words):
    '''
    generate dictionary of trigrams
    param: list of strings from build_words
    return: dictionary with keys of two word tuples and values of list of possible following words
    '''
    trigram_dict = {}
    for word in range(len(words)-2):
        k = tuple(words[word:word + 2])
        v = words[word+2]
        trigram_dict.setdefault(k, [])
        trigram_dict[k].append(v)
    return trigram_dict


def gen_seed(tri_dict):
    '''
    choose random two word key to begin story
    param: trigram dictionary from make_trigram
    return: two word tuple
    '''
    trigram_list = list(tri_dict)
    seed = random.choice(trigram_list)
    return seed


#def get_rand_val(tri_dict, new_key):
    #val = random.choice(tri_dict[new_key])
    #return val


def get_last_two(sent_str):
    '''
    return tuple containing last two words from sentence
    '''
    new_key = tuple(sent_str[-2:])
    return new_key


def get_next_word(tri_dict, new_key):
    '''
    randomly select next word from list in dictionary value
    param: dictionary and two word look up key
    return: string
    '''
    next_word = random.choice(tri_dict[new_key])
    #new_val = get_rand_val(tri_dict, new_key)
    return str(next_word)


def make_new_story(tri_dict):
    '''
    return new text generated from dictionary of trigrams
    '''
    new_story = []
    for i in range(20):
        sentence = list(gen_seed(tri_dict))
        for j in range(random.randint(2,15)):
            new_pair = get_last_two(sentence)
            sentence.append(get_next_word(tri_dict, new_pair))
        sentence[0] = sentence[0].capitalize()
        sentence[-1] += '.'
        new_story.extend(sentence)
    new_story = " ".join(new_story)
    return new_story


def select_text():
    selection = input("Please enter the name of a text document: ")
    return selection


if __name__ == "__main__":

    filename = select_text()
    infile = read_in(filename)
    raw_words = build_words(infile)
    trigram = make_trigram(raw_words)
    story = make_new_story(trigram)

    print(story)


#print(make_new_story(make_trigram(build_words(read_in('sherlock.txt')))))

