
#Task One
nums = (2, 123.4567, 10000, 12345.67)
format_string = "file_{:03}, {:.2f}, {:.2e}, {:.3G}"
print(format_string.format(*nums))


#Task Two
f_strformat = f"file_{nums[0]:03}, {nums[1]:.2f}, {nums[2]:.2e}, {nums[3]:.3G}"
print(f_strformat)

#Task Three
def form_string(*nums):
    n = len(nums)
    fstring = "The " +str(n) + " numbers are: " + "{:d}, "*(n-1) + "{:d}"
    return fstring.format(*nums)
print(form_string(2,3,600,58,79,236,14))


#Task Four
date = (4,30,2017,2,27)
stringy = "{3:02} {4} {2} {0:02} {1}"
print(stringy.format(*date))


#Task Five
n = ["oranges", 1.3, "lemons", 1.1]
print(f"The weight of an {(n[0])[0:6]}is {n[1]} and the weight of a {(n[2])[0:5]} is {n[3]}")


#Task Six
def make_table(cols):
    '''cols is a sequence of three element sequences, first element is name, second is age, and third is cost'''
    col_names = ["Name", "Age", "Cost"]
    headers = f'{col_names[0]:13}{col_names[1]:3}{col_names[2]:^13}'
    print(headers)
    for n in range(len(cols)):
        columns = f'{(cols[n])[0]:13}{(cols[n])[1]:0>3}{(cols[n])[2]:>13}'
        print(columns)
make_table([["Batman", 38, "$100,000.00"], ["Thor", 5, "$100.00"], ["Sponge Bob", 116, "$1,000.00"]])

