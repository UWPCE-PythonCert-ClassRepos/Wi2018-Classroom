name1 = 'name'; name2='shane'; name3='Sean'
age1='age'; age2='39'; age3='4'
cost1='cost'; cost2='$100'; cost3='$4000'

def some_code():
    print('{:10}{:10}{:10}'.format(name1, age1, cost1),end=' ')
    print()
    print ('{:10}{:10}{:10}'.format(name2, age2, cost2),end=' ')
    print()
    print ('{:10}{:10}{:10}'.format(name3, age3, cost3), end=' ')

