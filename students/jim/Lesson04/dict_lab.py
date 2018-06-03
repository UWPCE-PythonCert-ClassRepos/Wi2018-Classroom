# Dictionaries 1

my_dict = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(my_dict)

my_dict.pop('cake')

print('cake' in my_dict)
print(my_dict)

my_dict['fruit'] = 'Mango'
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print('cake' in my_dict)
print('Mango' in my_dict.values())

# Dictionaries 2

for key in my_dict:
    lowercase = my_dict[key].lower()
    my_dict[key] = lowercase.count('t')
print(my_dict)

# Sets 1

s2, s3, s4 = set(), set(), set()
for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2

letter_set = set()
letter_set.update("Python")
letter_set.add('i')

froset = set()
froset.update("marathon")
froset = frozenset(froset)

print(letter_set.union(froset))
print(letter_set.intersection(froset))