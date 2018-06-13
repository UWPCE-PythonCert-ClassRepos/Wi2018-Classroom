"""
Memoization test/comparison using recursive factorial function
"""

import timeit

def memoize(f):
    """
    Wrapper for memoization decorator
    """
    class memodict(dict):
        """
        Memoization decorator class using dictionary
        """
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def recurfact_memo(n):
    """ 
    Decorator memoized version of a simple recursive factorial function
    """
    if n == 1:
        return 1
    return n * recurfact_memo(n - 1)

def recurfact_nonmemo(n):
    """
    Non-memoized version of a simple recursive factorial function
    """
    if n == 1:
        return 1
    return n * recurfact_nonmemo(n-1)

if __name__ == '__main__':
    print("Running recursive factorial(50) a million times...")
    print("Memoized recursive factorial(50): ", 
        timeit.timeit('recurfact_memo(50)', 
        setup='from __main__ import recurfact_memo', number=1000000))
    print("Non-memoized recursive factorial(50): ", 
        timeit.timeit('recurfact_nonmemo(50)', 
        setup='from __main__ import recurfact_nonmemo', number=1000000))
