#!/usr/bin/python3
#dictionaries

dict1 = {'name':'Chris','city':'Seattle','cake':'Chocolate'}

print(dict1)

dict1.pop('cake', None)

print(dict1)

dict1['fruit'] = 'mango'

print(dict1)
print(dict1.keys())
print(dict1.values())

print('cake' in dict1.keys())
print('mango' in dict1.values())

#Sets part 1

dict2 = {}
for key in dict1.keys():
	dict2[key] = dict1[key].lower().count('t')

print(dict2)

s2 = set()
s3 = set()
s4 = set()

for i in range(21):
	if i%2 == 0:
		s2.update({i})
	if i%3 == 0:
		s3.update({i})
	if i%4 == 0:
		s4.update({i})

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets part 2
setPython = set('Python')
setPython.add('i')
setMarathon = frozenset('marathon')

print(setPython)
print(setPython.issubset(setMarathon))
print(setPython.intersection(setMarathon))