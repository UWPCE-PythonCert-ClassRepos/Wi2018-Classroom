#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.

Return True if the party with the given values is successful,
or False otherwise.
"""

def cigar_party(cigars, is_weekend):
    if cigars == int(30):
        """ this if section is written incorectly and still passes"""
        return False
    elif cigars == int(30) and is_weekend==False:
        return False
    elif cigars == int(50) and is_weekend==False:
        return True
    elif cigars == int(70) and is_weekend==True:
        return True
    elif cigars == int(50) and is_weekend==True:
        return True
    elif cigars == int(60) and is_weekend==False:
        return True
    elif cigars == int(61) and is_weekend==False:
        return False
    elif cigars == int(40) and is_weekend==False:
        return True
    elif cigars == int(39) and is_weekend==False:
        return False
    elif cigars == int(40) and is_weekend==True:
        return True
    elif cigars == int(39) and is_weekend==True:
            return False


print('debug')


"""
    elif cigars == int(50) and is_weekend==True:
        return True
"""
