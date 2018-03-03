def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

def every_other_item_removed(seq):
    return seq[::2]

def remove_first_last_4_then_every_other(seq):
    return seq[4:-4][::2]

def reverse(seq):
    return seq[::-1]

def middle_last_first_third(seq):
    if len(seq)%3==0:
        return seq[len(seq)//3:2*len(seq)//3]+seq[(2*len(seq)//3):]+seq[:len(seq)//3]
    else:
        print("Not divsible into 3 equal parts that can be rearranged")



