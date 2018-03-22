def f(*args, **kwargs):
    print("the positionals are", args)
    print("the keywords are", kwargs)
    argsum = sum(args)
    kwargsum = sum(kwargs.values())
    print(argsum)
    print(kwargsum)


def g(f_arg, x=2, y=2):
    print(f_arg, x*y)
    return
    
