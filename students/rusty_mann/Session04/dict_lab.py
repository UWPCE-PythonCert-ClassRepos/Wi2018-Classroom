#!/usr/bin/env python3


#Dictionaries 1
person = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

print(person)

person.pop('cake')
#del person['cake']

print(person)

person["fruit" ] = "Mango"

print(person)


#for x in person:
    #print( x)
print(person.keys())
print(person.values())

"cake" in person.keys()
"Mango" in person.values()

'''
if "cake" in person.keys():
    print(True)
else:
    print(False)

if "Mango" in person.values():
    print(True)
else:
    print(False)
'''

#Dictionaries 2
for k, v in person.items():




'''
def check_keys(key):
    for k in person:
        if k == key:
            return True
        else:
            return False

print(check_keys("cake"))
'''

#print(person)

'''
def check_vals(key, val):
    for k, v in person.items():
        if v == val:
            return True
        else:
            return False

print(check_vals("fruit", "Mango"))
'''

#Sets
s2 = set([2,4,6,8,10])
s3 = set([3,6,9,12,15])
s4 = set([4,8,12,16,20])


