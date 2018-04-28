def dictonaries_2():
    """Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?)."""
new_dict = {'name':'Chris','city':'Seattle','fruit':'Mango'}
new_dict2 = {}
new_dict2 = dict.fromkeys(['name','city','fruit'])
test = 0

for k,v in new_dict.items():
    test = v.count('t')
    new_dict2[k] = test
    print (new_dict2.values())
    print (new_dict2.keys())
