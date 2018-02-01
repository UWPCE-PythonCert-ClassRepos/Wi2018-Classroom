def exchange_first_last(seq):
    return seq[-1:] + seq[1:len(seq)-1] + seq[:1]

def remove_every_other(seq):
    return seq[::2]

def remove_4_then_every_other(seq):
    return seq[4:][:-4][::2]

def reverse(seq):
    return seq[::-1]

def thirds(seq):
    fthirdindex = round(len(seq)/3)
    nthirdindex = fthirdindex * 2
    newseq = seq[fthirdindex:nthirdindex] + seq[nthirdindex:] + seq[:fthirdindex]
    return newseq

mylist = (25, 7, 19, -5, 41, 601, 603, 4, 126, 1210, 14, 31, 1, -17, 2, 1, -401)
mystring = 'this is my test string'

print("Original List:", mylist)
print("Exchange First/Last:", exchange_first_last(mylist))
print("Remove Every Other:", remove_every_other(mylist))
print("Remove 4 then Every Other:", remove_4_then_every_other(mylist))
print("Reverse:", reverse(mylist))
print("Thirds:", thirds(mylist))

print()

print("Original String:", mystring)
print("Exchange First/Last:", exchange_first_last(mystring))
print("Remove Every Other:", remove_every_other(mystring))
print("Remove 4 then Every Other:", remove_4_then_every_other(mystring))
print("Reverse:", reverse(mystring))
print("Thirds:", thirds(mystring))

