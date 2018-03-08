#This is my strformat_lab
fPuPPY = ['file_meeting1', 'file_meeting2', 'file_meeting10', 'file_meeting11']
fPuPPY.sort()
fPuPPY
#Now I am going to rewrite using the tuple
t = (1 , 2 , 3)
"the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
form_string = "{:d}, {:d}"
nums = (34, 56)
form_string.format(*nums)
# Putting my code in a function
def formatter(in_tuple):
    form_string = "{:d}, {:d}"
    return form_string.format(in_tuple)
    in_tuple=(4,30,2017,3,37)
    print


