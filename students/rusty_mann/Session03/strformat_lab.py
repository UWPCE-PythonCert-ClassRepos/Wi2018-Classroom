
#Task One
nums = (2, 123.4567, 10000, 12345.67)
format_string = "file_{:03}, {:.2f}, {:.2e}, {:.3G}"
print(format_string.format(*nums))

#Task Two
f_strformat = f"file_{2:03}, {123.4567:.2f}, {10000:.2e}, {12345.67:.3G}"
print(f_strformat)

#Task Three
nums = (34, 56, 72, 98, 21)
n= len(nums) 
form_string1 = "the {:d} numbers are: "
form_string2 = " {:d}, "*(len(nums)-1) + "{:d}"
part1 = form_string1.format(n) 
part2 = form_string2.format(*nums)
print(part1+part2)

