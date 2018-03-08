punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

with open('sherlock_small.txt', 'r') as f:
    contents = f.read()
    text = contents.split()
    map = str.maketrans('', '', punctuation)
    stripped = [words.translate(map) for words in text]
    print(stripped)
    print(text)