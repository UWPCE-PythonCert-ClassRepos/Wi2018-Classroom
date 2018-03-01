# slicing assignment
def first_last_exchange(seq):
    return seq[-1:] + seq[1:len(seq)-1] + seq[:1]
 
def remove_every_other_item(seq):
    return seq[::2]
 
def remove_4_then_every_other_item(seq):
    return seq[4:][:-4][::2]
 
def reverse(seq):
    return seq[::-1]
 
def thirds(seq):
    fthirdindex = round(len(seq)/3)
    nthirdindex = fthirdindex * 2
    newseq = seq[fthirdindex:nthirdindex] + seq[nthirdindex:] + seq[:fthirdindex]
    return newseq
 
mylist = (100, 20, 30, 40, 50, 70, 90, 80, 10, -50, 110,)
mystring = 'this is my test data'
 
 print("Given List:", mylist)
 print("Exchange First/Last:", first_last_exchange(mylist))
 print("Remove Every Other:", remove_every_other_item(mylist))
 print("Remove 4 then Every Other:", remove_4_then_every_other_item(mylist))
 print("Reverse:", reverse(mylist))
 print("Thirds:", thirds(mylist))
 print("Original String:", mystring)
 print("Exchange First/Last:", first_last_exchange(mystring))
 print("Remove Every Other:", remove_every_other_item(mystring))
 print("Remove 4 then Every Other:", remove_4_then_every_other_item(mystring))
 print("Reverse:", reverse(mystring))
 print("Thirds:", thirds(mystring))