
#Task One
nums = (2, 123.4567, 10000, 12345.67)
format_string = "file_{:03}, {:.2f}, {:.2e}, {:.3G}"
print(format_string.format(*nums))

#Task Two
f_strformat = f"file_{2:03}, {123.4567:.2f}, {10000:.2e}, {12345.67:.3G}"
print(f_strformat)

#Task Three
def form_string(*nums):
    n = len(nums)
    fstring = "The " +str(n) + " numbers are: " + "{:d}, "*(n-1) + "{:d}"
    return fstring.format(*nums)


print(form_string(2,3,600,58,79,236,14))


