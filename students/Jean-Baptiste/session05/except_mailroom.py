#!/usr/bin/python//Wi2018-Classroom/students/jean-baptisteyamindi/session05
#This is to proper exception handler in the except mailroom code, so that the code can run.
#We make sure to catch specifically the error you find
NameError
~/Pythonpython/Wi2018-Classroom/students/jean-baptisteyamindi/session05 except-mailroom.py in mailroom()
first_try = ["Donor list:"]
listing_except = listing.append(first_try[0])
~/PythonStuff/UWPCE/Temp/except_test.py in listing.append(donor)
def listing.append(donor):
          if donor == 'name':
                 print(s)
                  elif donor == 'menu':
                   print()
                   NameError: name 's' is not defined
# Here is a try/except block. Add an else that prints not_listing_except
try:
    not_listing_except = listing_except = listing.append(first_try[2])
except SyntaxError:
    print('Run Away!')