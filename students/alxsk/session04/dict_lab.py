'''
Dictionaries & Sets Lab

Working with dictionaries and sets
'''

#Dictionaries 1
cake_dict={'name':'Chris','city':'Seattle','cake':'chocolate'}
print(cake_dict)

cake_dict.pop('cake', "Not present")
print(cake_dict)


cake_dict['fruit']="mango"
print(cake_dict)

print(cake_dict.keys())
print(cake_dict.values())

print('cake' in cake_dict)
print('mango' in cake_dict.values())
print()

#Dictionaries 2
#Make a dictionary using the same keys but with the number of ‘t’s in each value as the value
cake_dict={'name':'Chris','city':'Seattle','cake':'chocolate'}
for vals in cake_dict.values(): 
    print(vals)
    count=str(vals.lower().count('t'))
    print(count)
    
cake_dict.pop('name')
cake_dict.pop('city')
cake_dict.pop('cake')
cake_dict['name']=count


print(cake_dict)
print()

#Sets 1
s2 = set([2,4,6,8,10,12,14,16,18,20])
print(s2)
s3 = set([3,6,9,12,15,18])
print(s3)
s4 = set([4,8,12,16,20])
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))
print()

# Sets 2    
py=set('python')
py.update('i')
print(py)

fz_marathon=set('marathon')

print(py.union(fz_marathon))
print(py.intersection(fz_marathon))



