def bar_row(a):
    print (a*'|    ' + '|', end=' ')

def subgrid(n):
    print (n*'+----' + '+', end=' ')
    print ()
    bar_row (n)
    print ()
    bar_row (n)
    print ()
def grid_prt(n):
    for i in range(n):
        subgrid(n)
def final_grid(n):
    grid_prt(n)
    print (n*'+----' + '+', end=' ')

# Try final_grid(2) 
#+----+----+
#|    |    |
#|    |    |
#+----+----+
#|    |    |
#|    |    |
#+----+----+

