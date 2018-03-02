#!/usr/bin/env python

# Task 1
my_string = 'file_{:0>3d} :\t{:.2f}, {:.2e}, {:.2e}'.format( 2, 123.4567, 10000, 12345.67 )

print(my_string)


# Task 2
string_tuple = ( 2, 123.4567, 10000, 12345.67 )

my_string2 = (f"file_{string_tuple[0]:0>3d} :\t{string_tuple[1]:.2f}, "
              f"{string_tuple[2]:.2e}, {string_tuple[3]:.2e}")

print(my_string2)


# Task 3
