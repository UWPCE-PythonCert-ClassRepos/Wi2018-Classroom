print('LIST COMPREHENSIONS')
feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

#This will capitalize the first letter in each index in the feast list
comprehension = [delicacy.capitalize() for delicacy in feast]
print(comprehension)
print(comprehension[0])
print(comprehension[2])
print()

print('FILTERING WITH LIST COMPREHENSIONS')
feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

#This will only append elements to comp if the length of the item in the
#feast list is longer than 6 characters
#orangutans
#breakfast cereals
#fruit bats
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print(comp)
len(feast)
len(comp)
print()


print("UNPACKING TUPLES IN LIST COMPREHENSIONS")
#Will multiply the number found in each tuple by the word found in each
#tuple.  lumberjack * 1 = lumberjack
#2 * inquisition = inquisitioninquisition
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [skit * number for number, skit in list_of_tuples]
print(comprehension)
print(comprehension[0])
print(len(comprehension))

print("DOUBLE LIST COMPREHENSIONS:")
#Will create a list of length 6.  Each element in eggs list will be paired with
#each element in meats list. They are formatted using the string format '{0} and {1}'.format(egg, meat)
eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print(comprehension)
print(len(comprehension))
print(comprehension[0])
print()

print("SET COMPREHENSIONS")
#Creates a set of just (a, b, c)
comprehension = {c for c in 'aabbbcccc'}
print(comprehension)

print()
#will load the dictionary (dict_comprehension) with all uppercase letters of the key
#from dict_of_weapons followed by the weapon the key is associated with.  The key
#will only be added if a weapon exists in the dict_of_weapons dictionary
print("DICTIONARY COMPREHENSIONS:")
dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print(len(dict_of_weapons))
print()
print("ish")

print('COUNT EVEN NUMBERS')
def count_evens(nums):
    evens_list = [number for number in nums if number % 2 == 0]
    return len(evens_list)


evens_test1 = [2,1,2,3,4]
evens_test2 = [2,2,0]
evens_test3 = [1,3,5]
test1 = count_evens(evens_test1)
test2 = count_evens(evens_test2)
test3 = count_evens(evens_test3)
print("Evens test 1: " + test1)
print("Evens test 2: " + test2)
print("Evens test 3: " + test3)