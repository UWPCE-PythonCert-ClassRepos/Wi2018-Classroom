
def switch_first_last(seq):
    mid = seq[1:-1]
    new = seq[-1:] + mid + seq[:1]
    return new


print(switch_first_last("this is a string"))
print(switch_first_last([1,2,3,4,5,6,7,8,9,0]))
print(switch_first_last((1,2,3,4,5,6,7,8,9,0)))

