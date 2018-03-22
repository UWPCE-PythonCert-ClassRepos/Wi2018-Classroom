#!/usr/bin/env python

def formatter(in_tuple):
    """ Return string of variable length of tuple  """
    count = len(in_tuple)
    
    form_string = f"the {count} numbers are:"

    for num in range(count):
        form_string += ' {:d},'

    form_string = form_string[:-1]
    
    return form_string.format(*in_tuple)


if __name__=='__main__':
    # Task 1
    print("\nTask 1:")
    my_string = 'file_{:0>3d} :\t{:.2f}, {:.2e}, {:.2e}'.format( 2, 123.4567, 10000, 12345.67 )

    print(my_string)


    # Task 2
    print("\nTask 2:")
    string_tuple = ( 2, 123.4567, 10000, 12345.67 )

    my_string2 = (f"file_{string_tuple[0]:0>3d} :\t{string_tuple[1]:.2f}, "
                  f"{string_tuple[2]:.2e}, {string_tuple[3]:.2e}")

    print(my_string2)


    # Task 3
    print("\nTask 3:")
    print(formatter((2,3,5)))
    print(formatter((2,3,5,7,9)))


    # Task 4
    print("\nTask 4:")
    print("{3:0>2d} {4} {2} {0:0>2d} {1}".format( 4, 30, 2017, 2, 27))


    # Task 5
    print("\nTask 5:")
    string_list = ['oranges', 1.3, 'lemons', 1.1]

    print(f"The weight of an {string_list[0][:-1].upper()} is {string_list[1]*1.2} "
          f"and the weight of a {string_list[2][:-1].upper()} is {string_list[3]*1.2}")


    # Task 6
    print("\nTask 6:")
    row_0 = ['Name', 'Age', 'Cost']
    row_1 = ['Bill', 99, 50000]
    row_2 = ['Cory', 12, 29000000.53]
    row_3 = ['Suzanne', 42, 0.39]

    my_data = list([row_1, row_2, row_3])
    col_widths = [10, 5, 15]
    
    print(f"{row_0[0]:<{col_widths[0]}}{row_0[1]:<{col_widths[1]}}{row_0[2]:<{col_widths[2]}}")
    print('-' * (sum(col_widths) + 1))
    for row in my_data:
        print(f"{row[0]:<{col_widths[0]}}{row[1]:^{col_widths[1]}d}${row[2]:{col_widths[2]},.2f}")


    # Task 6a
    print("\nTask 6a:")
    my_tuple = tuple(range(10))
    print("My tuple:",my_tuple)
    print(('{:5d}'*10).format(*my_tuple))
