# Warmup-2 > last2
def last2(str):
    searchVar = str[-2:]

    count = 0
    for i in range(0,len(str)-2):
        if str[i:i+2] == searchVar:
            count+=1
    
    return count

# Logic-2 > lone_sum
def lone_sum(a, b, c):
    myList = [a, b, c]
    
    sum = 0

    for i in myList:
        if myList.count(i) == 1:
            sum += i

    return sum
    

# last2('axxxaaxx')
# lone_sum(1, 2, 3)
