#!/usr/bin/env python

# Write format string that will take the following tuple and produce the
# desired output.
input_tuple = ( 2, 123.4567, 10000, 12345.67 )
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'
my_string = 'file_{} :\t{}, {}, {}'.format(input_tuple)
