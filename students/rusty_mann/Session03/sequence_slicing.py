
def switch_first_last(seq):
    mid = seq[1:-1]
    new = seq[-1:] + mid + seq[:1]
    return new

#print(switch_first_last("this is a string"))
#print(switch_first_last([1,2,3,4,5,6,7,8,9,0]))
#print(switch_first_last((1,2,3,4,5,6,7,8,9,0)))


def every_other(seq):
    return seq[::2]

#print(every_other("this is a string"))
#print(every_other([1,2,3,4,5,6,7,8,9,0]))


def remove_four(seq):
    seq = seq[4:-4]
    return seq[::2]

print(remove_four("0000102030405060708090000"))
print(remove_four([0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0,0,0]))
print (remove_four((0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0,0,0)))

def reversed(seq):
    return seq[::-1]

#print(reversed("this is a string"))
#print(reversed([1,2,3,4,5,6,7,8,9,0]))
