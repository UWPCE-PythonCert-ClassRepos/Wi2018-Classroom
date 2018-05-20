def first_last_swap(a,b,c):
    """with the first and last items exchanged"""
    l = a,b,c
    print (len(l))
    print ((l[2]) ,(l[1]) ,(l[0]))

def every_other(a,b,c):
    """with every other item removed"""
    l = a,b,c
    print (len(l))
    print (l[::2])

def first_4_last_4(a,b,c):
    """with the first 4 and the last 4 items removed, and then every other item in between"""
    l = (a,b,c)*4
    print (len(l))
    print ((l[4:-4]) + l[::2])

def reversed_list(a,b,c):
    """with the elements reversed (just with slicing)"""
    l = a,b,c
    print (len(l))
    print ((l[::-1]))

def thirds(a,b,c):
    """return with the middle third, then last third, then the first third in the new order."""
    l = (a,b,c)*3
    f_t = int(len(l)/3)
    m_t = int((len(l)/3)*2)
    l_t = int((len(l)/3)*3)
    print (len(l))
    print (l)
    print(l[f_t:m_t] + l[m_t:l_t] + l[:f_t])
