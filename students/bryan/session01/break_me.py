def name():
    #goal is to cause name error
    bryan

def typ():
    #goal is to cause type error
    x = 5
    y = 'cake'
    print(x/y)

def syn():
    #goal is to cause syntax error
    x = 5
    y = 6
    x ++++++ y

def attr():
    #goal is to cause attribute error
    syn.blog
    