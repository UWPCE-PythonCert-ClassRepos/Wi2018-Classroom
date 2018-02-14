def grid(x,y):
    count1=0
    while count1<x:                 # keeps count of squares to repeat
        border1=0
        while border1<x:            # prints and repeats first row/pattern
            patternA = ('+'+'-'*y)
            print(patternA,end='')
            border1+=1
        print('+')
        count2=0
        while count2<y:             # prints and repeats second row/pattern
            border2=0
            while border2<x:
                patternB = ('|'+' '*y)
                print(patternB,end='')
                border2+=1
            print('|')
            count2+=1
        count1+=1
    border1=0
    while border1<x:                # prints the last row
        patternA = ('+'+'-'*y)
        print(patternA,end='')
        border1+=1
    print('+')