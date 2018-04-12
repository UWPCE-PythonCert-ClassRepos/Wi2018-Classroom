import random

text = ("One night--it was on the twentieth of March, 1888--I was "
"returning from a journey to a patient (for I had now returned to "
"civil practice), when my way led me through Baker Street. As I "
"passed the well-remembered door, which must always be associated "
"in my mind with my wooing, and with the dark incidents of the "
"Study in Scarlet, I was seized with a keen desire to see Holmes "
"again, and to know how he was employing his extraordinary powers. "
"His rooms were brilliantly lit, and, even as I looked up, I saw "
"his tall, spare figure pass twice in a dark silhouette against "
"the blind. He was pacing the room swiftly, eagerly, with his head "
"sunk upon his chest and his hands clasped behind him. To me, who "
"knew his every mood and habit, his attitude and manner told their "
"own story. He was at work again. He had risen out of his "
"drug-created dreams and was hot upon the scent of some new "
"problem. I rang the bell and was shown up to the chamber which "
"had formerly been in part my own.")
words = text.split()
pairs = dict()
newtext = ""
newkey = ""

for idx, word in enumerate(words):
    if idx == len(words) - 2:
        break
    pairs.setdefault("{:s} {:s}".format(words[idx], words[idx+1]), list()).append(words[idx+2])

print(pairs)

newkey, newvalue = random.choice(list(pairs.items()))
newtext += newkey + " " + random.choice(newvalue)
newkey = " ".join(newtext.split(' ')[-2:])

while True:
    try:
        newvalue = random.choice(pairs[newkey])
    except KeyError:
        break
    newtext += " " + newvalue
    newkey = " ".join(newtext.split(' ')[-2:])

print(newtext)

