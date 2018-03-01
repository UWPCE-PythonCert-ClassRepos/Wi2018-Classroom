#!/usr/bin/env python
from io import open
import sys
import random
import string


"""
# Programming in python B Winter 2018
# February 15, 2017
# Kata trigram codingSession 4
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom
I will see if I can figure this out with the solution to review
"""

infilename = u"sherlock.txt"


def make_words(text):
    """take out the punctuation and other stuff from a string"""
    table = {}
    punctuation = string.punctuation.replace("'", "")  # keep apostropies
    punctuation = string.punctuation.replace("-", "")  # keep hyphenated words
    table = dict([(ord(c), None) for c in punctuation])
# Make everything lower case
    text = text.lower()
# Split into separate make_words
    words = text.split()
    words = [word for word in words if word != "'"]
    words2 = []
    for word in words:
        if word != "'":  # remove quote by itself
            # "i" by itself should be capitalized
            words2.append("I" if word == 'i' else word)
    # could be done with list comprehension too -- next week!
# words2 = [("I" if word == 'i' else word) for word in words if word != "'"]
    return words2
    return words
    print(words)


def read_in_data(infilename):
    infile = open(infilename, 'r')
    # strip out the header, table of contents, etc.
    for i in range(61):
        infile.readline()
    full_text = []
    # read the rest of the file line by line
    for line in infile:
        if line.startswith(u"End of the Project Gutenberg EBook"):
            break
        full_text.append(line)

    # put all the lines together into one big string:
    return u" ".join(full_text)


def build_trigram(words):
    """build a trigram dict from the passed-in text"""
    word_pairs = {}
    # loop through the words
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])  # a tuple so it can be a key in the dict
        follower = words[i + 2]
        word_pairs.setdefault(pair, []).append(follower)
    return word_pairs


def build_text(word_pairs):
    """build some new text from the word_pair dict supplied"""
    new_text = []
    for i in range(30):  # do thirty sentences
        # pick a word pair to start the sentence
        sentence = list(random.choice(word_pairs.keys()))
        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(word_pairs[pair]))
        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        # Add the period
        sentence[-1] += u"."
        new_text.extend(sentence)
    new_text = " ".join(new_text)
    return new_text


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)
    print(new_text)
