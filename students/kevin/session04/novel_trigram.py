#!/usr/bin/env python3
import re
import random
import numpy as np

def read_text(input_file):
    """ Read text from input file """
    with open(input_file, 'r') as file:
        fin = file.read()

    return fin


def split_sentences(string):
    """ Split string by some common sentence endings, returning list of strings """
    # Remove '\n' and rejoin with ' '--this assumes string lines are
    # broken by '\n'
    string = ' '.join(string.split('\n'))

    # TODO Don't split at 'Mr.', 'Ms.', etc.
    sent_seps = ['. ', '? ', '! ']#, '."', '?"', '!"']

    # Split into sentences based on all the sentence-ending punctuation
    # in sent_seps
    for punct in sent_seps:
        if type(string) == str:
            string = string.split(punct)
        else:
            for idx, part in enumerate(string):
                if punct in part:
                    parts = part.split(punct)
                    string[idx] = parts

    return string


def parse_sent(string):
    """ Take a string, parse by words, and return list containing words. """
    return re.findall(r'[\w]+', string)


def create_sent(trigram_dict):
    """ Create and return new sentence based on trigram dict and starting pair. """
    pair = init_pair(trigram_dict)
    new_sent = pair.capitalize()

    while pair in trigram_dict:
        value_list = trigram_dict[pair]
        rand_value = random.randint(0, len(value_list) - 1)
        new_sent += ' ' +  trigram_dict[pair][rand_value]
        
        pair = ' '.join(new_sent.split(' ')[-2:])

    new_sent+='.'

    return new_sent


def init_pair(trigram_dict):
    """ Return psuedorandom key from dict. """
    return random.choice(list(trigram_dict))


def create_par(trigram_dict, min_sent=1, max_sent=15):
    """ Create a paragraph of a psuedorandom number of created sentences. """
    # num_sent = random.randint(min_sent, max_sent)
    num_sent = np.random.choice(list(range(min_sent, max_sent+1)), 1, p=[0.1, 0.2, 0.3, 0.099, 0.08, 0.06, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.001])[0]

    par = '  '
    
    for i in range(num_sent):
        new_sent = ''
        while len(new_sent.split(' ')) < 4:
            new_sent = create_sent(trigram_dict)

        par += new_sent + ' '

    par = par[:-1] + '\n'

    return par


def gen_text(trigram_dict, num_pars=3):
    """ Generate full body of text from trigram analysis. """
    text = ''

    for par in range(num_pars):
        text += create_par(trigram_dict) + '\n'

    return text
    

def gen_trigram(strings):
    """ Peform trigram analysis on input string list and return results as dict.  """
    tri_dict = {}
    for idx, line in enumerate(strings):
        # print(idx, type(line), line)

        if type(line) == str:
            words = parse_sent(line)

        if not words: continue

        if len(words) >= 3:
            for i in range(len(words) - 2):
                pair = ' '.join((words[i], words[i+1]))
                if words[i + 2] == '': continue

                if pair in tri_dict:
                    tri_dict[pair].append(words[i + 2])
                else: tri_dict[pair] = [words[i + 2]]

                i+=1

    return tri_dict


if __name__ == '__main__':
    working_dir = 'books/'
    input_file = 'sherlock_mod.txt'

    
    in_filepath = working_dir + input_file

    fin = read_text(in_filepath)

    sentences = split_sentences(fin)

    trigram_dict = gen_trigram(sentences)

    original_work = gen_text(trigram_dict, num_pars=50)

    original_fname = in_filepath.split('.')
    original_fname.insert(-1, '_fan_fic.')
    original_fname = ''.join(original_fname)

    with open(original_fname, 'w') as file:
        file.write(original_work)
    
