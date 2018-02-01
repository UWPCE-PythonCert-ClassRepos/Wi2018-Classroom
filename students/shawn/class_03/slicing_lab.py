"""
Slicing lab
"""
# slicing 1
def seq_ex(seq):
    """ the first and last items exchanged."""
    r=[]
    try:
        r=seq[-1:] + seq[1:-1]  + seq[0:1]
    except IndexError:
        try:
            r = seq[-1:] +  seq[0:1]
        except:
            return r
    except:
        r=None


    print(r)

# seq_ex([1,2,3,4,5])

#slicing 2
def seq_other(seq):
    """with every other item removed."""
    return seq[::2]

# print(seq_other((1,2,3,4,5)))

def seq_f4(seq):
    """with the first 4 and the last 4 items removed, and then every other item in between."""
    return seq[3:-3:3]

#print(seq_f4([1,3,4,5,5,6,7,8,9,10,11,12,13,14]))

def seq_rev(seq):
    """with the elements reversed (just with slicing)."""
    return seq[::-1]

# print(seq_rev('abcdefg'))

import  math as m
def seq_shift(seq):
    """with the middle third, then last third, then the first third in the new order."""
    r=[]
    spos= m.floor(len(seq)/3)
    epos= spos*2

    c = seq[spos:epos]
    f=seq[0:spos]
    e=seq[-(epos-spos):]

    return c + e + f



print(seq_shift("abcdefghijkl"))

