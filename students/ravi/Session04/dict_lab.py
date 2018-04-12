d = {'name':'Chris','city':'Seattle','cake':'Chocolate'}
print(d)

d.pop('cake')
print(d)

d['fruit']='Mango'
print(d)

print(d.keys())
print(d.values())

print('cake' in d.keys())
print('Mango' in d.values())

d['name']=d.get('name').count('t') + d.get('name').count('T')
d['city']=d.get('city').count('t') + d.get('city').count('T')
d['fruit']=d.get('fruit').count('t') + d.get('fruit').count('T')
print(d)


s2=set()
s3=set()
s4=set()
for i in range(21):
    if i%2==0:
        s2.add(i)
    if i%3==0:
        s3.add(i)
    if i%4==0:
        s4.add(i)
print (s2,s3,s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

s = set('Python')
print(s)
s.add('i')
print(s)

fs=frozenset('marathon')
print(fs)
print(s.union(fs))
