import string

def createTrigram(filename):
    """
    Function reads in the file data and creates a trigram. The punctuation is removed first
    followed by the newlines.
    :param filename: the file data we read in. Contains text
    """
    #Removes punctuation from text. Replaces all punctuation with a space
    no_punctuation_data = str.maketrans(string.punctuation, ' '* len(string.punctuation))
    new_file_data = filename.translate(no_punctuation_data)
    #Replaces all carriage returns with a space
    new_file_data = new_file_data.replace('\n', ' ')
    #Create list for each word and space found in text
    word_list = new_file_data.split(" ")
    trigram_dict = {}
    #Remove spaces from list
    copy_word_list = []
    new_key = None
    for word in word_list:
        if word == ' ' or word == '':
            continue
        else:
            copy_word_list.append(word)
    for key_index,key_word in enumerate(copy_word_list):
        #Detects if we are at the last two elements in the list
        if key_index + 1 < len(copy_word_list) - 1:
            new_key = key_word + ' ' + copy_word_list[key_index + 1]
            if new_key in trigram_dict:
                trigram_dict[new_key].append(copy_word_list[key_index+2])
            else:
                trigram_dict[new_key] = [copy_word_list[key_index+2]]
    print(trigram_dict)


with open("sherlock_small.txt", "r") as f:
    file_data = f.read()
f.close()
createTrigram(file_data)
