"""
This Python module will (if possible) standardize the form of 
Indo-European roots from lemma entries in 'brilldictionary.db' and then
find and list any other entries in the database that are associated 
with the same root
"""

from operator import itemgetter
from peewee import *

db = SqliteDatabase('brilldictionary.db')

class BaseModel(Model):
    class Meta:
        database = db

class Lemmas(BaseModel):
    """
    This class defines Lemma, which maintains details of an entry in an 
    etymological dictionary
    """
    id = CharField(primary_key = True, max_length = 11)
    language = CharField(max_length = 2)
    lemma_name = CharField(max_length = 100)
    lemma_long = TextField()
    grammar = TextField()
    forms = TextField()
    etymology = TextField()
    compounds = TextField()
    derivatives = TextField()
    html = TextField()

class Meanings(BaseModel):
    """
    This class defines Meaning, which maintains details of any meanings
    associated with a Lemma
    """
    id = IntegerField(primary_key = True)
    lemma_id = ForeignKeyField(Lemmas)
    meaning = TextField()

class Material(BaseModel):
    """
    This class defines Material, which maintains details of words 
    associated with a Lemma in the language of the dictionary and/or any 
    cognate languages
    """
    id = IntegerField(primary_key = True)
    lemma_id = ForeignKeyField(Lemmas)
    type = CharField(max_length = 50)
    language = CharField(max_length = 50)
    data = TextField()

def parse(rootinput):

    mapping = {
        ' ':((' '),''),
        '*':(('*'),''),
        'IE?':(('IE?'),''),
        'IE':(('IE'),''),
        'H':(('H','H2,3'),'H'),
        'h̥':(('h̥'),'h'),
        'h₁':(('h´1','h1','h₁','H₁','H1'),'h₁'),
        'h₂':(('h´2','h2','h₂','H₂','H2'),'h₂'),
        'h₃':(('h´3','h3','h₃','H₃','H3'),'h₃'),
        'gʷʰ':(('gwh','ghw','gʷʰ','gʰʷ'),'gʷʰ'),
        'bʰ':(('bh','bʰ'),'bʰ'),
        'dʰ':(('dh','dʰ'),'dʰ'),
        'gʰ':(('gh','gʰ'),'gʰ'),
        'ǵʰ':(('ǵh','ǵʰ','g\'h','g´h'),'ǵʰ'),
        'gʷ':(('gw','gʷ'),'gʷ'),
        'b':(('b'),'b'),
        'd':(('d'),'d'),
        'g':(('g'),'g'),
        'ǵ':(('ǵ','g\'','g´'),'ǵ'),
        'kʷ':(('kw','kʷ'),'kʷ'),
        'p':(('p'),'p'),
        't':(('t'),'t'),
        'k':(('k'),'k'),
        'ḱ':(('ḱ','k\'','k´'),'ḱ'),
        's':(('s'),'s'),
        'm':(('m'),'m'),
        'n':(('n','n̥'),'n'),
        'l':(('l','ĺ'),'l'),
        'r':(('r','ŕ'),'r'),
        'e':(('e','é','ē','ḗ'),'e'),
        'o':(('o','ó','ō'),'o'),
        'i':(('i','y','i̯','í'),'i'),
        'u':(('u','w','u̯','ú'),'u'),
    }

    for key, value in mapping.items():
        for i in value[0]:
            rootinput = rootinput.replace(i, value[1])

    rootinput = rootinput.split('-')[0].split(',')[0].split('\'')[0]

    return rootinput

def printlemmas():

    query = (Lemmas
            .select(Lemmas, Material)
            .join(Material)
            .where(Material.type == 'origin'))

    '''
    START TO DO CORRELATION OF ROOTS AND LEMMATA HERE (BY USING A DICT?)
    '''
    result = {lemma.lemma_name:parse(lemma.material.data) for lemma in query}

    for x in sorted(result.items(), key=itemgetter(1)):
        print(x)

if __name__ == '__main__':

    while True:
        rootinput = input("Enter IE root: ")
        if rootinput == 'q':
            printlemmas()
            break
        else:
            print(parse(rootinput))
            print()