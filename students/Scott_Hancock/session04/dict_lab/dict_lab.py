# Dictionaries 1
newDict = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(newDict)

del newDict['cake']
print(newDict)

newDict['fruit'] = 'Mango'
print(newDict)

print(newDict.keys())
print(newDict.values())
print('cake' in newDict.keys())
print('Mango' in newDict.values())

# Dictionaries 2
secondDict = newDict.copy()
for d in secondDict:
    secondDict[d] = newDict[d].count('t') + newDict[d].count('T')
print(secondDict)

# Sets 1
s2 = set()
s3 = set()
s4 = set()

for i in range(0, 21):
    if (i%2 == 0):
        s2.add(i)
    if (i%3 == 0):
        s3.add(i)
    if (i%4 == 0):
        s4.add(i)

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2
setP = set("Python")
setP.add('i')
print(setP)
setM = frozenset("marathon")
print(setM)
print(setM.union(setP))
print(setM.intersection(setP))





