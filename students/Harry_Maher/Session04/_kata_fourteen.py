#!/usr/bin/env python3

"""
Kata Fourteen: Tom Swift Under Milk Wood

For this kata, try implementing a trigram algorithm that generates a couple of 
hundred words of text using a book-sized file as input. Project Gutenberg is 
a good source of online books


I found a book entitled: THE “SURE to RISE” COOKERY BOOK. An old pun 
from a 1914! Hopefully it spits out a good bread recipe...

Here's my favorite recipe excerpt so far:
DATE CAKE. ½ lb. dates 1½ breakfastcups of flour piled up equal 1 lb. of steak ½ lb. flour 1 teaspoonful flour 1 pint milk

input: book.txt 
output: my_new_book.txt (300 words--not a real book.)


"""
import sys
import random

def main(book_input):
    """ Taking a book as input, implement a trigram algorithm that generates 300 words of text using a book-sized file as input"""
    trigram_d = trigram_dictionary_builder(book_input)
    book_writer(trigram_d)

def book_reader(book_input):
    """reads a short book, puts it into a list"""
    with open(book_input, "r", encoding="utf-8") as f:
        words = f.read().split()
    return words


def trigram_dictionary_builder(book_input):
    """builder dictionary from the list of words from book_reader"""
    words = book_reader(book_input)
    trigram_d = {}
    for i, word in enumerate(words[:-2]):  #cutting off the last two words to avoid error, kinda hack-y
        word_pair = word+" "+words[i+1]
        if word_pair not in trigram_d:
            trigram_d[word_pair] = [words[i+2]]
        else:
            trigram_d[word_pair] += [words[i+2]]
    return trigram_d

def book_writer(trigram_d):
    """keeps adding text until word count is 300, then puts the text into my_new_book.txt"""
    text_output = list(random.choice(list(trigram_d.keys())).split())
    while len(text_output) < 301:
        try:
            text_output += [random.choice(trigram_d[" ".join(text_output[-2:])])]
        except:
            text_output += list(random.choice(list(trigram_d.keys())).split())
    with open("my_new_book.txt", "w+") as f:
        f.write(" ".join(text_output))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        book_input = sys.argv[1]
    else:
        book_input = "book.txt"
    main(book_input)