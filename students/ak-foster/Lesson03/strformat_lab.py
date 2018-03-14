#!/usr/bin/env python3

def tasks():
    # Task 1
    test = (2, 123.4567, 10000, 12345.67)
    output1 = 'file_00' + str(test[0]) + ':   ' + str(round(test[1], 2)) + ', ' + '{:.2e}'.format(test[2]) + ', ' + '{:.2e}'.format(test[3])
    print(output1)

    # Task 2
    th = 'file_00'
    st = str(test[0])
    nd = str(round(test[1], 2))
    rd = '{:.2e}'.format(test[2])
    xh = '{:.2e}'.format(test[3])

    output2 = th + st + ':   ' + nd + ', ' + rd + ', ' + xh
    print(output2)

# Task 3
def numbers_are(s):
    """Take an arbitrary number of values and build into dynamic string."""
    l = len(s)
    return ('the {:d} numbers are: ' + '{:d}, '*(l-1) + '{:d}').format(l,*s)


# Task 4
t = (4, 30, 2017, 2, 27)
output = ('{:02d} ' * 4 + '{:d}').format(t[-2], t[-1], t[2], t[0], t[1])
print(output)

# Task 5
t = ['oranges', 1.3, 'lemons', 1.1] # yes, I know I'm writing over t
print(f'The weight of an {t[0].upper()} is {t[1] * 1.2} and the weight of a {t[2].upper()} is {t[3] * 1.2}')

# Task 6 - instructions don't make sense
