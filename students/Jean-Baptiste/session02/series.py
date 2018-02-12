def fibonacci(limit, sequence=None):
    if sequence is None:
        sequence = [0,1]
    else:
        sequence.append(sequence[-1] + sequence[-2])
    #print('limit', limit)
    #print('len sequence', len(sequence))
    if limit >= len(sequence):
        return fibonacci(limit -1,sequence)
    else:
        return sequence
print("serie of fibonacci")
print(fibonacci(12))
#The Lucas sequences adds the previous two numbers together
# A related series of integers that start with the values 2 and 1 rather than 0 and 1
#E.g 2, 1, 3, 4, 7, 11, 18, 29, ...
#Both the fibonacci series and the lucas numbers are based on an identical formula
def lucas(limit, sequence=None):
    if sequence is None:
        sequence = [2,1]
    else:
        sequence.append(sequence[-1] + sequence[-2])
    #print('limit', limit)
    #print('len sequence', len(sequence))
    if limit >= len(sequence):
        return lucas(limit -1,sequence)
    else:
        return sequence
print("serie of lucas")
print(lucas(12))